#!/usr/bin/env node
'use strict';
// Node-only: exercise the exact storage module and fixtures embedded in index.html.
// No DOM stub or browser-control dependencies; this cannot verify focus or layout.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const logic = html.split('// STORAGE_LOGIC_START')[1]?.split('// STORAGE_LOGIC_END')[0];
assert.ok(logic, 'embedded storage module markers');
const seedSource = html.slice(html.indexOf('const seed='), html.indexOf('// STORAGE_LOGIC_START'));
const context = vm.createContext({module: {exports: {}}});
vm.runInContext(`function day(offset=0){const date=new Date('2026-10-22T12:00:00Z');date.setUTCDate(date.getUTCDate()+offset);return date.toISOString().slice(0,10)}\n${seedSource}\n// STORAGE_LOGIC_START${logic}\nmodule.exports={createAtelierStorage,seed};`, context);
const {createAtelierStorage, seed} = context.module.exports;
const clone = value => JSON.parse(JSON.stringify(value));
const fixtures = clone(seed);
const key = 'atelier-crm-v1';
const envelope = data => JSON.stringify({schemaVersion: 1, data});
class MemoryStorage {
  constructor(raw = null) { this.values = new Map(raw === null ? [] : [[key, raw]]); this.writes = []; this.rejectGet = false; this.rejectWrite = () => false; }
  getItem(name) { if (this.rejectGet) throw Error('denied-read'); return this.values.has(name) ? this.values.get(name) : null; }
  setItem(name, value) { if (this.rejectWrite(name)) throw Error('denied-write'); this.values.set(name, value); this.writes.push({name, value}); }
}
let passed = 0;
function test(name, fn) { fn(); passed++; console.log('PASS ' + name); }
function open(raw) { const storage = new MemoryStorage(raw); const engine = createAtelierStorage(storage, key, fixtures); return {storage, engine}; }
function assertSame(actual, expected) { assert.equal(JSON.stringify(actual), JSON.stringify(expected)); }

test('first use: no eager write; first mutation writes schemaVersion 1', () => {
  const {storage, engine} = open(null);
  assert.equal(engine.state.status, 'first-use'); assert.equal(engine.state.writable, true);
  assert.equal(storage.writes.length, 0);
  const next = clone(fixtures); next.contacts[0].role = 'Changed';
  assert.equal(engine.commit(next).ok, true);
  assert.equal(JSON.parse(storage.getItem(key)).schemaVersion, 1);
  assertSame(engine.state.data, next);
});
test('versioned valid reload preserves edited records and does not write', () => {
  const data = clone(fixtures); data.contacts[0].role = 'Saved role';
  const raw = envelope(data), {storage, engine} = open(raw);
  assert.equal(engine.state.status, 'valid'); assertSame(engine.state.data, data);
  assert.equal(storage.getItem(key), raw); assert.equal(storage.writes.length, 0);
});
test('legacy reload migrates only after an exact recoverable source copy', () => {
  const data = clone(fixtures); data.contacts[0].role = 'Legacy saved role';
  const raw = JSON.stringify(data, null, 2), {storage, engine} = open(raw);
  assert.equal(engine.state.status, 'migrated'); assertSame(engine.state.data, data);
  assert.equal(storage.getItem(engine.state.backupKey), raw);
  assert.equal(storage.writes[0].name, engine.state.backupKey);
  assertSame(JSON.parse(storage.getItem(key)).data, data);
  const count = storage.writes.length, again = createAtelierStorage(storage, key, fixtures);
  assert.equal(again.state.status, 'valid'); assert.equal(storage.writes.length, count);
});
const invalidCases = [
  ['malformed JSON', '{broken', 'malformed'],
  ['empty saved bytes differ from first use', '', 'malformed'],
  ['JSON null', 'null', 'invalid'],
  ['wrong collection type', (()=>{const d=clone(fixtures);d.contacts={};return envelope(d)})(), 'invalid'],
  ['missing collection', (()=>{const d=clone(fixtures);delete d.activities;return envelope(d)})(), 'invalid'],
  ['duplicate IDs', (()=>{const d=clone(fixtures);d.contacts[1].id=d.contacts[0].id;return envelope(d)})(), 'invalid'],
  ['missing ID', (()=>{const d=clone(fixtures);delete d.contacts[0].id;return envelope(d)})(), 'invalid'],
  ['unsafe ID', (()=>{const d=clone(fixtures);d.activities[0].id='a\"unsafe';return envelope(d)})(), 'invalid'],
  ['broken contact-company relation', (()=>{const d=clone(fixtures);d.contacts[0].company='missing';return envelope(d)})(), 'invalid'],
  ['broken opportunity-contact relation', (()=>{const d=clone(fixtures);d.opportunities[0].contact='missing';return envelope(d)})(), 'invalid'],
  ['missing activity relation', (()=>{const d=clone(fixtures);delete d.activities[0].contact;return envelope(d)})(), 'invalid'],
  ['invalid calendar rollover', (()=>{const d=clone(fixtures);d.activities[0].date='2026-02-30';return envelope(d)})(), 'invalid'],
  ['invalid date shape', (()=>{const d=clone(fixtures);d.activities[0].date='tomorrow';return envelope(d)})(), 'invalid'],
  ['invalid boolean type', (()=>{const d=clone(fixtures);d.activities[0].done='false';return envelope(d)})(), 'invalid'],
  ['invalid status enum', (()=>{const d=clone(fixtures);d.contacts[0].status='unknown';return envelope(d)})(), 'invalid'],
  ['invalid field type', (()=>{const d=clone(fixtures);d.companies[0].name=42;return envelope(d)})(), 'invalid'],
  ['unsupported newer schema', JSON.stringify({schemaVersion:2,data:fixtures}), 'newer'],
  ['invalid schema version type', JSON.stringify({schemaVersion:'1',data:fixtures}), 'invalid'],
];
for (const [label, raw, status] of invalidCases) test(label + ': block writes and preserve original bytes', () => {
  const {storage, engine} = open(raw), prior = clone(engine.state.data);
  assert.equal(engine.state.status, status); assert.equal(engine.state.writable, false);
  assert.equal(engine.state.originalRaw, raw); assert.equal(storage.getItem(key), raw);
  const draft = clone(fixtures); draft.contacts[0].role = 'Unsaved draft'; const draftBefore = JSON.stringify(draft);
  assert.equal(engine.commit(draft).ok, false);
  assert.equal(JSON.stringify(draft), draftBefore); assertSame(engine.state.data, prior);
  assert.equal(storage.getItem(key), raw); assert.equal(storage.writes.length, 0);
});
test('valid empty collections are legitimate and not reseeded', () => {
  const data={companies:[],contacts:[],opportunities:[],activities:[]};
  const {engine,storage}=open(envelope(data));assertSame(engine.state.data,data);assert.equal(storage.writes.length,0);
});
test('calendar boundaries: leap day accepted; invalid leap day rejected', () => {
  const data=clone(fixtures);data.activities[0].date='2024-02-29';assert.equal(open(envelope(data)).engine.state.status,'valid');
  data.activities[0].date='2025-02-29';assert.equal(open(envelope(data)).engine.state.status,'invalid');
});
test('rejected write retains prior committed bytes, data and caller draft', () => {
  const raw=envelope(fixtures),{storage,engine}=open(raw),draft=clone(fixtures);draft.contacts[0].role='Pending change';
  const before=JSON.stringify(draft);storage.rejectWrite=()=>true;
  assert.equal(engine.commit(draft).reason,'rejected');assert.equal(storage.getItem(key),raw);
  assertSame(engine.state.data,fixtures);assert.equal(JSON.stringify(draft),before);
  storage.rejectWrite=()=>false;assert.equal(engine.commit(draft).ok,true);assertSame(engine.state.data,draft);
});
test('invalid mutation rejected before any write', () => {
  const raw=envelope(fixtures),{storage,engine}=open(raw),draft=clone(fixtures);draft.activities[0].contact='missing';
  assert.equal(engine.commit(draft).reason,'invalid-mutation');assert.equal(storage.getItem(key),raw);assert.equal(storage.writes.length,0);
});
test('denied read is distinguished from first use and cannot write', () => {
  const storage=new MemoryStorage(envelope(fixtures));storage.rejectGet=true;
  const engine=createAtelierStorage(storage,key,fixtures);assert.equal(engine.state.status,'unavailable');
  assert.equal(engine.commit(fixtures).reason,'blocked');assert.equal(engine.reset().ok,false);assert.equal(storage.writes.length,0);
});
for(const failedKey of ['backup','main'])test('legacy '+failedKey+' write rejection preserves exact legacy source and valid records',()=>{
  const raw=JSON.stringify(fixtures,null,2),storage=new MemoryStorage(raw);
  storage.rejectWrite=name=>failedKey==='backup'?name!==key:name===key;
  const engine=createAtelierStorage(storage,key,fixtures);
  assert.equal(engine.state.status,'migration-failed');assert.equal(engine.state.writable,false);
  assertSame(engine.state.data,fixtures);assert.equal(storage.getItem(key),raw);assert.equal(engine.commit(fixtures).ok,false);
  if(failedKey==='main')assert.equal(storage.getItem(engine.state.backupKey),raw);
});
test('explicit reset copies unreadable original before replacement; later writes enabled',()=>{
  const raw=' { bad saved bytes\n', {storage,engine}=open(raw);assert.equal(storage.writes.length,0);
  const result=engine.reset();assert.equal(result.ok,true);assert.equal(storage.getItem(result.backupKey),raw);
  assert.equal(storage.writes[0].name,result.backupKey);assert.equal(engine.state.originalRaw,raw);
  assertSame(JSON.parse(storage.getItem(key)).data,fixtures);assert.equal(engine.commit(fixtures).ok,true);
});
test('recovery never overwrites an older backup with different bytes',()=>{
  const raw='{bad', {storage,engine}=open(raw);storage.values.set(key+':recovery-source','older source');
  const result=engine.reset();assert.equal(result.ok,true);assert.equal(storage.getItem(key+':recovery-source'),'older source');
  assert.equal(storage.getItem(result.backupKey),raw);
});
for(const failedKey of ['backup','main'])test('rejected recovery '+failedKey+' write preserves original saved bytes',()=>{
  const raw='{bad', {storage,engine}=open(raw);storage.rejectWrite=name=>failedKey==='backup'?name!==key:name===key;
  assert.equal(engine.reset().ok,false);assert.equal(storage.getItem(key),raw);assert.equal(engine.state.writable,false);
  if(failedKey==='main')assert.equal(storage.getItem(key+':recovery-source'),raw);
});
test('a changed saved value blocks mutation instead of overwriting unseen bytes',()=>{
  const {storage,engine}=open(envelope(fixtures));storage.values.set(key,'newer external bytes');
  assert.equal(engine.commit(fixtures).reason,'changed');assert.equal(engine.state.writable,false);
  assert.equal(storage.getItem(key),'newer external bytes');assert.equal(engine.state.originalRaw,'newer external bytes');
});
console.log(`\n${passed} storage logic checks passed. Test clock: 2026-10-22 UTC. Focus, rendering and browser storage behavior are not tested.`);
