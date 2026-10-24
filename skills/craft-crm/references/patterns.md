# CRM pattern contracts

Contents: [shell](#shell-and-navigation) · [tables](#record-tables) · [filters](#filters-and-saved-views) · [records](#record-details-and-activity) · [pipeline](#pipeline) · [dashboard](#decision-dashboard) · [invoices](#invoice-operations) · [support](#support-and-customer-success) · [forms](#forms-imports-and-exports) · [states](#state-matrix).

Specifications below are original synthesis. Source IDs identify supporting patterns, not a claim that a source mandates every detail.

## Shell and navigation

Sources: S01, S09, S16, S28.
- Workspace/organization switcher changes data scope. Page title identifies the object. Saved view identifies the current subset. Never visually merge these three meanings.
- Keep primary navigation limited to actual modules. Group settings/integrations separately from work; allow saved views/favorites without an uncontrolled tree.
- Use one active item and preserve its label when navigation collapses.
- Put account menu in a stable place. Unread/task counts need defined meanings.
- Search scopes: global finds across objects; local filters current data. Use distinct placeholders and results.
- Page header: title, optional count/context, primary object action, rare page actions.
- View bar: saved view, table/board choice when relevant, query controls. Do not repeat the title or full global navigation inside every card.
- Keep global command search optional. Keyboard shortcuts supplement visible controls; never intercept typing or browser defaults without justification.

Acceptance: navigate from list to record and back; correct workspace, active item, view, and search remain understandable.

## Record tables

Sources: S02, S07–S10, S13, S15, S18, S21.
- Choose columns by comparison task. Default list often needs identity, owner, stage/status, next activity, last interaction, and one business value. Do not show the whole schema.
- Keep record identity prominent and linkable. Secondary identity fields use a consistent second line. Missing avatars use initials or a neutral fallback, not unrelated photos.
- Align text left and quantities right; keep numeric precision/currency consistent. Display unknown as “Not set” or an explained dash, not zero.
- Define column widths and minimums. Pin identity only if wide-table scanning needs it. Keep header and body widths synchronized, including scrollbars.
- Use subtle row dividers or hover to support scanning. Zebra stripes are optional, not decoration.
- Give sorts visible direction, predictable null ordering, and stable tie-breaking. Multi-sort needs an explicit priority order.
- Use native table markup for ordinary tables. Use a managed grid only when spreadsheet-like navigation/editing justifies the extra keyboard model [S21].
- Row selection and row navigation must not conflict. Clicking a checkbox/menu should not also open the record. Label each checkbox and action menu with record identity.
- Bulk action bar replaces or clearly supersedes the normal toolbar. Show count and clear selection. Distinguish “25 on this page” from “all 2,400 matching.”
- Pagination shows scope and totals when known. Do not invent a total for cursor pagination. Preserve selection behavior across pages explicitly.
- Offer column visibility/resizing only when useful; keep identity recoverable. Do not allow every column to disappear without recovery.
- For inline edit, provide an entry affordance, draft/commit/cancel, validation, pending status, and rollback. Avoid accidental save on blur for consequential fields.

Acceptance: sort actual values; filter beyond first page; open the correct record; bulk action affects the stated set; narrow layout retains identity; keyboard can reach required actions.

## Filters and saved views

Sources: S02, S03, S07, S08, S14, S32–S34, S46.
- Build a typed sequence: property → appropriate operator → valid value. Text, dates, amounts, people, boolean, single-select, multi-select, and relations need different controls.
- Define semantics: a useful default is OR within a multi-select field and AND across fields. Expose AND/OR grouping only when users need it; show grouping clearly.
- Define missing-value operators separately from empty strings. Relative dates use the declared user/workspace timezone; distinguish date-only values from timestamps.
- Quick filters cover frequent criteria. Advanced builders hold complex expressions; retain active chips/count outside the closed popover.
- Cheap/simple criteria may apply immediately; expensive/multi-step criteria can stage behind Apply/Cancel [S14]. Do not mix these behaviors invisibly.
- Search text is not a saved view name. Debounce remote search as needed; Enter/Escape and clearing behave predictably.
- Show filter summary, result count, per-filter removal, and clear-all. A filtered-empty result offers reset, not only “Create first record.”
- Save view stores query, sort, visible columns/order, layout, and ownership/visibility where supported. Distinguish temporary edits from saved/shared configuration.
- A shared view's existence never grants access to underlying records. Changing shared defaults must have explicit scope.
- Keep result rows, counts, financial totals, facets, exports, and pagination consistent. State whether facet counts are before or after other filters.
- Restore via refresh/Back/Forward when part of the contract. For private conditions, URL uses a permission-checked saved view ID rather than sensitive text.

Conflict worth understanding: Carbon discourages hiding multiple categories inside a simple dropdown, while modern CRM builders use richer popovers. Use a searchable property selector for entry; keep applied conditions visible and use a larger panel for complex multi-category editing. Do not call a cramped menu a full query builder.

Acceptance: apply owner+status, verify intersection; clear one; clear all; test null/date boundaries; save/reopen; change page size; export same scope; race two searches.

## Record details and activity

Sources: S04–S06, S28, S51, S17, S26.
- Inspector: quick review/edit while retaining the list's search, scroll, and selection.
- Full route: deep work, long timelines, complex forms, links opened in a new tab. Provide “Open full record” if the inspector is constrained.
- Header: identity, status, owner, primary action. Summary: a few key properties and relationships. Timeline: dated interactions with author/type and expandable detail.
- Keep relationships visible: company ↔ people ↔ opportunities. Do not duplicate conflicting values into disconnected cards.
- Tabs represent meaningful work areas, not each individual field. Preserve edits before changing tab or closing.
- Use explicit Save/Cancel for multi-field forms. If autosave is chosen, expose pending/saved/error and recovery.
- Modal drawer: move focus inside, contain it, make background inert, close via accessible control/Escape as appropriate, return focus.
- Non-modal inspector: do not trap focus or falsely set aria-modal; provide clear keyboard navigation between list and panel.
- Preserve a recoverable draft and warn before losing unsaved work. Do not silently discard after a failed request.
- Timeline avoids “Everything happened just now” demo data; show meaningful dates, empty history, long notes, and permission-limited items.

Acceptance: open record, edit, fail save, retain draft, close/reopen, return to exact list context. Test no-permission and deleted-record links.

## Pipeline

Sources: S04, S06, S10, S35.
- Use business-defined stages with entry/exit meaning. Won and lost are outcomes; do not confuse them with generic task completion.
- Header per stage: name, record count, value and currency scope if relevant. Exclude hidden records consistently with filters.
- Card: deal/account identity, value, owner, next activity or urgency. Do not turn each card into a mini dashboard.
- Provide a visible “Move to stage” action alongside drag. Keyboard users need equivalent control; pointer users who cannot drag need click/tap alternative [S25].
- On move, validate allowed transition and required fields. Confirm pending outcome; roll back on failure.
- Record reason/date for lost/won if required. Do not treat drag to a decorative bin as authorization for deletion.
- Show empty columns as usable drop targets. Board may scroll horizontally; keep stage context clear.
- Deal count/value must not double-count related contacts. Mixed currencies need grouped totals or an explicit conversion basis.
- Stage color is a secondary cue, not the only meaning.

Acceptance: move with pointer and keyboard alternative; reject a forbidden move; simulate save failure; verify totals and record detail agree.

## Decision dashboard

Sources: S28, S36, S50.
- Start with questions: “Which deals need follow-up?”, “What is overdue?”, “Where is work blocked?”
- Define every KPI: formula, scope, unit, time window, comparison baseline, update time, and a route to relevant records.
- Prefer a small summary strip plus an actionable queue. Zero KPI cards is valid.
- Match chart to question: trend → line; category comparison → bar; composition → restrained stacked bar; exact comparison → table.
- Use common axes/scales when comparing. Do not use a truncated axis to exaggerate differences without clear labeling.
- Show unavailable/stale/partial data distinctly from zero. A percent change from zero needs a non-misleading alternative.
- Keep dashboard filters and drill-down parameters aligned. Show which widgets use different scopes.
- Provide textual/table alternatives for important chart information. Do not force a hover tooltip as the only way to retrieve values.
- Domain metrics are not interchangeable: pipeline value is not recognized revenue; invoice amount is not cash collected.

Acceptance: recalculate one metric from fixtures; drill down to matching records; test zero baseline, mixed currency, loading, missing data.

## Invoice operations

Sources: S03, S11; domain rules below are synthesis, not financial advice.
- Default list: invoice ID, customer, due date, status, amount/currency, balance where needed, row actions.
- Separate draft, sent/pending, partial, overdue, paid, canceled when the backend supports them. Do not invent an unsupported status enum.
- “Overdue” depends on outstanding balance, due date, timezone and business policy. Displayed demo labels are not an accounting rule.
- Show count and sum for the current scope. Do not sum currencies blindly.
- Detail: issuer/customer, line items, tax/discount information from source data, totals, due/payment history.
- Group actions by lifecycle: edit draft; preview/send when authorized; follow up; record payment only through authorized backend; export.
- Reminder preview includes recipient and invoice. Sending is a real external action requiring the user's applicable authorization.
- Make canceled/paid state clear; avoid continuing to nag already paid customers.

Acceptance: filter overdue, reconcile count/sum, test partial payment and overdue boundary, verify export/preview scope. Do not execute real payment/reminder actions as an unsolicited test.

## Support and customer success

Sources: S28 and record/context principles in S04/S06/S51; this is a synthesized extension, not a reviewed helpdesk product clone.
- Queue contains priority, owner, age/SLA when defined, customer, and brief issue.
- Active case keeps conversation and next action dominant; customer context stays secondary.
- Avoid sorting purely by latest update if it hides urgent old items.
- Preserve reply drafts across queue navigation. Distinguish internal note from customer reply with label and audience.
- Resolve/reopen/assign actions need honest state transitions and history.
- Health scores need definitions, timestamps and constituent signals; do not present invented scores as real predictions.

## Forms, imports, and exports

Sources: S04, S27, S30, S34, S45.
- Use short creation forms with required fields; progressive optional detail. Always label inputs and give examples for unusual formats.
- Searchable owner/account pickers need loading/no-results states and keyboard support.
- Validation identifies the field and recovery; complex forms also provide a linked error summary. Preserve entered values after server failure.
- Import flow: choose file → map columns → validate/preview → resolve duplicates → confirm scope → progress → outcome/retry failed rows. Do not mutate before preview.
- Duplicate resolution explicitly identifies merge winner, conflicts, and irreversible impact. Do not silently merge contacts by name.
- Export declares filtered/all/selected scope and fields. Honor permissions; handle partial/async exports and errors.

## State matrix

| State | User sees | Recovery / expectation |
| --- | --- | --- |
| Initial loading | Geometry-preserving placeholder | No fake zero metrics |
| Refresh | Existing content plus local pending cue | Focus/selection stable |
| No records | Explanation and permitted create/import action | Does not imply error |
| No filter matches | Active query and clear/reset | No loss of saved view |
| Network failure | Failed region with retry | Existing/draft data retained where possible |
| Partial failure | Success/failure counts and affected records | Retry only failures |
| No permission | Clear access explanation | No unauthorized hidden-field leakage |
| Invalid input | Field error and summary when needed | Fix without retyping |
| Mutation pending | Pending control and duplicate prevention | No premature success |
| Mutation failed | Error and retained draft/rollback | Retry or cancel |
| Conflict | Changed version explained | Review/reload/merge supported by backend |
| Deleted record | Gone state and return path | No endless spinner |
| Offline/stale | Last known data and timestamp if available | No false saved/synced claim |
