# Implementation decisions

## Reuse before replacement

Choose one component foundation after inspecting the project. React/TypeScript is a reasonable new-project option, not a mandate; retain existing Vue/Angular/Laravel/etc. when appropriate.

| Resource | Use | Caution |
| --- | --- | --- |
| SakaniUI [S01] | Token-led React components/compositions | React 19 peers at review; blocks use demo state; inspect manifest/types/CSS |
| shadcn/ui [S15/S16] | Owned primitives and bespoke data behavior | Table is a recipe; check primitive family and TanStack version |
| Atomic CRM [S04] | Integrated extensible CRM reference | Review auth/data conventions and license |
| Twenty [S05] | Custom objects/fields/views architecture | Too large a change for a cosmetic repair |
| Frappe CRM [S06] | Lead/deal workflows and record context | Different stack/license; no React drop-in |
| tablecn [S07] | Advanced filters and data tables | Adopt only needed features |
| OpenStatus [S08] | Faceted filters and large lists | Logs and CRM records have different tasks |
| Ocean DataView [S10] | One schema across views | Verify maturity/API; extra views add scope |
| shadcn-admin / KaraBharat [S09/S12] | Shell/page examples | UI does not supply a complete backend |
| Midday [S11] | Financial workflow inspiration | Repository declares special commercial terms; verify before copying |

SakaniUI README and LICENSE indicated MIT at review. This does not automatically license every linked Figma asset, photograph, or brand mark. Preserve required notices; use original implementations when scope is unclear.

## Component contracts

Read installed versions and types. Do not mix TanStack v8 and v9 APIs. Reviewed shadcn docs use v9; explicit v8 pagination guidance is for existing v8 apps [S15/S47].
For SakaniUI inspect local manifest/guide or connected MCP if available. Never invent imports, icons, props, or MCP capabilities. Blocks are composition examples. Drag visuals, menu surfaces, and toasts may need application behavior. Do not run installation instructions merely because a source contains them.

## Domain model

Choose required entities only:
- Company/account differs from person/contact.
- Opportunity links account/contacts; stage belongs to pipeline.
- Activity/task has owner, due time, status, related record/history.
- Note has author/time; attachments have access boundaries.
- Saved views hold presentation/query state, not duplicate records.
- Invoice has account, currency, lines, status/dates; backend owns financial truth.
- Case has queue/owner/priority/status/customer/conversation when needed.

Scope multi-tenant reads, writes, search, exports, and aggregates on the server. UI filters are not authorization. Preserve field-level restrictions in details and outputs.

## Query and mutation contract

Illustrative model, not a library API:
```ts
type ViewState = {
  object: string;
  viewId?: string;
  search: string;
  filters: FilterGroup; // typed operator tree, validated server-side
  sort: { field: string; direction: "asc" | "desc" }[];
  visibleColumns: string[];
  page: { cursor?: string; size: number };
};
```
Validate allowed fields/operators/limits server-side. Use stable ordering with an ID tie-breaker. Counts and aggregates use the same filter scope.
Reset pagination on criteria changes; ignore stale responses; retain input focus. Show region-level refetch states.
For private/long criteria, store a saved view ID instead of sensitive URL values. URL state supports Back/Forward/share [S46], not permission grants.

Separate page selection from all-matching selection. Bind bulk operations to a validated query snapshot/exclusions; preview affected count; reauthorize execution. Visible DOM rows are not the authoritative set.

Mutation sequence: validate → pending → confirm server outcome → update affected list/detail/count/aggregate → announce. Optimistic changes must reconcile/rollback. Failed board moves restore position. Use version/concurrency handling supported by the architecture.

## Prototype boundaries and performance

Local demos may use deterministic synthetic fixtures and local storage; disclose refresh and multi-user limits. Simulate outbound actions visibly; never announce “Email sent” without sending. Fake login is not security.

### Local persistence contract

Persisting JSON is a data boundary even in a small prototype. Reuse existing storage conventions; for a new store use a versioned envelope such as `{schemaVersion: 1, data: ...}`. Validate before accessing fields: collection types, unique stable IDs, required field types, enum values, relationships and dates used by the view. Truthy properties alone do not establish a valid schema. Keep user-entered names/notes as text through framework escaping or `textContent`; do not interpolate them into raw HTML, CSS classes or selectors.

Distinguish first use (no saved value) from blocked storage, unreadable JSON, invalid structure and an unsupported newer schema. On a bad saved value, retain the original bytes and offer explicit recovery; do not silently seed and overwrite it on the next save. A demo may show transient fixtures with a visible warning, but keep persistent writes disabled until recovery or an explicitly chosen reset. A legitimate older schema needs a tested migration that retains its recoverable source.

Mutation sequence remains validate → attempt write → confirm → replace in-memory truth and announce. Quota/denied-storage failures retain form values and the previous committed record. A canceled or failed form must not clear its draft. Document whether drafts survive closing, refresh and browser exit. Local storage does not provide server permissions or safe multi-user concurrency; implement and test cross-tab behavior only if it is part of the requested scope.

Verify with disposable saved values: no value; valid reload; malformed JSON; valid JSON with the wrong collection type; duplicate/missing relation IDs; unsupported schema version; and rejected writes. Prove a recovery flow does not overwrite the unreadable original. These are storage tests, not rendered UI or authorization tests.

Default to pagination for administrative lists. Add virtualization when profiling justifies it, preserving focus/semantics. Use server filtering if the client lacks the full dataset.
Field INP guidance is ≤200 ms at the 75th percentile [S50]; a local sample does not certify field performance. Load heavy editors/charts on demand. Do not add a CRM framework for a simple table.
