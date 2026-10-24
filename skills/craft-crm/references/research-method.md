# Research method and maintenance

## Scope and evidence

Reviewed 52 distinct resources on 22 October 2026 across CRM products, creator demos, repositories, design systems, accessibility, interaction writing, design skills and performance guidance. Grouping the separate SakaniUI source file with its repository yields 51 resources. Several pages share publishers; the count is not a claim of independent corroboration.

sources.json is the canonical annotated registry. Each record has URL, access/evidence type, observation, derived application, limitation and review date. sources.md is its readable counterpart.
- Official standards and APG anchor accessibility rules.
- Product documentation anchors observable CRM concepts.
- Repository documentation identifies patterns and integration candidates.
- Creator work informs composition and interaction details.
- This skill's sizes, palette, architecture defaults and scoring threshold are original heuristics.

The corpus supports informed construction; it is not exhaustive, a ranking of “best CRMs,” or proof that each referenced app is production-ready.

## What was directly inspected

The customer-filter demo was visually inspected and its filter entry menu opened. The follow-on numeric-filter interaction stalled; no claim is made that it was tested fully.
The invoice demo was visually inspected. Its status filter changed the displayed scope to 3 overdue invoices and EUR 9,700. Other actions, persistence and full accessibility were not tested.
The customer-drawer demo was retrieved as page text, not visually audited.
SakaniUI README, agent guide, license, package manifest and CRM block source were inspected via GitHub. Its React 19 requirement and explicit example-block boundary shaped the implementation guidance.
Other repositories were read primarily at README level; no whole-repository security audit or installation was performed.

## Discovery leads, excluded from the reviewed count

These indexed creator posts helped find examples. They are discovery records, not substitutes for a live audit:
- Louis Nguyen Studio, customer drawer: https://x.com/louisnstudio/status/2091575122675277833
- Louis Nguyen Studio, reorder/resize: https://x.com/louisnstudio/status/2092547072394412502
- Louis Nguyen Studio, general settings: https://x.com/louisnstudio/status/2085355259007017227
- Louis Nguyen Studio, customer table: https://x.com/louisnstudio/status/2090529285203444198
- Marcel Kargul, sales CRM: https://x.com/marcelkargul/status/2099447410804035806
- Bharat Kara, CRM demo: https://x.com/KaraBharat/status/1914628130393710950

The X search timeline https://x.com/search?q=crm&src=typed_query was unavailable through web retrieval. This research does not claim to have scrolled it or collected all posts.
The Marcel sales demo https://sales-crm-kargulstudio.vercel.app/ was discovered but not inspected successfully.
The KaraBharat live demo https://shadcn-crm-dashboard.vercel.app/ was not retrieved successfully; its repository was read.
Atlassian's dynamic-table page returned no usable content; Spectrum table and an attempted Salesforce data-table URL were not usable. These were not counted.
A guessed bazza/ui repository path returned 404 and was excluded. No claims rely on it.

## Turn a future resource into a rule

1. Identify canonical author/source and exact page or file.
2. Open the resource; record whether evidence is snippet, document, code, screenshot, interaction, or measured test.
3. Extract one concrete pattern: anatomy, task, inputs, states, failure behavior.
4. Record when it applies and when it should not.
5. Cross-check accessibility and functional claims against authoritative sources or actual tests.
6. Add a short paraphrase and link; do not copy whole articles, external skill files, or unlicensed assets.
7. Map it to an existing pattern or explain why a new one is needed.
8. Keep draft/discovery entries separate; do not inflate the verified count.
9. Reconcile contradictory guidance explicitly.
10. Validate the bundle and forward-test a relevant brief before saving changes.

## Refresh

Re-check library APIs/licenses at implementation time and live links when selected as a reference. Refresh the catalog periodically when maintaining the skill; do not claim an automatic scheduled refresh exists.
Retain review dates and mark moved/unavailable sources. Prioritize changed APIs, broken links and conflicting evidence rather than repeating the whole research for every CRM build.
Keep successful user-specific product decisions in the project's own design contract; do not silently overwrite this generic skill after each task.
