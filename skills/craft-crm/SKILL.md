---
name: craft-crm
description: Plan, build, redesign, or audit CRM interfaces and workflows, including records, filters, forms, activities, and domain-specific pipelines. Use for new CRMs or improvements to an existing relationship-management product; preserve its stack and working behavior.
---

# CRM Craft

Turn a business brief into a coherent working CRM. Optimize for frequent decisions and actions, then refine visual composition. Treat bundled references as evidence and reusable decisions, not a request to reproduce a brand or install every library.

This is a **general CRM skill**. Records, relationships, activities, permissions, views, and reusable UI form the common foundation. Sales pipelines, invoices, support queues, and other modules are optional domain adaptations. Do not let a reference demo's business domain dictate the user's product.

## Start efficiently

1. Classify the request as **plan**, **build**, **revamp**, **audit**, or **polish**. Planning produces implementation contracts, not an application; audit produces findings, not source changes. Otherwise default to build when no existing product exists.
2. Identify operator, main object, top three tasks, required screens, existing stack, brand constraints, data volume, and prototype versus integrated application. Read supplied repository instructions and existing routes/components first. Use available context; ask at most three material questions. If answers are optional, state assumptions and proceed.
3. For a revamp, preserve routes, schemas, permission rules, integrations, analytics, and existing behavior unless changing them is requested. Follow [revamp.md](references/revamp.md).
4. Read [foundations.md](references/foundations.md) for visual work, applicable [component specs](references/component-specs.md), and only relevant sections of [patterns.md](references/patterns.md). Read [implementation.md](references/implementation.md) before implementing persistence or defining integrated data contracts. Use [domain adapters](references/domain-adapters.md) for an unfamiliar CRM brief. Do not load the entire source catalog for routine builds.
5. For builds or visual redesigns, select an archetype from [directions.md](references/directions.md). Reuse the established product language where one exists. For audits, assess the existing composition against its tasks; choosing a replacement design is optional unless requested.

For job discovery, lead databases or other filter-heavy search pages, read [search-results.md](references/search-results.md). When repairing pickers/pop-outs, read [popovers.md](references/popovers.md); its sibling-popup and focus checks apply without expanding the business scope.

## Choose a visual direction without stalling

- If the user says “just build,” choose the best-fitting direction and build.
- If the user asks for options or direction materially affects acceptance, show up to three **comparable views of the same screen, data, and viewport**, with a recommendation and tradeoff. Use the bundled [direction board](assets/direction-board.svg) as a schematic starting point; create brief-specific previews in code when tools permit. The board is an original illustration, not a screenshot of a cited product.
- Vary composition or density, not merely accent colors. Do not use an image generator for exact UI labels, data, or interactions.
- If visual rendering is unavailable, give a compact comparison and proceed with the recommended default; do not claim screenshots were inspected.
- Read [anti-slop.md](references/anti-slop.md) before accepting a composition. Familiar controls and common fonts are allowed. Unjustified sameness is the problem.

## Write the small build contract

For planning and implementation work, use the contract below. An audit-only request needs a scoped findings report with evidence and acceptance checks; it does not need a separate build contract or new design direction.

Fill relevant fields in [build-contract.md](assets/build-contract.md); keep it proportional to scope:
- Operator, domain, tasks, objects, routes, real or synthetic data.
- Chosen direction, canvas/surface distinction, density, typography, icon family.
- One primary action per task context; page / view / row action scopes.
- Table columns, default view, filter semantics, pagination and selection scope.
- Main success flow plus loading, empty, filtered-empty, error, permission, and save-failure states.
- Persistence owner and recovery boundary, test records/clock, and observable expected outcomes for the main checks.
- Source IDs supporting important choices, deliberate exceptions, and acceptance checks.

For a new CRM with no scope, default to records list → record details → create/edit → next activity. Add a pipeline only for staged work. Add a dashboard only when its metrics answer a recurring question. Do not invent an ERP-sized navigation tree.

## Implement in connected slices

1. Establish semantic tokens and shell; use [tokens.css](assets/tokens.css) only as a starting point. Adapt existing tokens instead of adding a second system.
2. Build a realistic records list with meaningful fields and working search/filter/sort.
3. Connect the list to a record view and create/edit flow.
4. Add the domain's distinguishing workflow: pipeline transition, invoice follow-up, support triage, or account task.
5. Complete adverse states, responsiveness, keyboard behavior, and persistence.
6. Refine alignment, hierarchy, icon weight, row rhythm, copy, and purposeful motion.

Use [implementation.md](references/implementation.md) for stack choice, component contracts, API boundaries, data ownership, and license checks. Check installed versions before using remembered APIs. Library accessibility claims do not prove that an assembled screen is accessible.

For a prototype, implement working local interactions and disclose persistence limits. For an integrated app, use real data contracts. Never call a static composition a fully functional CRM. Do not silently perform real outreach, payments, imports, destructive migrations, or permission changes while testing.

## Required behavior and composition

- Separate workspace navigation, page identity, saved views, and record controls. Keep search attached to its scope.
- Use one deliberate surface hierarchy. A light gray canvas with white work surfaces is one option; flat tables and dark products are also valid when intentional.
- Align amounts and totals; show units, currency, date scope, and missing-value meaning.
- Keep repeated geometry consistent. Avoid nested cards for plain labels, metrics without decisions, decorative gradients behind dense data, and competing primary buttons.
- Name icon-only controls accessibly; keep visible labels for ambiguous or critical actions. Use one main icon family, with brand icons as an explicit exception.
- For newly designed branded CRM screens, use a coherent select/combobox component, including its open popup, rather than leaving browser-default dropdowns as the finished design. Reuse established project primitives. Follow the custom-dropdown contract in [component-specs.md](references/component-specs.md); preserve an existing native control when the user or platform context calls for it.
- Use native table semantics unless the keyboard model requires a composite grid. A visual grid is not an ARIA grid by default.
- Keep filters, counts, aggregates, exports, and pagination consistent. Declare current-page versus all-matching selection.
- Prefer a context-preserving drawer for quick inspection and a full record route for long work. Manage focus according to modal or non-modal behavior.
- Provide keyboard and single-pointer alternatives to dragging.
- Handle text overflow, touch targets, localization, slow networks, denied permissions, and failed saves.
- Keep focus stable during typing and return it to a logical control after rerenders, filter changes, locale switches, and dialog transitions. Do not rebuild a live form on every keystroke.
- Treat local saved data as untrusted input: validate its shape/version before rendering and preserve unreadable data rather than overwriting it with fixtures. Follow the local-persistence contract in [implementation.md](references/implementation.md).
- Fix overflow at its source; do not hide broken layouts by disabling scroll or zoom.
- Give AI suggestions provenance and review states; never imply certainty or successful saves without evidence.

## Verify the result

Read [quality-gates.md](references/quality-gates.md). Run relevant project checks and exercise the primary workflow with realistic data. Inspect rendered desktop, constrained-desktop, and mobile screens where supported. Include keyboard-only and adverse-state checks. In audit-only work, distinguish observed defects from inferred risks.

Use [audit-template.json](assets/audit-template.json) and optionally:
```bash
python3 scripts/score_audit.py path/to/completed-audit.json --format text
```
The script evaluates submitted checklist evidence; it does not inspect UI or certify accessibility. Unknown checks are not passes. A high score cannot override a failed critical gate.
Exit 1 means a valid review has findings or unverified checks; it is not a script crash. Exit 2 means invalid input. Omit `--format text` for JSON automation.

Stop optional testing when material risks are resolved. Report what changed, why, what was verified, viewports/states, limitations, and how to run/use the result. Do not promise pixel perfection, WCAG conformance, production readiness, or a fixed speed improvement from the skill alone.

## Reference routing

| Need | Read |
| --- | --- |
| Layout choice and optional previews | [directions.md](references/directions.md) |
| Tokens, dimensions, type, icons | [foundations.md](references/foundations.md) |
| Component anatomy, sizing, states and responsive behavior | [component-specs.md](references/component-specs.md) |
| General data model and domain-specific CRM adaptation | [domain-adapters.md](references/domain-adapters.md) |
| Tables, filters, records, pipelines, dashboards, invoices, support, imports | [patterns.md](references/patterns.md) |
| Generic design and companion-skill conflicts | [anti-slop.md](references/anti-slop.md) |
| Existing CRM audit and staged changes | [revamp.md](references/revamp.md) |
| Jobs, leads and filter-heavy search results | [search-results.md](references/search-results.md) |
| Pop-out ownership, dismissal, focus and clipping | [popovers.md](references/popovers.md) |
| Libraries and functional contracts | [implementation.md](references/implementation.md) |
| Verification and evidence scoring | [quality-gates.md](references/quality-gates.md) |
| Worked briefs and prompts | [examples.md](references/examples.md) |
| Provenance, limitations, refresh | [research-method.md](references/research-method.md) |
| Annotated evidence | [sources.md](references/sources.md) |
| Machine-readable records | [sources.json](references/sources.json) |
| Bundle integrity check | [validate_bundle.py](scripts/validate_bundle.py) |

Use this original synthesis without requiring companion skills. If another design skill is installed, read anti-slop.md's conflict rules. Follow explicit user direction and product constraints.
