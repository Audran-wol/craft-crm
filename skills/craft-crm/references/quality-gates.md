# Quality gates and evidence

Use these as a review rubric, not a certification. Evaluate applicable behavior, not visual fashion.

## Critical gates

G01 Main workflow completes with actual state change.
G02 Permission and data boundaries remain intact for integrated apps; prototypes clearly state their boundary.
G03 Required actions are keyboard accessible; focus is usable.
G04 Failed saves preserve user input or restore a truthful prior state.
G05 Layout keeps core content/actions reachable at supported widths and zoom.
G06 Counts, filtered rows, totals, and selected scope agree.
G07 Existing required behavior remains intact during a revamp.

Any applicable fail blocks “ready.” Unknown/unverified critical gates block that claim too. Mark not applicable only with a concrete reason; do not exclude gates to inflate a score.

## Scored dimensions

| Dimension | Weight | Evidence |
| --- | --- | --- |
| Workflow/data behavior | 25 | Primary scenario, filter/selection semantics, save outcomes |
| Information architecture | 15 | Navigation, action scopes, context retention |
| Composition/hierarchy | 20 | Rendered screenshot, alignment, density, domain relevance |
| Consistency/details | 15 | Type, icon family, geometry, copy, numeric alignment |
| Accessibility/responsiveness | 15 | Keyboard, focus, contrast, widths, zoom |
| Adverse states/performance | 10 | Empty/error/loading/conflict, latency observations |

For each dimension use 0–4: 0 unusable, 1 major defects, 2 workable with defects, 3 strong with minor issues, 4 strong and evidenced for the agreed scope. Unknown is null. These are judgment scores, not automated measurements.
The bundled scorer computes weighted score on applicable dimensions and evidence coverage. Default ready threshold: 85/100 plus all applicable critical gates pass and full dimension evidence. This threshold is this skill's heuristic.

## Minimum scenario set

Run scenarios for features in the delivered scope. Selection, saved views, boards, exports and other optional modules are not required merely to satisfy a checklist. For report-only audits, record available observations and unverified behavior rather than implementing missing features.

1. Find a record using combined filters; clear one; navigate across pages; return via Back.
2. Open record, edit meaningful field, verify list/detail agreement, and check refresh persistence.
3. Select records and perform a reversible local/test action; prove scope.
4. Perform the domain-specific task: stage move, task completion, invoice filter, or support assignment.
5. Simulate one failed save; verify draft retention/rollback and useful recovery.
6. Keyboard-only navigation through list, primary action, form, menu, and inspector; Escape and focus restoration.
7. Inspect desktop and narrow/mobile layouts with long text and empty results.

When local persistence is implemented, also exercise malformed/wrong-shape saved data and a rejected write. An error must preserve both the prior persisted bytes and the user's draft. For locale/filter/navigation rerenders, check the focused element before and after; a correctly translated view can still strand keyboard focus on the document body. For due-state views, completed/canceled work must not retain an active overdue warning merely because its date is in the past.

For each executed scenario record the fixture, action, expected result, actual result and method (source inspection, logic harness, browser interaction, screenshot, or assistive technology). A DOM stub cannot establish focus, layout or native input behavior. Use a declared test clock for relative-date boundary checks. Record viewport dimensions for rendered evidence; a CSS media query existing in source is not a phone test.

For a small polish request, run only scenarios affected by the change plus relevant regression gates. Do not test real customer mutations without authorization.

## Visual pass

Inspect actual renders, not only component code. Compare the same route/data/viewport before and after.
Check shared alignment edges, primary/secondary contrast, row rhythm, truncation strategy, toolbar grouping, badge semantics, scroll ownership, menu clipping, and consistent icon sizes.
Look at populated, filtered-empty, open menu, open inspector, form-error, and mobile states. Note unrendered states.

## Accessibility pass

Normal text contrast 4.5:1; qualifying large text 3:1 [S24]. Necessary non-text indicators generally 3:1 [S48].
WCAG 2.2 target-size AA uses 24×24 CSS px or defined spacing/other exceptions [S22]; 44×44 is this skill's preferred touch comfort target, not the AA minimum.
SC 2.4.11 requires focus not entirely obscured [S23]; aim to keep it fully visible.
Drag alternative must be single-pointer without dragging [S25], as well as keyboard operable.
Use native HTML semantics for buttons, text inputs and ordinary tables. Styled select/combobox popups must follow the chosen component's keyboard and focus contract; inspect both the closed and open state. Table/grid choice and modal behavior follow APG [S21/S26/S27].
Test zoom/reflow [S49]. Never disable zoom to conceal layout issues.
Automated a11y tools help but do not prove conformance. Screen-reader behavior remains unverified unless actually tested.

## Report honestly

For each issue: severity, route/component, evidence, user impact, proposed fix, acceptance check. Separate observed from inferred.
Report executed commands and relevant results concisely. A screenshot cannot prove server authorization; a successful build cannot prove UX quality.
