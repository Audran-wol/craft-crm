# Foundations

Numeric values here are original practical defaults, not measurements from Louis's demos or guaranteed accessibility thresholds. Adapt established brand systems.

## Geometry

| Role | Starting value | Rule |
| --- | --- | --- |
| Expanded navigation | 224–256 px | Fit real labels; collapse at content pressure |
| Icon rail | 56–72 px | Labels/tooltips and discoverable expand control |
| Page gutter | 24–32 px; 16 px narrow | One shared alignment edge |
| Header | 56–64 px minimum | Wrap long/translated titles; avoid clipping |
| Controls | 32–36 px compact; 40 px comfortable | Prefer 44 px touch targets |
| Rows | 40 px compact; 48 px standard; 64 px two-line | One density per view |
| Popovers | 240–360 px | Fit content and viewport |
| Inspector | 400–560 px | Full-screen narrow alternative |
| Radius | 6–8 px controls; 10–12 px surfaces | Pills for actual chips |
| Spacing | 4, 8, 12, 16, 24, 32, 48 px | Tokens; explicit optical exceptions |

Define canvas, work surface, overlay, and selected-state roles. Separate surfaces by tone, border, or spacing without overusing all three. Shadows explain elevation. A card corresponds to a distinct object/task; headings and rules often suffice.
Carbon supports density variants and consistent table geometry [S13]; the values above remain configurable.

## Typography

Retain a readable existing UI face. For new products choose one sturdy sans-serif with needed languages and good numerals; system fonts, Inter, Geist, or IBM Plex Sans can be appropriate. Do not select or ban fonts because AI often uses them.
- Body/data: 14 px / 20 px desktop starting point.
- Supporting metadata: 12–13 px / 18 px; never the only home of critical facts.
- Section title: 16–18 px; page title: 22–28 px.
- Use weight and spacing before color for hierarchy.
- Tabular numerals and right-aligned values/headings for comparisons.
- Consistent casing; sentence case is a default, not a reason to break an existing system.
- Locale-aware formatting; long values get wrapping, resizing, or accessible disclosure.

## Color and contrast

Neutral work surfaces dominate; accent identifies active controls/main action. Semantic status colors keep stable meaning. Separate selected from success, warning from overdue, disabled from loading. Pair color with text/icon.
An upward overdue balance is not a positive trend.
Measure foreground/background combinations. WCAG text thresholds are 4.5:1 normal and 3:1 qualifying large text, subject to exceptions [S24]. Required non-text control/state information generally needs 3:1 against adjacent colors [S48]; decorative rules do not all require that ratio. Check chips, focus, hover, tinted backgrounds, and dark mode.

## Icons

Use the established family or Lucide/Tabler [S19/S20]. Verify exports in the installed version. These are semantic mappings, not guaranteed import identifiers.

| Meaning | Metaphor | Label |
| --- | --- | --- |
| People | Person group | Contacts |
| Organizations | Building | Companies |
| Opportunities | Kanban/briefcase | Deals |
| Work due | Clock/checklist | Activities |
| Billing record | Document/receipt | Invoices |
| Create | Plus | Add contact / New deal |
| Narrow results | Funnel/sliders | Filter |
| Presentation | List/layout | View name |
| Order | Up/down | Sort |
| Row commands | Ellipsis | Accessible “Actions for [record]” |
| Output | Download/arrow out | Export |
| History | Clock/history | Activity history |
| Attention | Warning | Overdue / Needs attention |

Start at 16 px inline, 18–20 px navigation, 20–24 px standalone. Keep optical weight/baselines/gaps consistent. A small glyph may have a 32–44 px hit area. Brand icons may be an explicit family exception. Hide decorative icons from assistive technology. Label interactive controls and ambiguous symbols [S29].

## Scroll and responsive behavior

Declare scroll ownership: page scroll or app-height main data scroller. Navigation/inspectors may scroll independently; avoid accidental body+main vertical scrollbars. Preserve intentional wide-table horizontal scrolling.
Use flex/grid minimum sizing correctly. Account for sticky offsets. Menus escape clipping through established overlay primitives and fit the viewport.

Check 1440, 1280, 1024, 768, and 390 CSS px as sample widths, not universal breakpoints; add 320 CSS px reflow and text zoom [S49]. Tables may qualify for two-dimensional exceptions; surrounding controls still need to work.
Mobile prioritizes identity, status, next action, and details. Do not hide every useful field.

## Motion

Initial defaults: 120–200 ms for small transitions, 180–240 ms for panels. Adjust to distance/frequency. Allow interruption, animate from the trigger, preserve focus/scroll, respect reduced motion [S40–S43]. Frequent actions should be immediate. Avoid row entrance cascades and decorative looping charts.
