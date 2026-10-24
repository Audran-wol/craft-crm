# Annotated research corpus

52 distinct reviewed resources; 51 if the separate SakaniUI implementation file is grouped with its repository. These are not 52 independent products or full audits. Evidence depth is explicit. Review date: 22 October 2026.

Contents: [creator demos and code](#creator-demos-and-code) · [systems and accessibility](#systems-and-accessibility) · [products and design skills](#products-and-design-skills) · [craft and implementation](#craft-and-implementation).

Read only relevant entries. Observations describe source content; applications are this skill's synthesis. Runtime quality is unverified unless an interaction is specified. Public availability is not a reuse license. Full articles, external skills, and third-party screenshots are not bundled.

## Creator demos and code

### S01 · SakaniUI

[Source](https://github.com/samzydd/Sakaniui) · repository · GitHub README, AGENTS, LICENSE and package manifest read.

**Observed:** Semantic token layers, component contracts and deliberate block composition are documented. **Apply:** Use real component contracts and one token vocabulary. **Limit:** React 19 peer requirement observed; broad accessibility claims not independently certified. MIT file read; linked asset rights need separate checks.

### S02 · Louis CRM filter demo

[Source](https://louis-crm-filter.vercel.app/) · live-demo · Browser screenshot and filter-entry interaction.

**Observed:** Customer table has compact navigation, a scoped toolbar, labeled columns and a property-selection filter menu. **Apply:** Borrow table-first hierarchy and filter entry composition. **Limit:** Numeric filter continuation timed out; persistence, keyboard behavior and backend not verified. No reuse license checked.

### S03 · Louis unpaid invoice demo

[Source](https://louis-unpaid-invoice.vercel.app/) · live-demo · Browser screenshot and status-filter interaction.

**Observed:** List includes due date, ID, status, description, client and amount; Overdue reduced results to 3 and total to EUR 9700. **Apply:** Keep count, monetary total and filtered records synchronized. **Limit:** Other invoice actions and persistence unverified; demo labels do not define accounting rules. No code license checked.

### S04 · Atomic CRM

[Source](https://github.com/marmelab/atomic-crm) · repository · README read.

**Observed:** Documents contacts, tasks, notes, deals, activity history, import/export and customization. **Apply:** Use connected record/activity workflows as the baseline feature model. **Limit:** Not installed or runtime-tested; confirm current license and architecture before reuse.

### S05 · Twenty

[Source](https://github.com/twentyhq/twenty) · repository · README read.

**Observed:** Describes a customizable CRM with objects, fields and views defined for extension. **Apply:** Separate data model from view presentation. **Limit:** Not installed; architectural inspiration, not a drop-in dependency recommendation.

### S06 · Frappe CRM

[Source](https://github.com/frappe/crm) · repository · README read.

**Observed:** Documents an all-in-one lead/deal page, kanban and customized filtered views. **Apply:** Keep relevant work and history connected on records. **Limit:** Runtime and accessibility not audited; stack and license must be reviewed before copying.

### S07 · tablecn

[Source](https://github.com/sadmann7/tablecn) · repository · README read.

**Observed:** Lists server queries, configurable columns, advanced filters, selection actions and virtualization. **Apply:** Use as a targeted table interaction reference. **Limit:** Features documented by author, not executed here; version compatibility still required.

### S08 · OpenStatus data-table-filters

[Source](https://github.com/openstatusHQ/data-table-filters) · repository · README read.

**Observed:** Documents schema-driven facets, selection controls, state adapters and server-backed pagination. **Apply:** Align schema, controls and query state. **Limit:** Observability use differs from CRM; production and CI statements are author claims.

### S09 · shadcn-admin

[Source](https://github.com/satnaing/shadcn-admin) · repository · README read.

**Observed:** Documents shared sidebar, global search, themes and specific RTL component modifications. **Apply:** Reuse shell patterns and preserve existing component customizations. **Limit:** README explicitly distinguishes this from a starter; auth is partial.

### S10 · Ocean DataView

[Source](https://github.com/jingerpie/ocean-dataview) · repository · README read.

**Observed:** Maps one property schema to table, list, gallery and board with query state. **Apply:** Keep views of the same records consistent. **Limit:** Not runtime-tested; verify version, maturity and license.

### S11 · Midday

[Source](https://github.com/midday-ai/midday) · repository · README read.

**Observed:** Combines financial workflow modules and exports in one business product. **Apply:** Study financial context and related tasks. **Limit:** README declares non-commercial/commercial terms; do not assume unrestricted reuse or infer present feature availability from stale sections.

### S12 · KaraBharat CRM dashboard

[Source](https://github.com/KaraBharat/shadcn-crm-dashboard) · repository · README read.

**Observed:** Documents customer, invoice, lead and analytics UI with modular page structure. **Apply:** Study shared shell and module composition. **Limit:** UI source is not proof of production backend, responsiveness or accessibility.

## Systems and accessibility

### S13 · Carbon data table

[Source](https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines) · design-system · Official documentation read.

**Observed:** Defines toolbar, headers, rows, optional pagination, density variants and consistent sizing. **Apply:** Make table geometry and action placement deliberate. **Limit:** Carbon-specific choices are not mandatory for every CRM.

### S14 · Carbon filtering

[Source](https://www.carbondesignsystem.com/building-blocks/core/patterns/filtering) · design-system · Official documentation read.

**Observed:** Distinguishes instant from batch filtering and requires visible applied-filter indicators/reset. **Apply:** Choose apply behavior from task/query cost. **Limit:** Its advice on multi-category menus needs interpretation for richer CRM builders.

### S15 · shadcn data table

[Source](https://ui.shadcn.com/docs/components/base/data-table) · implementation · Official documentation read.

**Observed:** A composition guide combines a table with explicit behaviors rather than one universal data-table component. **Apply:** Assemble only required features and verify current API. **Limit:** Reviewed guide uses TanStack v9; older projects may use v8.

### S16 · shadcn sidebar

[Source](https://ui.shadcn.com/docs/components/base/sidebar) · implementation · Official documentation read.

**Observed:** Separates provider, header, content, groups, footer and collapse variants. **Apply:** Centralize shell state and navigation anatomy. **Limit:** Use current installed primitive family and preserve local modifications.

### S17 · Radix Dialog

[Source](https://www.radix-ui.com/primitives/docs/components/dialog) · implementation · Official documentation read.

**Observed:** Documents modal/non-modal behavior, title/description, focus management and Escape. **Apply:** Use an established overlay primitive with correct mode. **Limit:** Application composition still needs verification.

### S18 · React Aria Table

[Source](https://react-aria.adobe.com/Table) · implementation · Official documentation read.

**Observed:** Documents table navigation, optional selection/sorting and cell focus configuration. **Apply:** Choose an explicit accessible interaction model. **Limit:** Do not mix keyboard models casually; not a runtime audit.

### S19 · Tabler Icons

[Source](https://tabler.io/icons) · icons · Official site read.

**Observed:** Documents consistent SVG grid/stroke with configurable appearance. **Apply:** Use coherent optical size and weight. **Limit:** Do not treat icon counts as stable or assume every identifier exists in installed version.

### S20 · Lucide stroke width

[Source](https://lucide.dev/guide/react/basics/stroke-width) · icons · Official documentation read.

**Observed:** Explains stroke customization and size-relative versus non-scaling strokes. **Apply:** Keep small and large icon weights consistent. **Limit:** Current and older versions use different non-scaling prop names; inspect installed API.

### S21 · WAI-ARIA grid pattern

[Source](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) · accessibility · Official APG read.

**Observed:** Composite grids require managed internal focus and differ from ordinary table tab order. **Apply:** Use native table unless composite interactions justify a grid. **Limit:** APG is implementation guidance; a role alone supplies no keyboard behavior.

### S22 · WCAG target size minimum

[Source](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) · accessibility · Official understanding document read.

**Observed:** AA criterion sets a 24 CSS-pixel target minimum with specified exceptions. **Apply:** Evaluate hit area and spacing, not just visible glyph. **Limit:** 44-pixel touch preference in this skill is a comfort default, not this AA threshold.

### S23 · WCAG focus not obscured

[Source](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) · accessibility · Official understanding document read.

**Observed:** Focused controls must not be entirely hidden by author-created content. **Apply:** Check sticky toolbars, menus and inspector focus. **Limit:** Aim for full visibility; do not misstate the criterion's minimum.

### S24 · WCAG text contrast

[Source](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) · accessibility · Official understanding document read.

**Observed:** Sets normal/large text contrast requirements and exceptions. **Apply:** Measure actual text/background pairs. **Limit:** A palette alone cannot certify all rendered states.

### S25 · WCAG dragging movements

[Source](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html) · accessibility · Official understanding document read.

**Observed:** Dragging functionality needs a single-pointer non-drag alternative unless excepted. **Apply:** Add move-to-stage actions besides board dragging. **Limit:** Keyboard support alone does not satisfy the single-pointer alternative.

### S26 · WAI-ARIA modal dialog

[Source](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) · accessibility · Official APG read.

**Observed:** Describes inert background, initial focus, contained tab sequence and dialog semantics. **Apply:** Make modal drawers function as dialogs. **Limit:** Do not impose a modal trap on a non-modal inspector.

### S27 · WAI-ARIA combobox

[Source](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) · accessibility · Official APG read.

**Observed:** Distinguishes editable/select-only controls and associated popup behaviors. **Apply:** Build searchable owners/relations with an established pattern. **Limit:** Not every dropdown is a combobox.

### S28 · NN/G complex applications

[Source](https://www.nngroup.com/articles/complex-application-design/) · ux-research · Article read.

**Observed:** Recommends retaining capability while reducing clutter and easing transitions to secondary information. **Apply:** Use progressive disclosure without deleting important workflows. **Limit:** General guidance needs task-specific validation.

### S29 · NN/G icon usability

[Source](https://www.nngroup.com/articles/icon-usability/) · ux-research · Article read.

**Observed:** Explains that icon recognition depends on experience and ambiguous meanings need labels. **Apply:** Label critical and unfamiliar actions visibly. **Limit:** A tooltip is not always a substitute for a visible label.

### S30 · GOV.UK error summary

[Source](https://design-system.service.gov.uk/components/error-summary/) · design-system · Official documentation read.

**Observed:** Pairs summary-level error navigation with field-level messages. **Apply:** Make longer forms recoverable without re-entry. **Limit:** Adapt visual styling to the product; do not copy public-service branding.

### S31 · PatternFly empty states

[Source](https://www.patternfly.org/components/empty-state/design-guidelines/) · design-system · Official documentation read.

**Observed:** Separates no results, setup, no access and backend failure contexts. **Apply:** Give state-specific recovery rather than a generic empty card. **Limit:** Do not equate denied access or failure with no data.

## Products and design skills

### S32 · Attio filter and sort views

[Source](https://attio.com/help/reference/managing-your-data/views/filter-and-sort-views) · crm-product · Official help article read.

**Observed:** Documents property/condition/value filters, groups, and saved versus temporary shared-view changes. **Apply:** Make filter logic and save scope explicit. **Limit:** Attio-specific persistence rules need not be copied unchanged.

### S33 · Attio data model

[Source](https://attio.com/help/reference/attio-101/attios-data-model/define-your-data-model-objects-lists-and-views) · crm-product · Official help article read.

**Observed:** Distinguishes objects, relationships, lists and views. **Apply:** Avoid duplicating records merely to present different subsets. **Limit:** Choose domain cardinality from the actual brief.

### S34 · HubSpot saved views

[Source](https://knowledge.hubspot.com/records/create-and-manage-saved-views) · crm-product · Official help article read.

**Observed:** Documents filters, view types, columns, sorting and sharing configuration. **Apply:** Treat saved views as explicit reusable configurations. **Limit:** Product-specific limits and entitlements are not universal CRM rules.

### S35 · Pipedrive pipeline view

[Source](https://support.pipedrive.com/en/article/pipeline-view) · crm-product · Official help article read.

**Observed:** Cards summarize deals and next activities, with full details and won/lost outcomes. **Apply:** Connect pipeline progression to real activities and records. **Limit:** Do not assume moving a card is a complete validated transition.

### S36 · Dashboard Design Patterns

[Source](https://dashboarddesignpatterns.github.io/patterns.html) · research · Research project pattern page read.

**Observed:** Distinguishes data, metadata, visual encoding, interaction, and composition patterns. **Apply:** Design dashboards around questions and information relationships. **Limit:** This skill's specific CRM templates are original synthesis, not validated outcomes of the paper.

### S37 · Anthropic frontend-design skill

[Source](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) · design-skill · Source file read.

**Observed:** Advocates brief-specific intent, a small design plan and self-critique. **Apply:** Make domain-specific visual decisions and critique the result. **Limit:** Marketing-oriented novelty rules need restraint in daily CRM work; source not copied.

### S38 · Vercel web-design-guidelines skill

[Source](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md) · design-skill · Source file read.

**Observed:** Routes audits through current interface guidance and concrete code findings. **Apply:** Keep review rules evidence-backed and current. **Limit:** Optional companion, not a dependency or permission grant.

### S39 · Impeccable

[Source](https://github.com/pbakaus/impeccable) · design-skill · README read.

**Observed:** Describes separate shaping, audit, hardening and polish activities. **Apply:** Separate product truth, visual direction and quality review. **Limit:** README capabilities not executed here; reject mechanical font/color bans when they harm the brief.

## Craft and implementation

### S40 · Emil Kowalski: Great Animations

[Source](https://emilkowal.ski/ui/great-animations) · creator · Author article read.

**Observed:** Discusses response speed, purpose, frequency, easing and accessibility. **Apply:** Use motion to explain changes without delaying frequent work. **Limit:** Timings are contextual; this skill's token values are starting defaults.

### S41 · Emil Kowalski: Agents with Taste

[Source](https://emilkowal.ski/ui/agents-with-taste) · creator · Author article read.

**Observed:** Explains making design judgments explicit enough to guide agents. **Apply:** Turn vague polish requests into specific rules and examples. **Limit:** Does not guarantee any agent's output quality.

### S42 · Rauno Freiberg: Interaction Design

[Source](https://rauno.me/craft/interaction-design) · creator · Author essay read.

**Observed:** Examines familiar metaphors, intent and interruptible interactions. **Apply:** Preserve control, continuity and predictability. **Limit:** Essay observations are not normative accessibility requirements.

### S43 · Rauno Freiberg: Novelty

[Source](https://rauno.me/craft/novelty) · creator · Author essay read.

**Observed:** Relates repeated actions to reduced value of extravagant visual novelty. **Apply:** Keep frequent actions quiet; reserve distinction for meaningful moments. **Limit:** Author presents a hypothesis, not a measured universal law.

### S44 · mxkaske Craft

[Source](https://craft.mxkaske.dev/) · creator · Author index and indexed table description read.

**Observed:** Catalogs interaction explorations including a data-table controls/filter example. **Apply:** Use as a discovery route to focused interaction examples. **Limit:** Index-level review only; no independent behavior audit or component adoption.

### S45 · Vercel Web Interface Guidelines

[Source](https://vercel.com/design/guidelines) · implementation · Guidelines page and repository command source read.

**Observed:** Covers keyboard/focus, input behavior, URL state, mutation feedback and interface details. **Apply:** Review interaction details as well as visual styling. **Limit:** Conflicting zoom/overflow suggestions must not override accessibility; no blanket compliance claim.

### S46 · nuqs basic usage

[Source](https://nuqs.dev/docs/basic-usage) · implementation · Official documentation read.

**Observed:** Synchronizes component state with URL query values. **Apply:** Preserve shareable navigation/filter state where safe. **Limit:** Sensitive criteria may belong behind a saved-view ID; URL state is not access control.

### S47 · TanStack v8 pagination

[Source](https://tanstack.com/table/v8/docs/guide/pagination) · implementation · Versioned official documentation read.

**Observed:** Manual pagination assumes pre-paginated data and needs totals for known page counts. **Apply:** Keep server/client pagination responsibilities explicit. **Limit:** Version-specific v8 source; do not apply its APIs to a v9 implementation.

### S48 · WCAG non-text contrast

[Source](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) · accessibility · Official understanding document read.

**Observed:** Required control and state visual information has contrast requirements against adjacent colors. **Apply:** Check borders/icons/state indicators that convey necessary meaning. **Limit:** Decorative separators and inactive states have distinctions/exceptions.

### S49 · WCAG reflow

[Source](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) · accessibility · Official understanding document read.

**Observed:** Describes reflow without loss of information/function with exceptions for necessary two-dimensional content. **Apply:** Test narrow/zoomed layouts while allowing legitimate table scrolling. **Limit:** Table exception does not exempt surrounding controls or the entire app.

### S50 · web.dev INP

[Source](https://web.dev/articles/inp) · performance · Official article read.

**Observed:** Defines interaction latency and field percentile thresholds. **Apply:** Measure responsive feedback and avoid blocking interactions. **Limit:** Local tests do not establish field INP or production performance.

### S51 · Louis customer list and drawer

[Source](https://crm-customer-ui.vercel.app/) · live-demo · Page content retrieved; visual interaction not tested.

**Observed:** Content includes a customer grid and record details with relationship/contact fields and work tabs. **Apply:** Use as a contextual record-inspector reference. **Limit:** No claim of tested focus, persistence, tab behavior or accessible drawer implementation.

### S52 · SakaniUI CRM composition source

[Source](https://github.com/samzydd/Sakaniui/blob/main/src/blocks/CRMDashboardBlock/CRMDashboardBlock.tsx) · implementation · Source inspected; blob 3e7d1f430b6eab936a2926d5436c26fb348b5460.

**Observed:** Source describes an icon rail, entity tabs, collapsible filters, toolbar, table and footer assembled from primitives. **Apply:** Study composition while supplying application-specific data/behavior. **Limit:** Separate resource in same repository as S01; not an additional independent publisher. No copied source or avatar assets.
