'use strict';
// Real Chromium pointer regression. No browser download is performed.
// Run: node visualization/cosmos/tests/test_browser.js
// Optional: CHROMIUM_PATH=/path/to/chrome; COSMOS_SCREENSHOTS=/path/to/output
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

function playwright() {
  try { return require('playwright'); } catch (error) {
    if (!process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES) throw error;
    return require(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES, 'playwright'));
  }
}

async function frames(page, count) {
  const target = await page.evaluate(n => cosmos.state.frames + n, count);
  await page.waitForFunction(n => cosmos.state.frames >= n, target, { timeout: 45000 });
}

async function snapshot(page, systemId) {
  return page.evaluate(id => {
    const center = cosmos.systems.find(s => s.id === id);
    const groupById = new Map(cosmos.graph.nodes.map(n => [n.id, CosmosEngine.group(n)]));
    const members = cosmos.positions.filter(n => groupById.get(n.id) === id);
    const glyph = document.querySelector(`[data-system-glyph="${id}"]`);
    const p = new DOMPoint(0, 0).matrixTransform(glyph.getScreenCTM());
    const transform = d3.zoomTransform(document.querySelector('#scene'));
    const routes = Array.from(document.querySelectorAll('#routes path.route:not(.hit)'), el => {
      const values = el.getAttribute('d').match(/[-+]?(?:\d*\.)?\d+(?:e[-+]?\d+)?/gi).map(Number);
      return { start: values.slice(0, 2), end: values.slice(-2) };
    });
    return { center, members, glyph: { x: p.x, y: p.y }, k: transform.k,
      time: cosmos.state.time, anchors: cosmos.anchors, routes };
  }, systemId);
}

function close(actual, expected, tolerance, description) {
  assert.ok(Math.abs(actual - expected) <= tolerance,
    `${description}: expected ${expected}, received ${actual} (tolerance ${tolerance})`);
}

async function validateOrbitsAndRoutes(page) {
  const errors = await page.evaluate(() => {
    const m = CosmosEngine.make(cosmos.graph, { anchors: cosmos.anchors });
    for (const position of cosmos.positions) Object.assign(m.byId.get(position.id), position);
    const errors = [];
    for (const n of m.nodes.filter(n => n.orbit)) {
      const parent = m.byId.get(n.orbit.parent);
      const distance = ((n.x - parent.x) / n.orbit.radius) ** 2 +
        ((n.y - parent.y) / (n.orbit.radius * n.orbit.tilt)) ** 2;
      if (Math.abs(distance - 1) > 1e-6) errors.push(`${n.id} left its parent's orbital track`);
    }
    const edge = m.edges.find(e => e.id === 'E02');
    const junction = CosmosEngine.junction(edge, m);
    const paths = Array.from(document.querySelectorAll('[data-edge="E02"] path.route:not(.hit)'));
    if (paths.length !== edge.inputs.length + 1) errors.push('E02 lost a conjunctive branch');
    for (const [index, element] of paths.entries()) {
      const values = element.getAttribute('d').match(/[-+]?(?:\d*\.)?\d+(?:e[-+]?\d+)?/gi).map(Number);
      const start = { x: values[0], y: values[1] };
      const end = { x: values.at(-2), y: values.at(-1) };
      const input = index < edge.inputs.length;
      const body = m.byId.get(input ? edge.inputs[index] : edge.output);
      const endpoint = input ? start : end;
      const joint = input ? end : start;
      if (Math.hypot(joint.x - junction.x, joint.y - junction.y) > 1e-6)
        errors.push(`E02 branch ${index} does not reach its current junction`);
      const radius = CosmosVisuals.visualBounds(body, CosmosEngine.orbitIds.indexOf(body.id)) + 5;
      if (Math.abs(Math.hypot(endpoint.x - body.x, endpoint.y - body.y) - radius) > 1e-6)
        errors.push(`E02 branch ${index} endpoint detached from ${body.id}`);
    }
    return errors;
  });
  assert.deepEqual(errors, []);
}

async function dragCase(browser, systemId, running) {
  const page = await browser.newPage({ viewport: { width: 1600, height: 1100 }, reducedMotion: 'reduce' });
  const pageErrors = [];
  page.on('pageerror', error => pageErrors.push(error.message));
  const name = `${systemId}-${running ? 'running' : 'paused'}`;
  try {
    await page.goto(pathToFileURL(path.join(__dirname, '../index.html')).href);
    await page.waitForFunction(() => window.cosmos && cosmos.state.frames > 2);
    await page.evaluate(() => { cosmos.pause(); cosmos.overview(); cosmos.selectEdge('E02'); });
    await frames(page, 2);
    if (running) await page.evaluate(() => cosmos.resume());
    const initial = await snapshot(page, systemId);
    assert.ok(initial.k < .35, 'overview must expose the system drag handle');
    const down = { x: initial.glyph.x + 14, y: initial.glyph.y - 9 };
    // Verify the actual hit owner before exercising mouse input.
    const owner = await page.evaluate(p => document.elementFromPoint(p.x, p.y)
      ?.closest('[data-system-glyph]')?.getAttribute('data-system-glyph'), down);
    assert.equal(owner, systemId, 'pointer must hit the requested system glyph');
    await page.mouse.move(down.x, down.y);
    await page.mouse.down();
    const before = await snapshot(page, systemId);
    const delta = { x: 95, y: 50 };
    await page.mouse.move(down.x + delta.x, down.y + delta.y, { steps: 12 });
    await frames(page, 12); // Hold still while both simulations get a chance to tick.
    const held = await snapshot(page, systemId);
    close(held.glyph.x, before.glyph.x + delta.x, .8, `${name}: glyph follows pointer x`);
    close(held.glyph.y, before.glyph.y + delta.y, .8, `${name}: glyph follows pointer y`);
    const oldMembers = new Map(before.members.map(n => [n.id, n]));
    for (const n of held.members) {
      if (running && n.parent) continue; // Live orbital phase is intentionally allowed to advance.
      const old = oldMembers.get(n.id);
      close(n.x - held.center.x, old.x - before.center.x, 1e-6, `${name}/${n.id}: held relative x`);
      close(n.y - held.center.y, old.y - before.center.y, 1e-6, `${name}/${n.id}: held relative y`);
    }
    if (!running && systemId === 'solar') {
      for (let i = 0; i < held.routes.length; i++) for (const endpoint of ['start', 'end']) {
        close(held.routes[i][endpoint][0] - before.routes[i][endpoint][0], delta.x / before.k,
          1e-6, `${name}: route ${i} ${endpoint} x translates`);
        close(held.routes[i][endpoint][1] - before.routes[i][endpoint][1], delta.y / before.k,
          1e-6, `${name}: route ${i} ${endpoint} y translates`);
      }
    }
    await validateOrbitsAndRoutes(page);
    await page.mouse.up();
    // Also catches a paused drag whose stale anchors only become apparent on resume.
    await page.evaluate(() => cosmos.resume());
    await frames(page, 120);
    await page.evaluate(() => cosmos.pause());
    const released = await snapshot(page, systemId);
    for (const n of released.members.filter(n => !n.parent)) {
      const old = oldMembers.get(n.id);
      const error = Math.hypot(n.x - released.center.x - (old.x - before.center.x),
        n.y - released.center.y - (old.y - before.center.y));
      assert.ok(error < 100, `${name}/${n.id}: member drifted ${error.toFixed(2)} world units after release`);
    }
    assert.deepEqual(released.anchors, before.anchors, 'drag must preserve canonical anchors');
    assert.ok(released.time > held.time, 'resume must advance the orbital clock');
    await validateOrbitsAndRoutes(page);
    assert.deepEqual(pageErrors, [], 'page errors');
    if (process.env.COSMOS_SCREENSHOTS) {
      fs.mkdirSync(process.env.COSMOS_SCREENSHOTS, { recursive: true });
      await page.screenshot({ path: path.join(process.env.COSMOS_SCREENSHOTS, `drag-${name}.png`) });
    }
    console.log(`PASS real SVG pointer drag ${name}, hold, release + 120 frames, orbits and endpoints`);
  } finally { await page.close(); }
}

async function detailHitCase(browser) {
  const page = await browser.newPage({ viewport: { width: 1600, height: 1100 }, reducedMotion: 'reduce' });
  try {
    await page.goto(pathToFileURL(path.join(__dirname, '../index.html')).href);
    await page.waitForFunction(() => window.cosmos && cosmos.state.frames > 2);
    await page.evaluate(() => { cosmos.pause(); cosmos.solar(); });
    await frames(page, 2);
    const state = await page.evaluate(() => {
      const glyph = document.querySelector('[data-system-glyph="solar"]');
      const p = new DOMPoint(0, 0).matrixTransform(glyph.getScreenCTM());
      const hit = document.elementFromPoint(p.x, p.y);
      return { k: d3.zoomTransform(document.querySelector('#scene')).k,
        glyphOwner: hit?.closest('[data-system-glyph]')?.getAttribute('data-system-glyph'),
        nodeOwner: hit?.closest('[data-id]')?.getAttribute('data-id') };
    });
    assert.ok(state.k > .42, 'detail camera must completely hide overview glyph');
    assert.equal(state.glyphOwner, undefined, 'hidden glyph must not intercept detail input');
    assert.equal(state.nodeOwner, 'R02', 'detail sun must own its visible center');
    console.log('PASS hidden overview glyph does not intercept detail input');
  } finally { await page.close(); }
}

(async () => {
  // Some restricted runtimes have no /tmp. Use a removable task-local temp directory.
  let temporary;
  if (!fs.existsSync(os.tmpdir())) {
    temporary = fs.mkdtempSync(path.join(process.cwd(), '.cosmos-browser-tmp-'));
    process.env.TMPDIR = temporary;
  }
  let browser;
  try {
    const { chromium } = playwright();
    const executablePath = process.env.CHROMIUM_PATH;
    if (executablePath) assert.ok(fs.existsSync(executablePath), `CHROMIUM_PATH does not exist: ${executablePath}`);
    browser = await chromium.launch({ headless: true, ...(executablePath ? { executablePath } : {}) });
    console.log(`Chromium ${browser.version()}`);
    let failures = 0;
    for (const systemId of ['structure', 'solar']) for (const running of [false, true]) {
      try { await dragCase(browser, systemId, running); }
      catch (error) { failures++; console.error(`FAIL ${systemId}-${running ? 'running' : 'paused'}: ${error.stack}`); }
    }
    try { await detailHitCase(browser); }
    catch (error) { failures++; console.error(`FAIL detail hit ownership: ${error.stack}`); }
    if (failures) throw Error(`${failures} browser regression case(s) failed`);
    console.log('5 browser regression cases passed. This does not certify touch input or Safari.');
  } finally {
    if (browser) await browser.close();
    if (temporary) fs.rmSync(temporary, { recursive: true, force: true });
  }
})().catch(error => { console.error(error.stack || error); process.exitCode = 1; });
