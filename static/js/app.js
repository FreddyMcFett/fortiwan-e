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
    interfaceParams: {}, // { ifaceName: { delay_ms, jitter_ms, ... } }
};

// DOM refs
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
    $('#btn-apply-all').addEventListener('click', handleApplyAll);
    $('#btn-clear-all').addEventListener('click', handleClearAll);
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
    try {
        await API.disconnect();
    } catch (_) {}
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

function selectRouter(router) {
    // Deselect all
    $$('.topo-device').forEach(el => el.classList.remove('selected'));
    // Select this one
    const el = document.querySelector(`.topo-device[data-id="${router.id}"][data-type="router"]`);
    if (el) el.classList.add('selected');

    state.selectedRouter = router;
    state.interfaceParams = {};

    // Build interface list from ports
    const ports = router.ports || [];
    ports.forEach(p => {
        const name = p.name || `eth${p.id}`;
        state.interfaceParams[name] = {
            delay_ms: 0,
            jitter_ms: 0,
            loss_percent: 0,
            bandwidth_kbit: 0,
            corrupt_percent: 0,
            duplicate_percent: 0,
            reorder_percent: 0,
            correlation_percent: 0,
        };
    });

    renderEmulator(router);
    $('#emulator-panel').classList.remove('hidden');
    $('#emulator-title').textContent = `WAN Emulation — ${router.name}`;
}

// --- Presets ---

async function loadPresets() {
    try {
        const data = await API.presets();
        state.presets = data.presets;
        renderPresets();
    } catch (_) {
        // Use fallback presets if API not available yet
        state.presets = {};
    }
}

function renderPresets() {
    const container = $('#preset-buttons');
    container.innerHTML = '';

    Object.entries(state.presets).forEach(([key, preset]) => {
        const btn = document.createElement('button');
        btn.className = 'preset-btn';
        btn.textContent = preset.label;
        btn.dataset.preset = key;
        btn.addEventListener('click', () => applyPreset(key));
        container.appendChild(btn);
    });
}

function applyPreset(key) {
    const preset = state.presets[key];
    if (!preset) return;

    // Highlight active preset
    $$('.preset-btn').forEach(b => b.classList.remove('active'));
    const btn = document.querySelector(`.preset-btn[data-preset="${key}"]`);
    if (btn) btn.classList.add('active');

    // Apply to all interfaces
    Object.keys(state.interfaceParams).forEach(iface => {
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
    });

    // Re-render sliders
    renderEmulator(state.selectedRouter);
    addLog(`Preset "${preset.label}" applied to all interfaces`);
}

// --- Emulator Controls ---

function renderEmulator(router) {
    const container = $('#interface-cards');
    container.innerHTML = '';

    Object.entries(state.interfaceParams).forEach(([iface, params]) => {
        const card = createInterfaceCard(iface, params);
        container.appendChild(card);
    });
}

function createInterfaceCard(iface, params) {
    const card = document.createElement('div');
    card.className = 'iface-card';
    card.dataset.iface = iface;

    const hasRules = Object.values(params).some(v => v > 0);

    card.innerHTML = `
        <div class="iface-header">
            <div class="iface-name">
                <span class="dot ${hasRules ? 'active' : ''}"></span>
                ${iface}
            </div>
            <div class="iface-status">${hasRules ? 'Rules Active' : 'No Rules'}</div>
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

    // Attach slider listeners after inserting into DOM
    setTimeout(() => {
        card.querySelectorAll('input[type="range"]').forEach(input => {
            input.addEventListener('input', (e) => {
                const param = e.target.dataset.param;
                const val = parseFloat(e.target.value);
                state.interfaceParams[iface][param] = val;
                const display = e.target.closest('.slider-group').querySelector('.slider-value');
                display.textContent = formatValue(val, e.target.dataset.unit);
                // Clear preset highlight
                $$('.preset-btn').forEach(b => b.classList.remove('active'));
                // Update status dot
                updateCardStatus(iface);
            });
        });
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
    const hasRules = Object.values(params).some(v => v > 0);
    const card = document.querySelector(`.iface-card[data-iface="${iface}"]`);
    if (!card) return;
    const dot = card.querySelector('.dot');
    const status = card.querySelector('.iface-status');
    dot.className = `dot ${hasRules ? 'active' : ''}`;
    status.textContent = hasRules ? 'Rules Active' : 'No Rules';
}

// --- Apply/Clear ---

async function handleApplyAll() {
    if (!state.selectedRouter) return toast('Select a router first', 'error');

    const btn = $('#btn-apply-all');
    btn.disabled = true;
    btn.textContent = 'Applying...';

    try {
        const result = await API.apply({
            router_id: state.selectedRouter.id,
            interfaces: state.interfaceParams,
        });
        toast('WAN rules applied successfully', 'success');
        addLog(`Rules applied to ${state.selectedRouter.name}`, 'success');
        if (result.script) {
            addLog(`Script: ${result.script}`);
        }
    } catch (err) {
        toast('Failed to apply rules: ' + err.message, 'error');
        addLog(`Error: ${err.message}`, 'error');
    } finally {
        btn.disabled = false;
        btn.textContent = 'Apply All';
    }
}

async function handleClearAll() {
    if (!state.selectedRouter) return toast('Select a router first', 'error');

    const btn = $('#btn-clear-all');
    btn.disabled = true;

    try {
        await API.clear({
            router_id: state.selectedRouter.id,
            interfaces: Object.keys(state.interfaceParams),
        });

        // Reset all params
        Object.keys(state.interfaceParams).forEach(iface => {
            Object.keys(state.interfaceParams[iface]).forEach(k => {
                state.interfaceParams[iface][k] = 0;
            });
        });

        renderEmulator(state.selectedRouter);
        $$('.preset-btn').forEach(b => b.classList.remove('active'));
        toast('All WAN rules cleared', 'success');
        addLog(`Rules cleared on ${state.selectedRouter.name}`, 'success');
    } catch (err) {
        toast('Failed to clear rules: ' + err.message, 'error');
        addLog(`Error: ${err.message}`, 'error');
    } finally {
        btn.disabled = false;
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

    // Keep max 50 entries
    while (container.children.length > 50) {
        container.removeChild(container.lastChild);
    }
}

// --- Toast ---

function toast(msg, type = 'success') {
    const el = document.createElement('div');
    el.className = `toast toast-${type}`;
    el.textContent = msg;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 3000);
}
