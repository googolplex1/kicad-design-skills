# Symbols designed for circuit reading

For custom-symbol work, apply the [KLC profile](klc-profile.md) and its selected
offline rules. The profile separates project exceptions from upstream wording;
it also routes to the relevant local illustrations.

## Choose shape and pin groups before wiring

Search the installed libraries first. For basic parts, reuse conventional symbols
such as `Device:R`, `Device:C`, `Device:C_Polarized` and `Device:L` when available
and appropriate. Likewise prefer existing diode, transistor, switch, connector,
power and ground symbols. Choose the correct polarity/type and retain useful
stock graphics, pin-number visibility and field conventions. Different values,
ratings, MPNs or footprints normally belong on instances of the same symbol.

Do not redraw a resistor or capacitor, or put a familiar primitive in an IC box,
just to fit a generic symbol generator. An unchanged project-local copy of a
stock symbol is valid when portability or the tool requires it; retain its source
identity in the recipe or library metadata. A project-local library ID alone does
not imply a custom drawing. Reuse one definition for equivalent instances.

Budget for adapting or creating nontrivial IC symbols when that improves the
circuit. A part-number match alone does not guarantee a useful arrangement.
For a custom drawing, identify the specific missing symbol or readability/mapping
problem it solves. Keep this reason in existing design notes, not a new mandatory
document. Preserve standard primitives unless a real functional distinction
requires different graphics.

Sketch the intended role: incoming signals, outgoing signals, controls, reference,
power, and local feedback. Arrange pins to expose that role. Group related
interfaces together with spacing between unrelated groups. Power inputs normally
go above, returns below, signals left/right; a regulator normally has input left
and output right. These choices also align with [KiCad functional grouping][groups].
Physical package pin order is for mapping verification, not the default layout.

Prefer:

- Triangular op-amps with legible `+` and `−` inputs. A dual/quad package normally
  uses separate amplifier units with shared power in a power unit. For a
  single-unit IC, keep its power pins on that same symbol ([S3.8](klc/graphics.md#s38)).
- A converter-style ADC outline when it clarifies analog-to-digital flow. Keep
  analog inputs together, digital interfaces legible, and references distinct
  from supply pins. A verified rectangular symbol remains usable when adequate.
- A small internal functional diagram only when it explains an important device.
  A central precision reference may justify more detail than a support IC.
  Keep it simple; do not add functional diagrams for multifunction MCUs
  ([S3.4](klc/graphics.md#s34)). The drawing is explanatory, not a transistor-level
  or simulation model.

Do not alter pin numbers to get convenient positions. Distinguish moving an MCU
pin on paper from changing its peripheral assignment; the latter changes the
electrical/firmware design and needs supporting device evidence.

## Unused pins need coverage, not drawing space

Retain every physical identifier in the symbol and package map without giving
each one a visible terminal. For pins that must remain unconnected, normally
use hidden pins with the `Not Connected` / `Unconnected` electrical type. Place
their endpoints within the body, away from functional connection points; they
must not determine the body size. This follows [KiCad hidden-pin conventions][hidden].

Establish the disposition from the exact datasheet. NC, DNC, NIC and internally
tied pins are not interchangeable: NIC commonly means *not internally connected*.
Keep pins visible when they need an external connection, strap, test access or
an explicit design choice. A functional pin unused only in this circuit keeps
its actual type and an instance no-connect flag; do not retype it as permanently
unconnected to suppress ERC.

Do not stack permanently unconnected pins. KLC S4.3 prohibits NC stacks even if
a KiCad version supports an unconnected stack representation. Hide these pins
individually while preserving identifiers and verifying native export/ERC.
After hiding or grouping pins, resize the body and recompose the surrounding
circuit; an empty oversized rectangle still fails the readability objective.

## Pin stacking is an electrical decision

For an electrically joined stack, use only pins required to share the same net and
whose individual roles remain clear. Matching names or voltage is insufficient.
Keep independently filtered domains, force/sense pairs, Kelvin returns, and pins
with distinct placement requirements separate when stacking would hide that
distinction. Never stack NC/DNC pins as if they were a connected group. Verify
an exposed pad's required connection separately; do not infer it from its shape.

For KiCad 10+, use native pin stacks when stacking is appropriate and downstream
tools support them. If the tool cannot preserve native stacks, keep the pins
separately visible or use another supported tool. For an explicitly older target,
validated coincident physical pin records are a version exception; retain a
meaningful visible electrical type and use passive hidden members as appropriate.
Hidden power-input pins create implicit global connections. Verify every
represented pin in the exported netlist. The [offline stacking rule][klc-stacks]
and [project version exception](klc-profile.md) govern this choice; the
[KiCad pin-stack manual][stacks] is optional implementation detail.

Do not suppress ERC by making all unrelated pins passive. Preserve the actual
function and direction of each interface. A deliberate stack representation must
still expose the relevant electrical check.

## Verify and package a custom symbol

Use the manufacturer's documentation for the exact part and package variant.
Keep a pin map with physical number, name/function, electrical type, symbol unit,
and stack membership where applicable. Check total pin coverage, NC/DNC handling,
power pins, exposed pads, and footprint pad numbering. Mark missing evidence;
do not represent a graphic-only draft as a verified production symbol.

Compare exact identifiers, not just their count: replacing pin `12` with `13`
can preserve a count while breaking the design. Reconcile every supply, ground,
reserved, NC/DNC, and exposed-pad identifier. An incomplete source table is a
research gap to resolve, not permission to omit inconvenient pins. Reduced
graphic-only symbols belong in explicitly requested block diagrams, not in a
completed schematic. Do not use composite text such as `C6/C7` or `GND balls`
as a physical pin number; use a supported stack that exports real pin identities.

Use [check_pinmap.py](../scripts/check_pinmap.py) to compare a sourced expected
pin map with a complete `kicad-tool sch query lib-symbol ... --format json`
result. Query the full embedded library symbol, not just one placed unit. The
helper accepts flattened physical records, reports missing/unexpected numbers,
name mismatches and duplicate records, and returns nonzero on a mismatch. See
[completion checks](completion-checks.md#package-identity-check) for its input
format and limits, including intentionally unconnected pins. Also confirm intended
units are placed and native exports preserve their pin mapping; a complete library
alone cannot establish instance completeness or connectivity.

Store new/adapted symbols in a project-local `.kicad_sym` library and register it
through the project library table with portable paths such as `${KIPRJMOD}`.
Keep the library definition and schematic's embedded symbol consistent. Preserve
the original library ID/source when useful for traceability, but give a materially
adapted symbol its own project ID so standard-library updates do not replace it.

Pin redistribution may be needed after placement. Before updating an existing
symbol, capture its instance pin-to-net map. Update affected instances and rewire
to the moved connection points. Then compare intended connectivity across all
affected units and instances, check the pin/footprint mapping, and render the
result. Verify gains/feedback polarity separately; ERC cannot prove them.

Use version-compatible symbol validation and whole-project ERC/netlist export.
If a parser or writer cannot round-trip native stacks or custom graphics, use
a supported representation/tool route and disclose the limitation. Do not
silently drop pins, flatten unlike domains, or fake a stack with a text label.

[groups]: klc/pins.md#s42
[stacks]: https://docs.kicad.org/10.0/en/eeschema/eeschema.html#pin-stacks
[klc-stacks]: klc/pins.md#s43
[hidden]: klc/pins.md#s46
