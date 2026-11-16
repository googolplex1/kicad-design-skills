# Drawing decisions

## Sheet boundaries

Treat a sheet as a reader's answer to a functional question. The MCU's clock,
flash, boot/reset, debug, and ordinary connectors normally belong with the MCU.
They may form separate local blocks without becoming separate sheets.

Keep a simple AFE and ADC together when the uninterrupted analog path helps
explain conversion. Split when understanding one requires navigating unrelated
range controls, current and voltage paths, or dense supporting circuits. Put the
ADC's own input driver/filter, reference support, and clocks where their role is
clearest; do not split a feedback loop across sheets. Name and expose interfaces
at the chosen boundary.

Group supply generation on a Power sheet unless its complexity justifies more.
Consumer bypassing stays with the consumer's sheet. A regulator dedicated to an
analog block may stay there when it is essential to the block's explanation.
Avoid adding hierarchy levels simply to imitate a software folder structure.

At the root, place acquisition blocks in signal order and control/power in
supporting positions. Show major interfaces through sheet pins and connections;
use consistent rail/domain names. For a large design, an overview must reveal
how blocks cooperate as well as what pages exist.
Power relationships must identify the consumers as well as the rail sources.
Global power nets need not all become sheet pins: a concise rail-to-sheet table
or clearly identified supply inputs can make those relationships explicit.

## Direct wires or labels

Ask: would hiding this connection force a reader to reconstruct the circuit?
If yes, retain a direct wire when practical. Do not set a global wire/label ratio.

| Situation | Drawing default | Reason |
| --- | --- | --- |
| Op-amp feedback and gain network | Direct wires | Topology determines behavior |
| Input divider, filter, termination, reset pull-up/RC | Direct wires | Passives explain the node |
| Crystal and load components | Local direct connections | Keep the clock circuit recognizable |
| Mux → amplifier → ADC chain | Continuous direct path when readable | Preserve the signal story across local blocks |
| Separate reference buffers feeding several blocks | Named outputs and labels at consumers | Avoid unrelated crossing wires |
| Distant control/status or digital interface | Labels, grouped consistently | Avoid a wire maze |
| Nearby simple interface with a clean route | Direct wires are allowed | Labels are not mandatory at every block boundary |
| Already wired signal needing a useful name | Add a label without breaking the wire | Identification need not hide topology |

Use short, functional names such as `ADC_IN_P`, `ADC_IN_N`, and `REF_2V5_BUF`.
Keep polarity and active-low meaning consistent. Do not use generic `IN` or
`OUT` labels for unrelated nets on the same sheet. Repeated channels need clear
instance identity rather than accidental global connections.

A local net may have a label while retaining its direct wire. Do not replace
every component terminal with a label just because the generator makes that
easy. Read each amplifier, regulator, filter, and crystal circuit with the net
names mentally hidden: its functional topology should still be recognizable.
If a distant control needs a pull resistor at its consumer, draw the resistor
on that consumer's actual wire stub. One label may name the wired node; do not
join an adjacent resistor and IC pin through two overlapping labels.

Use local labels within a sheet, hierarchical labels with matching sheet pins
for explicit parent/child interfaces, and global labels only for intentionally
project-wide nets. Power symbols also make global connections. Preserve distinct
ground/rail names across isolation and filtering boundaries. Equal voltage does
not establish that two rails are one net. [KiCad label and power semantics][manual]

### Label geometry

Treat the electrical anchor and the visible text as different geometry. The
anchor must stay on the wire or pin connection point; move, rotate and justify
the label so its lettering occupies clear space. Never float the anchor off the
net merely to make the text look better.

- On a horizontal wire, keep local-label lettering above or otherwise clear of
  the line, not vertically centred on it. On a vertical wire, use an appropriate
  rotated label or a short horizontal branch when that reads better.
- At a terminal stub, choose the text direction and justification so the label
  extends into free space rather than back across the pin number, name or body.
  For global/hierarchical labels, the electrical anchor must face the arriving
  wire; the label body must extend away from that wire. If the label is left of
  an IC and the wire arrives from the right, its anchor belongs on the label's
  right edge. Rotate a left-anchored label 180 degrees. Mirror this arrangement
  for a label right of an IC; apply the same principle above/below a circuit.
  A symmetric outline can conceal which tip is the actual anchor: verify the
  electrical connection point, not just the nearest drawn tip.
- Keep enough stub length and spacing for the actual label extent. Remove
  redundant coincident or overlapping same-net labels after checking topology.
  If they substitute for a short local wire, draw that connection and retain
  only the useful annotation.

For a horizontal terminal connection (`o` is the electrical anchor):

```text
Label left of IC:   [ LABEL ]o--------[ IC ]
Label right of IC:  [ IC ]--------o[ LABEL ]
```

Keep the wire connected when rotating/repositioning the label and terminate it
at that anchor. Do not leave a wire traversing the label body to reach the far
edge. Verify the final geometry in a native render. This anchor-side error is
distinct from local-label text being vertically centred on a wire: correct the
former with orientation/routing and the latter with text justification. The
local-label justification fix does not repair a reversed global label.

## Flow and composition

Start with inputs on the left and outputs on the right. Put gain-setting and
feedback components where the circuit is recognized immediately. Keep related
differential branches aligned and polarity explicit. Route loops back naturally;
do not force each feedback segment to run left to right.

Place positive rails above their local circuit, ground below, and negative rails
downward where feasible. Power converters still read source → converter → load.
Bidirectional buses and unusual device functions may need another orientation;
choose the arrangement that preserves recognizable function.

Orient passives by circuit role: series elements usually follow the signal path;
shunt/filter/bypass capacitors and pull resistors usually branch toward the rail
or ground. In particular, draw a supply-to-ground bypass capacitor vertically
with the supply above and ground below, unless a different orientation clarifies
the local topology. Use dedicated power/GND symbols for ordinary supplies and
returns, preserving the intended domain names and scope. For ordinary grounded
capacitors and pull-downs, place the downward-facing GND symbol below the part;
do not put ground above it merely to match a generator's terminal order.

Use a consistent connection grid, orthogonal routing where practical, and space
between independent groups. Mark intended junctions clearly; avoid ambiguous
four-way crossings. Keep reference/value text off wires and symbols and avoid
shrinking text to fit an overcrowded sheet. Reconsider block placement or the
sheet boundary first.

Reserve the title block and page borders before placing circuitry. Check dense
details at readable zoom as well as the whole page: whitespace elsewhere does
not compensate for a cramped buffer, feedback loop or overlapping IC fields.
Use available page space to give the whole local circuit room; shrink excessive
symbol bodies, redistribute pins or move neighboring blocks before increasing
page size. Enlarge only the specific body or spacing that needs it. Keep useful
whitespace between groups rather than maximizing page occupancy.
Treat each label's anchor, orientation, and text extent as part of placement.
Place reference/value fields in clear space beside a vertical passive or above
a horizontal one; do not put them over its body or connection endpoints merely
because the generator applies the same offsets to every component.

Frames are optional visual grouping: thin, unobtrusive, named by function. Avoid
frames within frames unless the nested function is useful. A continuous analog
path can cross a frame; a frame is not an electrical or isolation boundary.

## Passives: classify by role, not part type

| Role | Schematic location |
| --- | --- |
| Gain/feedback resistor, divider, bias, termination | Inside its local circuit |
| Reset RC, crystal capacitor, anti-alias filter | Inside its local circuit |
| LDO input/output capacitors, SET/NR parts, compensation | Beside the regulator, directly wired |
| DC/DC inductor, feedback, bootstrap and loop capacitors | Inside the conversion stage |
| Reference output reservoir or buffer load capacitor | Keep visible with reference/buffer when it defines loading or response |
| Ordinary IC supply bypass capacitors | Separate, clearly assigned area on the same sheet |

A capacitor connected to a supply is not automatically presentation-only
decoupling. If its value, ESR, or node placement helps explain operation or
stability, keep it with the functional circuit.

### Remote decoupling must retain ownership

Group by IC and supply domain, not only by nominal voltage. Add short headers or
notes such as `U8 VDD pins 3, 8: C31/C32` and `U8 additional bulk: C33, 10 µF`.
The exact format is flexible; the association must be unambiguous. A multi-unit
IC's power unit can sit with its assigned bypass group. For many identical
groups, a compact allocation table may be clearer than repeated long notes.

Record which capacitors serve which supply-pin groups and which are shared bulk.
Do not draw a bank of capacitors that looks interchangeable when one belongs to
a specific IC. Repeat the applicable rail and ground symbols without apology.
For PCB handoff, include concise placement intent where needed: e.g. a capacitor
must serve a named supply pin, a Kelvin reference return, or a short converter
loop. Separation on the schematic is not permission for remote PCB placement.

Local bypass placement beside the IC is a valid exception when a small standalone
circuit or pin-specific requirement becomes clearer that way. Prefer the separate
area otherwise; make the reason for an exception apparent from the circuit or
a short note rather than applying one placement rule mechanically.

### Selecting values

For ordinary supply bypassing, prefer consistent 100 nF plus 1 µF groups
instead of unexplained exceptions. Apply this after checking the exact part:
some devices need a capacitor per supply pin, a dedicated internal-regulator
capacitor, different values, or a specific reference network. Do not replace
those requirements with one generic pair per package.

If an otherwise equivalent IC lacks the 1 µF and adding it is compatible with
the device and rail requirements, include it during creation. Do not speculate
about unavailable PCB space to justify omission. Record a real exception near
the affected group. Keep extra capacitance, dielectric, voltage-rating, effective
capacitance, or placement requirements explicit where they affect selection.

Do not extend that default to an op-amp output, reference output, LDO output, or
compensation pin. Added output capacitance can change amplifier stability;
regulator stability can depend on output capacitance and ESR. Consult the exact
device's current documentation rather than copying an old example's values.
[ADI amplifier loading][opamp] and [LDO stability][ldo] explain why these are
functional component choices. If evidence is missing, mark the value provisional.

## Notes that preserve design intent

Place useful equations and selection guidance beside the circuit they explain.
Prefer gain/range, cutoff, power dissipation, reference loading, and relevant
tolerance/temperature constraints over a wall of general commentary.

Distinguish derived results, simulation, measurements, and open work. A calculation
needs its assumptions and units; a simulation result needs its model/circuit and
conditions. Do not present a screenshot's number as a result for a new design.
Keep longer derivations and model files in the project and link/name them from
a concise schematic note. Component selection guidance should identify the
affected part(s), e.g. film dielectric for a specific filter, not all capacitors.

Do not inherit example notes about split grounds, star connections, dielectric
substitution, or ADC performance as general design rules. Re-establish the
electrical rationale for the new circuit and exact parts.

[manual]: https://docs.kicad.org/10.0/en/eeschema/eeschema.html#electrical-connections
[opamp]: https://www.analog.com/en/resources/analog-dialogue/articles/ask-the-applications-engineer-25.html
[ldo]: https://www.analog.com/en/resources/analog-dialogue/articles/low-dropout-regulators.html
