/**
 * FortiWAN-E — WAN Emulator Frontend
 */

const API = {
    async request(method, url, body = null) {
        const opts = {
            method,
            headers: { 'Content-Type': 'application/json' },
        };
        if (body) opts.body = JSON.stringify(body);
        const resp = await fetch(url, opts);
        const data = await resp.json();
        if (data.status === 'error') throw new Error(data.message);
        return data;
    },
    connect: (d) => API.request('POST', '/api/connect', d),
    disconnect: () => API.request('POST', '/api/disconnect'),
    fabrics: () => API.request('GET', '/api/fabrics'),
    topology: (id) => API.request('GET', `/api/fabric/${id}/topology`),
    routerPorts: (id) => API.request('GET', `/api/router/${id}/ports`),
    presets: () => API.request('GET', '/api/presets'),
    apply: (d) => API.request('POST', '/api/apply', d),
    clear: (d) => API.request('POST', '/api/clear', d),
    status: () => API.request('GET', '/api/status'),
};

// State
const state = {
    connected: false,
    fabricId: null,
    topology: null,
    selectedRouter: null,
    presets: {},
    interfaceParams: {},
};

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => document.querySelectorAll(sel);

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
    setupEventListeners();
    await loadPresets();
    await checkConnection();
});

function setupEventListeners() {
    $('#connect-form').addEventListener('submit', handleConnect);
    $('#btn-disconnect').addEventListener('click', handleDisconnect);
    $('#btn-load-topology').addEventListener('click', handleLoadTopology);
    $('#btn-clear-log').addEventListener('click', () => { $('#log-entries').innerHTML = ''; });
}

// --- Connection ---

async function handleConnect(e) {
    e.preventDefault();
    const btn = $('#btn-connect');
    btn.disabled = true;
    btn.textContent = 'Connecting...';

    try {
        await API.connect({
            host: $('#fs-host').value.trim(),
            username: $('#fs-user').value.trim(),
            password: $('#fs-pass').value,
        });
        setConnected(true);
        toast('Connected to Fabric Studio', 'success');
        await loadFabrics();
    } catch (err) {
        toast(err.message, 'error');
    } finally {
        btn.disabled = false;
        btn.textContent = 'Connect';
    }
}

async function handleDisconnect() {
    try { await API.disconnect(); } catch (_) {}
    setConnected(false);
    state.fabricId = null;
    state.topology = null;
    state.selectedRouter = null;
    $('#fabric-panel').classList.add('hidden');
    $('#topology-panel').classList.add('hidden');
    $('#emulator-panel').classList.add('hidden');
    $('#log-panel').classList.add('hidden');
    toast('Disconnected', 'success');
}

function setConnected(val) {
    state.connected = val;
    const badge = $('#connection-badge');
    const text = $('#connection-text');
    if (val) {
        badge.className = 'badge badge-connected';
        text.textContent = `Connected to ${$('#fs-host').value}`;
        $('#btn-connect').classList.add('hidden');
        $('#btn-disconnect').classList.remove('hidden');
        $('#fabric-panel').classList.remove('hidden');
    } else {
        badge.className = 'badge badge-disconnected';
        text.textContent = 'Disconnected';
        $('#btn-connect').classList.remove('hidden');
        $('#btn-disconnect').classList.add('hidden');
    }
}

async function checkConnection() {
    try {
        const data = await API.status();
        if (data.status === 'connected') {
            $('#fs-host').value = data.host;
            $('#fs-user').value = data.username;
            setConnected(true);
            await loadFabrics();
        }
    } catch (_) {}
}

// --- Fabrics ---

async function loadFabrics() {
    try {
        const data = await API.fabrics();
        const sel = $('#fabric-select');
        sel.innerHTML = '<option value="">-- Select a Fabric --</option>';
        (data.fabrics || []).forEach(f => {
            const opt = document.createElement('option');
            opt.value = f.id;
            opt.textContent = f.name;
            sel.appendChild(opt);
        });
    } catch (err) {
        toast('Failed to load fabrics: ' + err.message, 'error');
    }
}

// --- Topology ---

async function handleLoadTopology() {
    const fabricId = $('#fabric-select').value;
    if (!fabricId) return toast('Select a fabric first', 'error');

    state.fabricId = parseInt(fabricId);
    try {
        const data = await API.topology(fabricId);
        state.topology = data.topology;
        renderTopology(data.topology);
        $('#topology-panel').classList.remove('hidden');
        $('#log-panel').classList.remove('hidden');
    } catch (err) {
        toast('Failed to load topology: ' + err.message, 'error');
    }
}

function renderTopology(topo) {
    const container = $('#topology-diagram');
    container.innerHTML = '';

    const allDevices = [
        ...(topo.routers || []).map(d => ({ ...d, type: 'router' })),
        ...(topo.vms || []).map(d => ({ ...d, type: 'vm' })),
        ...(topo.switches || []).map(d => ({ ...d, type: 'switch' })),
    ];

    if (allDevices.length === 0) {
        container.innerHTML = '<p style="color:var(--text-muted)">No devices found in this fabric.</p>';
        return;
    }

    allDevices.forEach(dev => {
        const el = document.createElement('div');
        el.className = `topo-device type-${dev.type}`;
        el.dataset.id = dev.id;
        el.dataset.type = dev.type;

        const iconText = dev.type === 'router' ? 'R' : dev.type === 'vm' ? 'VM' : 'SW';
        const portCount = (dev.ports || []).length;

        el.innerHTML = `
            <div class="topo-icon">${iconText}</div>
            <div class="topo-info">
                <div class="topo-name">${dev.name}</div>
                <div class="topo-type">${dev.type}</div>
                <div class="topo-ports">${portCount} port${portCount !== 1 ? 's' : ''}</div>
            </div>
        `;

        if (dev.type === 'router') {
            el.addEventListener('click', () => selectRouter(dev));
        }

        container.appendChild(el);
    });
}

async function selectRouter(router) {
    // Deselect all
    $$('.topo-device').forEach(el => el.classList.remove('selected'));
    const el = document.querySelector(`.topo-device[data-id="${router.id}"][data-type="router"]`);
    if (el) el.classList.add('selected');

    state.selectedRouter = router;
    state.interfaceParams = {};

    // Use ports from topology; if empty, fetch separately
    let ports = router.ports || [];
    if (ports.length === 0) {
        try {
            const data = await API.routerPorts(router.id);
            ports = data.ports || [];
            // Update the topology device too
            router.ports = ports;
            // Update port count in topology view
            if (el) {
                const portsEl = el.querySelector('.topo-ports');
                if (portsEl) portsEl.textContent = `${ports.length} port${ports.length !== 1 ? 's' : ''}`;
            }
        } catch (err) {
            addLog(`Failed to fetch ports for ${router.name}: ${err.message}`, 'error');
        }
    }

    ports.forEach(p => {
        const name = p.name || `eth${p.id}`;
        state.interfaceParams[name] = defaultParams();
    });

    renderEmulator(router);
    $('#emulator-panel').classList.remove('hidden');
    $('#emulator-title').textContent = `WAN Emulation — ${router.name}`;
}

function defaultParams() {
    return {
        delay_ms: 0, jitter_ms: 0, loss_percent: 0,
        bandwidth_kbit: 0, corrupt_percent: 0,
        duplicate_percent: 0, reorder_percent: 0,
        correlation_percent: 0,
    };
}

// --- Presets ---

async function loadPresets() {
    try {
        const data = await API.presets();
        state.presets = data.presets;
    } catch (_) {
        state.presets = {};
    }
}

function applyPresetToInterface(iface, key) {
    const preset = state.presets[key];
    if (!preset) return;

    state.interfaceParams[iface] = {
        delay_ms: preset.delay_ms || 0,
        jitter_ms: preset.jitter_ms || 0,
        loss_percent: preset.loss_percent || 0,
        bandwidth_kbit: preset.bandwidth_kbit || 0,
        corrupt_percent: preset.corrupt_percent || 0,
        duplicate_percent: preset.duplicate_percent || 0,
        reorder_percent: preset.reorder_percent || 0,
        correlation_percent: 0,
    };

    // Re-render just this card
    renderEmulator(state.selectedRouter);
    addLog(`Preset "${preset.label}" applied to ${iface}`);
}

// --- Emulator Controls ---

function renderEmulator(router) {
    const container = $('#interface-cards');
    container.innerHTML = '';

    const entries = Object.entries(state.interfaceParams);

    if (entries.length === 0) {
        container.innerHTML = '<p style="color:var(--text-muted)">No ports found on this router. The router may not have ports configured yet.</p>';
        return;
    }

    entries.forEach(([iface, params]) => {
        const card = createInterfaceCard(iface, params);
        container.appendChild(card);
    });
}

function createInterfaceCard(iface, params) {
    const card = document.createElement('div');
    card.className = 'iface-card';
    card.dataset.iface = iface;

    const hasRules = Object.entries(params).some(([k, v]) => k !== 'correlation_percent' && v > 0);

    // Build preset options
    let presetOptions = '<option value="">-- Select Preset --</option>';
    Object.entries(state.presets).forEach(([key, preset]) => {
        presetOptions += `<option value="${key}">${preset.label}</option>`;
    });

    card.innerHTML = `
        <div class="iface-header">
            <div class="iface-name">
                <span class="dot ${hasRules ? 'active' : ''}"></span>
                ${iface}
            </div>
            <div class="iface-header-actions">
                <select class="preset-select" data-iface="${iface}">
                    ${presetOptions}
                </select>
                <button class="btn btn-sm btn-primary btn-apply" data-iface="${iface}">Apply</button>
                <button class="btn btn-sm btn-danger btn-clear" data-iface="${iface}">Clear</button>
            </div>
        </div>
        <div class="iface-body">
            ${slider(iface, 'delay_ms', 'Delay', params.delay_ms, 0, 2000, 1, 'ms')}
            ${slider(iface, 'jitter_ms', 'Jitter', params.jitter_ms, 0, 500, 1, 'ms')}
            ${slider(iface, 'loss_percent', 'Packet Loss', params.loss_percent, 0, 100, 0.1, '%')}
            ${slider(iface, 'corrupt_percent', 'Corruption', params.corrupt_percent, 0, 50, 0.1, '%')}
            ${slider(iface, 'duplicate_percent', 'Duplicates', params.duplicate_percent, 0, 50, 0.1, '%')}
            ${slider(iface, 'reorder_percent', 'Reorder', params.reorder_percent, 0, 50, 0.1, '%')}
            ${slider(iface, 'bandwidth_kbit', 'Bandwidth Limit', params.bandwidth_kbit, 0, 1000000, 100, 'kbit/s', true)}
        </div>
    `;

    // Attach event listeners after DOM insertion
    setTimeout(() => {
        // Sliders
        card.querySelectorAll('input[type="range"]').forEach(input => {
            input.addEventListener('input', (e) => {
                const param = e.target.dataset.param;
                const val = parseFloat(e.target.value);
                state.interfaceParams[iface][param] = val;
                const display = e.target.closest('.slider-group').querySelector('.slider-value');
                display.textContent = formatValue(val, e.target.dataset.unit);
                // Reset preset dropdown
                const sel = card.querySelector('.preset-select');
                if (sel) sel.value = '';
                updateCardStatus(iface);
            });
        });

        // Preset dropdown
        const presetSel = card.querySelector('.preset-select');
        if (presetSel) {
            presetSel.addEventListener('change', (e) => {
                if (e.target.value) applyPresetToInterface(iface, e.target.value);
            });
        }

        // Apply button
        const applyBtn = card.querySelector('.btn-apply');
        if (applyBtn) {
            applyBtn.addEventListener('click', () => handleApplyInterface(iface));
        }

        // Clear button
        const clearBtn = card.querySelector('.btn-clear');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => handleClearInterface(iface));
        }
    }, 0);

    return card;
}

function slider(iface, param, label, value, min, max, step, unit, fullWidth = false) {
    return `
        <div class="slider-group ${fullWidth ? 'full-width' : ''}">
            <div class="slider-label">
                <span>${label}</span>
                <span class="slider-value">${formatValue(value, unit)}</span>
            </div>
            <input type="range" min="${min}" max="${max}" step="${step}" value="${value}"
                   data-iface="${iface}" data-param="${param}" data-unit="${unit}">
        </div>
    `;
}

function formatValue(val, unit) {
    if (unit === 'kbit/s') {
        if (val === 0) return 'Unlimited';
        if (val >= 1000) return `${(val / 1000).toFixed(1)} Mbit/s`;
        return `${val} kbit/s`;
    }
    if (val === 0) return `0 ${unit}`;
    return `${val} ${unit}`;
}

function updateCardStatus(iface) {
    const params = state.interfaceParams[iface];
    const hasRules = Object.entries(params).some(([k, v]) => k !== 'correlation_percent' && v > 0);
    const card = document.querySelector(`.iface-card[data-iface="${iface}"]`);
    if (!card) return;
    card.querySelector('.dot').className = `dot ${hasRules ? 'active' : ''}`;
}

// --- Per-Interface Apply/Clear ---

async function handleApplyInterface(iface) {
    if (!state.selectedRouter) return;

    const card = document.querySelector(`.iface-card[data-iface="${iface}"]`);
    const btn = card?.querySelector('.btn-apply');
    if (btn) { btn.disabled = true; btn.textContent = 'Applying...'; }

    try {
        const result = await API.apply({
            router_id: state.selectedRouter.id,
            interfaces: { [iface]: state.interfaceParams[iface] },
        });
        toast(`Rules applied to ${iface}`, 'success');
        addLog(`Rules applied to ${state.selectedRouter.name} / ${iface}`, 'success');
        if (result.script) addLog(`Script: ${result.script}`);
    } catch (err) {
        toast(`Failed: ${err.message}`, 'error');
        addLog(`Error applying to ${iface}: ${err.message}`, 'error');
    } finally {
        if (btn) { btn.disabled = false; btn.textContent = 'Apply'; }
    }
}

async function handleClearInterface(iface) {
    if (!state.selectedRouter) return;

    const card = document.querySelector(`.iface-card[data-iface="${iface}"]`);
    const btn = card?.querySelector('.btn-clear');
    if (btn) btn.disabled = true;

    try {
        await API.clear({
            router_id: state.selectedRouter.id,
            interfaces: [iface],
        });

        // Reset params
        state.interfaceParams[iface] = defaultParams();
        renderEmulator(state.selectedRouter);
        toast(`Rules cleared on ${iface}`, 'success');
        addLog(`Rules cleared on ${state.selectedRouter.name} / ${iface}`, 'success');
    } catch (err) {
        toast(`Failed: ${err.message}`, 'error');
        addLog(`Error clearing ${iface}: ${err.message}`, 'error');
    } finally {
        if (btn) btn.disabled = false;
    }
}

// --- Logging ---

function addLog(msg, type = '') {
    const container = $('#log-entries');
    const now = new Date().toLocaleTimeString();
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    entry.innerHTML = `<span class="log-time">${now}</span><span class="log-msg ${type}">${msg}</span>`;
    container.prepend(entry);
    while (container.children.length > 50) container.removeChild(container.lastChild);
}

// --- Toast ---

function toast(msg, type = 'success') {
    const el = document.createElement('div');
    el.className = `toast toast-${type}`;
    el.textContent = msg;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 3000);
}
