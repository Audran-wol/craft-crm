const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const assert = require('node:assert/strict');
const source = fs.readFileSync(process.argv[2] || path.join(__dirname, 'fixtures/legacy-crm.html'), 'utf8');
const script = source.match(/<script>([\s\S]*?)<\/script>/)[1];
function boot() {
  const ids = [...source.matchAll(/id="([^"]+)"/g)].map(m => m[1]);
  const elements = Object.fromEntries(ids.map(id => [id, {value:'', checked:false, textContent:'', innerHTML:'', style:{}}]));
  elements.form.reset = () => { elements.name.value=''; elements.company.value=''; elements.reject.checked=false; };
  const context = vm.createContext({document:{getElementById:id => elements[id]}});
  vm.runInContext(script, context);
  return {elements, run:code => vm.runInContext(code, context)};
}
const evidence = [];
function check(name, fn) { const result=fn(); evidence.push({name,result}); }
check('Combined owner and case-insensitive name filtering', () => {
  const {elements:e}=boot(); e.owner.value='Amina'; e.search.value='CLARA'; e.search.oninput();
  assert.ok(e.rows.innerHTML.includes('Clara Ndom')); assert.equal((e.rows.innerHTML.match(/<tr>/g)||[]).length,1);
  assert.equal(e.count.textContent,'7 matching contacts');
  return {rows:1,shownCount:e.count.textContent};
});
check('Filter on page three retains invalid page; Clear does not reset it', () => {
  const {elements:e}=boot(); e.next.onclick(); e.next.onclick(); e.owner.value='Amina'; e.owner.onchange();
  assert.equal(e.rows.innerHTML,''); assert.equal(e.page.textContent,'Page 3');
  e.clear.onclick(); assert.equal(e.page.textContent,'Page 3');
  return {filteredRows:0,afterClearPage:e.page.textContent};
});
check('Next has no final-page bound', () => {
  const {elements:e}=boot(); for(let i=0;i<20;i++)e.next.onclick();
  assert.equal(e.page.textContent,'Page 21'); assert.equal(e.rows.innerHTML,'');
  return {page:e.page.textContent,rows:0};
});
check('Rejected save clears draft, leaves record unchanged, reports Saved', () => {
  const {elements:e,run}=boot(); run('edit(1)'); e.name.value='Revised Amina'; e.company.value='Draft company'; e.reject.checked=true;
  e.form.onsubmit({preventDefault(){}});
  assert.equal(e.name.value,''); assert.equal(e.company.value,''); assert.equal(e.status.textContent,'Saved');
  assert.equal(run('contacts[0].name'),'Amina Njoya'); assert.equal(e.editor.style.display,'block');
  assert.equal(e.error.textContent,'Save failed. Try again.');
  const failedDraftName=e.name.value;
  run('edit(2)'); assert.equal(e.error.textContent,'Save failed. Try again.');
  return {failedDraftName,status:e.status.textContent,record:run('contacts[0].name'),staleErrorOnNextRecord:e.error.textContent};
});
check('Successful save updates memory/list but a fresh script boot restores fixture', () => {
  const {elements:e,run}=boot(); run('edit(1)'); e.name.value='Revised Amina'; e.form.onsubmit({preventDefault(){}});
  assert.equal(run('contacts[0].name'),'Revised Amina'); assert.ok(e.rows.innerHTML.includes('Revised Amina'));
  assert.equal(boot().run('contacts[0].name'),'Amina Njoya');
  return {inMemory:'Revised Amina',freshBoot:'Amina Njoya'};
});
check('Edited values flow unescaped into HTML sink', () => {
  const {elements:e,run}=boot(); run('edit(1)'); e.name.value='<strong data-probe="audit">probe</strong>';
  e.form.onsubmit({preventDefault(){}}); assert.ok(e.rows.innerHTML.includes('<td><strong data-probe="audit">probe</strong></td>'));
  return {literalMarkupInInnerHTML:true,executionTested:false};
});
console.log(JSON.stringify({method:'Node vm with minimal document stubs; not a browser DOM',checks:evidence},null,2));
