# Search-results workspaces

Use for job discovery, lead lists, directories and other pages where finding, comparing and inspecting results is the main task. A jobs search page is not automatically an applicant-tracking system; preserve the actual objects and actions in the brief. These are original adaptations of the table/filter/detail contracts in patterns.md, not a reviewed domain standard.

## Define scope before layout

Record what is searched, which fields are allowed, how filters combine, how nulls/dates behave, and whether rows/counts/facets are server- or client-scoped. Search only permitted fields. Distinguish a source result from an already saved CRM record; Save, Open source and Contact are different actions. Show source/freshness context when it changes the operator's decision.

A job result might need role, employer, location/work model, source and posted time. Compensation needs currency and period when available; missing compensation is unknown, not zero. A lead result might need person/company, role, source, owner and last activity. Do not transplant job fields into a lead database or invent extra business modules.

## Composition

Use a compact page identity, one clear query bar, a small group of frequent filters, removable applied chips, result scope/sort, then a dominant list. Keep the default row dense enough to compare useful results. Use a context-preserving inspector for quick review and an explicit full-record/source link for deeper work.

Prioritize identity and the next action; keep metadata quieter. A restrained summary is useful only if it answers a repeated question. Avoid pushing results below a decorative header or filling unused space with metrics. Keep existing view and shell conventions during a revamp.

## Query and navigation contract

- Use typed filters; a useful initial convention is OR within a multi-select and AND across fields. Expose the actual grouping if the backend differs.
- Each chip removes only its own condition. Reset clears the documented query scope, not unrelated workspace settings. Keep counts and reset reachable when filters wrap on narrow screens.
- Filter/sort changes reset pagination. Results, counts, facets, selected scope and any export use the same normalized query and permissions. Ignore stale responses without dropping input focus.
- Preserve query, scroll and a logical focus position when returning from detail. Use existing route/history conventions; do not put private search text into public URLs just to make restoration convenient.
- Distinguish initial loading, refetch with retained results, no matches, no records, denied access and failed retrieval. A failed request must not be displayed as zero results.
- When saving or changing a result, update the list/detail relationship and relevant counts. Do not remove an item from the current view before the outcome is confirmed or recoverable.

## Pop-outs and narrow screens

Use popovers.md for sibling ownership, Escape, focus departure and modal layering. A filter popover should not compete with another sibling popover for keyboard input. Keep legitimate nested controls within their parent's interaction boundary.

At narrow widths wrap query controls, retain active chips and reset, and prioritize result identity/status/next action. An inspector can become an overlay/full route. Intentional table scrolling is acceptable; page-wide hidden overflow is not a repair.

## Acceptance scenarios

1. Combine text + two filters; verify the intersection, count, facets and null/date cases using a known dataset.
2. Apply and clear criteria from the last page; no valid results disappear into an out-of-range page. Race a slow response with a newer search.
3. Open a result, move between results, close and return; verify query, scroll, correct record identity and focus.
4. Open picker A then picker B; only the intended sibling remains open. Escape dismisses the topmost popup without closing the inspector or losing drafts.
5. At desktop and 390/320px, inspect long titles, duplicate names, missing metadata, open pop-outs, no matches and query failure.
6. For a visual update, rerun the affected pre-existing save/navigation/selection actions and record both observed results and unverified boundaries.
