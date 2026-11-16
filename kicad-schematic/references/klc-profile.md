# Applying KLC to project schematics

This is **our project profile**, not upstream KLC text. The separately attributed
[offline snapshot](klc/NOTICE.md) preserves 19 selected rules and 20 illustrations
at a pinned revision. It is sufficient for the selected conventions without
internet access, a Hugo installation, or the original project screenshots.
Upstream source links and the bus-order wiki link are optional further reading;
they are not prerequisites for applying this profile offline.

Exact-device electrical requirements and package mapping constrain all drawing
choices. Explicit project requirements override stylistic defaults. Apply the
selected KLC rules through the scope and exceptions below; do not claim complete
KLC compliance or official-library acceptance for a project drawing.

## Load the relevant rules

| Task | Read | Inspect when useful |
| --- | --- | --- |
| Select a stock symbol or decide whether customization is needed | [G2.1](klc/library-fields.md#g21) and [symbol design](symbol-design.md) | G2.1 illustrations distinguish reusable primitives from exact parts |
| Draw or reshape a custom symbol | [Graphics](klc/graphics.md) and [pins](klc/pins.md) | S3.4 for functional interiors; S3.5 for connection points; S4.2 for grouping |
| Hide permanently unconnected pins or stack supply pins | [S4.3–S4.6](klc/pins.md#s43) and the pin rules below | S4.6 shows hidden NC endpoints inside/on the outline |
| Choose symbol units or move power pins | [S3.8](klc/graphics.md#s38) | Separate power units belong to genuinely multi-unit symbols |
| Package a custom library or assign footprints | [Library fields](klc/library-fields.md) | S5.1–S5.2 and S6.2 illustrate fields and filters |
| A dedicated power symbol is missing | [S7.1](klc/library-fields.md#s71) | The image shows a special global power symbol, not an IC power pin |

Read the relevant text first. Open the specific local PNG through the host's
image viewer when evaluating its illustrated geometry; reading an image link
alone is not image inspection. Do not load every image for every schematic.
The text carries the requirements if image viewing is unavailable. Validate the
actual schematic with native renders; illustrative screenshots are not tests.

## Adopted rules and explicit adaptations

| Rules | Project application |
| --- | --- |
| G2.1 | Reuse stock generic symbols, particularly basic passives. Choose package, value, rating and sourcing fields on instances. An exact-part IC must map to the selected package. The official library's restricted list of generic libraries is not a restriction on project-local libraries. |
| S3.1–S3.3, S3.6 | Apply the origin/grid, field-size, outline/fill and pin-name-offset conventions to new custom symbols. Use the stated small/special-geometry exceptions when justified. Do not redraw verified stock primitives merely to normalize their geometry or an older style. |
| S3.4 | Keep internal functional drawings simple. Do not put a detailed block diagram inside a multifunction MCU. A central reference or special-function IC can justify a small explanatory interior; being the main IC is not by itself sufficient. |
| S3.5 with S4.6 | Visible, connectable pin endpoints stay outside the body. Permanently unconnected hidden pins are the explicit exception: put their endpoints inside/on the outline, away from other terminals. |
| S3.8 | Shared power pins of genuine multi-unit devices belong in a power unit. A single-unit IC retains its power pins on the same symbol. Separating ordinary bypass capacitors on the sheet does not justify splitting off its power pins. |
| S4.1–S4.2 | Use functional groups and the specified pin grid/length rules; retain unique physical identifiers and correct device functions. Preserve supply domains and mandatory strapping names. Library geometry is not permission to reorder electrical assignments. |
| S4.3 | Use native connected pin stacks for KiCad 10+. Never stack NC/DNC pins. Stack only pins that must share the same net; keep independently filtered domains, force/sense and other distinct roles separate. For an explicitly older target, a validated legacy representation is a version exception. For a KiCad 10 tool lacking native-stack support, use separate visible pins or another supported tool, not a silent legacy workaround. |
| S4.4, S4.7 | Match electrical types to real function and show active-low names clearly without double negation. Project pin aliases must retain the underlying datasheet identity. Do not make unrelated pins passive to obtain clean ERC. |
| S4.5–S4.6 | **Stricter project rule:** retain every physical pin identifier, even where KLC permits omission. Hide permanently unconnected pins individually with the proper type. Keep a pin visible if the datasheet requires bias/connection or its use is a circuit decision. A functional pin unused in this design keeps its real type and an instance no-connect flag. |
| S5.1–S5.2 | Distinguish a generic library definition from an instance's chosen footprint. Assigned footprints and filters must match the exact package. For schematic-only work, record unresolved footprints rather than inventing mappings or implying PCB readiness. |
| S6.2 | Preserve useful visible reference/value fields and hidden implementation metadata. **Project exception:** permit MPN, supplier, rating, tolerance, DNP and other useful BOM/verification fields. The official library's ban on custom fields and its librarian-approval process do not apply to project metadata. A passive instance's value is its component value, not the generic library symbol name. |
| S7.1 | Reuse standard power/GND symbols first. If a new power symbol is needed, use the correct semantics for the target KiCad version. A hidden ordinary IC power pin is not a substitute for an explicit supply connection. |

NC, DNC, NIC and internally connected pins are not interchangeable labels. Follow
the exact datasheet, not an abbreviation guess; hiding or stacking must preserve
both pin identity and the required electrical disposition.

## Outside this selection

KLC primarily governs reusable library assets. It does not replace our sheet
hierarchy, A3 default, left-to-right circuit presentation, local wiring versus
labels, near-side label anchors, decoupling ownership, or balanced block spacing.
Those remain in [drawing decisions](drawing-decisions.md). A standard-compliant
symbol can still be used in an unreadable or electrically wrong schematic.

Official-library submission procedures are not project requirements. In
particular, G1.8's current-stable-version requirement is excluded: target the
project's agreed KiCad version. G1.10's library embedded-file restriction is not
a blanket ban on project resources. Unselected symbol naming/package-variant
rules, footprint rules and 3D-model rules are not imported by implication. This
pack does not establish PCB footprint or fabrication compliance.

Treat the snapshot as pinned. To update it, review the upstream diff, per-asset
notices, and these exceptions; then refresh the source/output hashes and check
local links and illustrations. Preserve [attribution and license files](klc/NOTICE.md).
