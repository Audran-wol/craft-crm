# Reusable component specifications

Use with foundations.md for token values and patterns.md for behavior. Dimensions below are original starting defaults. They are not measurements from the research demos or substitutes for testing real content. Retain a coherent existing design system.

## Compose before decorating

Build this hierarchy: workspace shell → page identity → view/query controls → main work region → contextual detail. Give each level one purpose. A nested card is not required at each level. At desktop size, align the title, tabs, toolbar and main data edge. Use one dominant work region; reserve a second panel for useful context.

## Component inventory

| Component | Anatomy and starting size | Required behavior and states | Narrow-screen adaptation |
| --- | --- | --- | --- |
| Sidebar | Workspace identity, labeled navigation, active state, secondary settings; 224–256 px expanded | Active route, long label, workspace switching, collapsed labels/tooltips | Drawer with correct focus behavior; keep current page identity visible |
| Page header | Breadcrumb if useful, title, optional context, main action; 56–64 px minimum height | Long title, permission-limited action, loading identity | Allow wrapping; prioritize action and identity rather than squeezing |
| Saved-view bar | Active view name, alternate views, optional layout selector | Unsaved changes, private/shared scope, accessible overflow | Scroll or menu secondary views; never hide active view |
| Query toolbar | Scoped search, quick filters, sort, display controls; 8 px control gaps within 16–24 px groups | Active conditions, reset, pending query, result scope | Search gets usable width; advanced controls open a labeled panel |
| Data table | Selection if needed, identity, comparison fields, row actions; 40/48/64 px row densities | Sort, selected/hover/focus, loading, empty, error, overflow, pagination | Prioritize columns or use record summaries; preserve explicit detail access and horizontal scroll where needed |
| Table footer | Known result range, pagination or load-more, page size where useful | Last/empty page, pending request, changed total | Wrap controls; do not force tiny buttons |
| Record summary/card | Identity, status, one or two decision fields, next action | Long identity, missing values, selection, pending | Useful alternative to a wide table; do not drop essential comparison information silently |
| Record inspector | Identity/action header, properties, related records, recent activity; 400–560 px | Opening/loading, permissions, unsaved draft, error, full-record link | Full-width detail route/panel; preserve return context |
| Full record page | Identity header, summary fields, meaningful tabs, timeline/relationships | Deep link, not found, access denied, concurrent update | Stack sections in task order; avoid a fixed wide two-column form |
| Field/input | Persistent label, control, optional hint, error; 32–40 px desktop control height | Hover/focus/disabled/read-only/invalid/pending; accessible description | Prefer 44 px targets; 16 px input text as a practical mobile default; zoom remains enabled |
| Relation picker | Search, identity + distinguishing context, selected values, clear | Duplicate names, loading, no match, permission-limited results | Full-width popover/dialog using existing primitive and keyboard model |
| Select/filter popover | Labeled trigger, property/operator/value or options; commonly 240–360 px | Placement, collision, keyboard, selection, apply/cancel if staged | Fit viewport; use a larger sheet/dialog for complex expressions |
| Action menu | Labeled trigger, scoped verb labels, optional destructive group | Keyboard focus, disabled explanation, dismissal, focus return | Comfortable hit areas; no hover-only access |
| Dialog | Title, purpose, content, scoped footer; width follows content | Initial focus, containment if modal, close, validation, pending/recovery | Fit viewport height and keep content/actions reachable with scrolling |
| Activity timeline | Type, actor, timestamp, content, related record, next action | Empty history, long notes, attachments, permission-limited entries | Single column, explicit dates; expandable detail without losing context |
| Task/agenda row | Task, related record, due time, owner, completion control | Overdue, done, pending, failed update, reassignment | Keep next action visible; keyboard and touch completion |
| Pipeline card | Identity, stage context, value if relevant, owner, next action | Move, validation, pending, failed rollback, selection | Horizontal board or list alternative; click/tap move option |
| Status badge | Stable text + semantic color, optional icon; small controlled padding | Unknown/new status, disabled vs inactive distinction | Do not truncate the only status meaning |
| Toast/banner | Outcome or actionable warning, optional retry/undo | Accurate timing, announcements, dismissal; no duplicate success | Avoid covering primary controls; persistent errors remain near affected work |
| Empty/error state | Scope-aware explanation, useful next step | No data vs no matches vs no permission vs failed load | Preserve query/context and reachable recovery |
| Dashboard module | Decision, definition, scope/time/unit, visualization + drill-down | Missing/stale/partial/zero data, accessible values | Stack by importance; simplify chart labels without losing meaning |

## Tables: precise visual rules

- Share column definitions between header and rows. Include selection/action columns and scrollbar width in alignment.
- Starting cell padding: 12–16 px horizontal. Keep the same edge for related header/body content. Numeric headers and values share right alignment.
- Prefer 6–8 useful default columns when the task permits; this is a heuristic, not a hard cap. Identity may need 200–280 px, compact status/owner fields less. Measure actual translated text.
- Use `min-width: 0` for shrinkable flex/grid children; put intended horizontal scroll on the data region. Fix sticky offsets and overlay clipping explicitly.
- Keep selection, link and menu hit areas independent. A row click alone is not a keyboard-accessible record link.
- Truncation needs a way to obtain the full value using keyboard/touch as well as mouse. Do not make every cell a tooltip.
- Use tabular numerals for comparable numeric columns. Never align amounts by inserting spaces.
- Row height is a minimum; wrapped/translated content must not be clipped. A density toggle changes related spacing consistently.

## Custom dropdowns and pickers

For a newly designed branded CRM, the closed trigger and open popup belong to the same component system. A styled native select still opens a browser/OS popup; it does not satisfy an explicit request for a custom dropdown. Prefer the project's existing accessible select/combobox primitive; for a dependency-free prototype, implement the same interaction contract and verify it. Retain native buttons, text inputs and form semantics around it.

- Match control height, typography, border, radius and focus ring across filters, form fields, locale and stage controls. Use a consistent chevron and selected check; selected, active/hover, disabled and pending states must remain distinct.
- Fit the popup to the trigger/content and viewport; allow long labels and intentional option scrolling. Check its placement near viewport edges and inside dialogs/table scrollers. A popup below a modal backdrop is broken even if it works on the main page.
- Give the visible control a name distinct from its current value, expose expanded state and associate its popup. Use the appropriate select-only or editable combobox/listbox model [S27], rather than an action menu for a field value. Keep options free of nested buttons/links.
- Support opening and choosing by keyboard, option navigation, Escape without an unintended change, and logical focus after selection/dismissal. For long lists provide typeahead or search, with an honest no-results state. Preserve native text editing behavior in editable controls.
- Check pointer/touch selection, outside dismissal, form submission, required-field errors, and focus restoration after localization/rerenders. Hidden native backing fields may preserve form data, but must not create duplicate focus targets or expose a native popup.
- Keep simple option lists simple. Add avatars, counts, grouping or descriptions only when they help distinguish real options; do not invent metadata to decorate a menu.

Acceptance: open every distinct dropdown variant, select a value and prove its effect; dismiss with Escape; exercise keyboard navigation; inspect selected/disabled/empty states; inspect an open form dropdown at desktop and 320/390 px widths. Record actual rendered evidence. APG references: [combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) and [listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/).

## Icons and microdetails

Choose one primary icon family already used in the app; otherwise Lucide/Tabler are candidates [S19/S20]. Verify the actual exported names. Use semantic mappings in foundations.md.
Typical icon size: 16 px in controls/data, 18–20 px in navigation, 20–24 px for standalone actions. Retain consistent stroke settings and optical alignment. Do not scale one family randomly to imitate another.
Use an 8 px starting gap between icon and text. Small glyph size does not determine hit-area size. Give icon-only actions a programmatic name, visible focus and explanatory label/tooltip where useful. Use visible text for ambiguous or consequential actions. Hide decorative SVGs from assistive technology. Do not use emoji as an accidental interface icon family.
Status, relationship and action icons must have consistent meaning across modules. Brand logos may remain distinct. Empty avatars get deterministic initials/fallbacks; they do not need a rainbow palette.

## Responsive contract

| Content pressure | Response | Preserve |
| --- | --- | --- |
| Wide work surface | Expanded navigation; table; optional inspector | Shared alignment, reasonable readable widths |
| Constrained desktop/tablet | Collapse optional navigation; reduce secondary columns; inspector may overlay | Main action, active filters, identity, selected scope |
| Phone | Compact header; navigation drawer; priority fields; full-screen detail | Search/filter/reset, record access, next action, form recovery |
| 320 px / zoom / enlarged text | Wrap controls; allow purposeful scrolling; flexible row heights | Readability and every essential control |

Use foundation sample viewports to test, not as blindly copied CSS breakpoints. Decide from content pressure. Test French/other long labels, numbers, large names and error text. Use logical CSS properties when directionality matters; RTL needs a deliberate audit of navigation, icons and charts.

Check mobile browser chrome, safe-area padding and on-screen keyboard where relevant. Avoid fixed footers that cover form fields. On coarse pointers, provide comfortable targets even when a desktop density toggle is compact. Avoid hover-only row menus.

## Completion checklist

For every implemented component, account for: purpose; semantics; default/hover/focus/selected/disabled/pending/error states where applicable; text overflow; keyboard; touch; loading/empty data; permissions; and responsive behavior. Not every component needs every state. Document meaningful omissions and verify assembled screens rather than treating component-level claims as proof.
