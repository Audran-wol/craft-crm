# Pop-out ownership and focus

Use for filter pickers, view controls and other transient panels. Reuse established overlay primitives; this checklist describes behavior, not a request to replace the component library. Use component-specs.md for appearance and quality-gates.md for evidence.

## Choose the interaction model

A field-value picker, action menu, non-modal inspector and modal dialog have different roles and keyboard contracts. A decorative panel with a click handler does not establish any of them. Declare trigger, owner, open state, selected/draft state, dismissal and focus destination.

For sibling pop-outs, coordinate open state: opening a second filter should close the first. Do not prohibit legitimate nested menus or a picker inside a dialog. Escape dismisses the topmost transient layer first; it should not also close its parent dialog or discard a draft.

## Dismissal without focus bugs

- Keyboard dismissal returns focus to the opening control or a meaningful replacement if that control was removed by a query/render.
- A deliberate click outside can move focus to the clicked control. Do not force it back to the old trigger after the user has moved elsewhere.
- If focus leaves a non-modal picker entirely, close or retain it according to the chosen pattern; do not leave an invisible active layer intercepting later keys. Moving focus to a child portal is still inside the logical interaction boundary.
- Internal pointer movement/scrolling is not outside dismissal. Do not close while selecting a checkbox or editing a query unless that control's commit model calls for it.
- Separate draft and committed values for staged Apply/Cancel. Do not make Escape unexpectedly commit a partially edited filter.
- Rerenders, record changes and navigation must clear orphaned overlays and stale focus references. Avoid remounting a live input on every keystroke.

## Layering and placement

Check the actual ancestor scroll/overflow/transform and modal layer. Use the project's portal/top-layer primitive correctly; raising z-index alone may not escape clipping or a modal backdrop. Keep accessibility ownership and focus containment consistent when portaling.

Fit both axes to the viewport, flip where appropriate, cap height and make long option lists intentionally scrollable. Reposition on relevant scroll/resize. In constrained cases use a larger sheet/dialog instead of a panel with unreachable actions. Test enlarged text and long translated labels, not only short placeholders.

## Compact regression sequence

Open A → keyboard through its options → open B → verify A no longer receives input → Escape B → verify logical focus. Then reopen, move focus outside, reopen inside an inspector/dialog, select or cancel, and scroll the page/panel near viewport edges. Verify the chosen value, containing dialog, draft and result count after each step. Repeat at desktop and phone widths.

Source inspection can identify missing handlers and likely clipping; rendered keyboard/touch behavior remains unknown until actually exercised. Record the exact sequence that reproduced a bug instead of claiming all pop-outs are accessible from one successful screenshot.
