# One preference brief per project

Establish this once before consequential part and package choices. Read the
request and existing project notes first. Ask only unanswered, relevant prompts
in a compact batch; if the answers are already known, ask nothing. Reuse the
brief through schematic, BOM, PCB and ordering work, including later chats on
the same project. Do not ask these questions for individual components.

The prompts are a menu to adapt, not a mandatory form. A small circuit or an
extension to an established board may need only one clarification. Accept
"no preference; recommend" and record the resulting delegation. Do not fill
silence with supposed user preferences or silently import another project's
package, supplier, cost, or assembly choices.

## Core prompts

| Topic | Optimized question |
| --- | --- |
| Assembly and mounting | How will the board be assembled: hand soldering, stencil/reflow, an assembly service, or a mix? Do you prefer SMD, through-hole, or a mix? |
| Passive packages | What is your preferred passive size and the smallest acceptable size? Is that minimum strict, or may smaller parts be used for justified exceptions? State the size convention. |
| IC packages | Which packages are acceptable: visible leads such as SOIC/TSSOP, leadless QFN/DFN/LGA, or BGA? Any pitch, exposed-pad, inspection, or rework limits? |
| Tradeoffs | Once electrical requirements are met, what should lead: total cost, small board size, easy assembly/rework, or fewer distinct BOM items? Name the main priority and any close second. |
| Quantity and cost | How many prototypes and likely later units? Is there a cost target, and does it cover components only or the assembled board including setup and shipping? |
| Fabrication and assembly service | Do you have a preferred PCB manufacturer and assembly service/process, or should I recommend one? Are any board or process constraints already fixed? |
| Sourcing | Any required suppliers, assembler parts catalog, existing stock to reuse, or lead-time/lifecycle constraints? Are qualified alternative parts welcome? |

Explain package notation only as needed: imperial 0603 is approximately
1.6 x 0.8 mm; metric 0603 denotes a different size. Store an unambiguous code
or dimensions. "Leaded" here means visible package leads, not solder chemistry.
QFN acceptance does not imply BGA acceptance. Assembly method can inform a
recommendation but does not establish a hard package limit by itself.

Separate the preferred passive size from a hard minimum. A larger, cheaper
qualified part may satisfy the brief; a blanket "all passives must be the same
size" rule does not follow from a preference for fewer distinct BOM items.
Verify actual costs at the relevant quantity rather than assuming a package
size is inherently cheapest. Do not hardcode a default size, distributor,
fabricator, or stencil specification from previous project feedback.

Ask the user for the intended service and constraints; research the service's
current capabilities yourself. A vendor name alone may not identify the stackup
or assembly process. Resolve detailed fabrication/stencil choices when they
affect the design or the requested release, not as trivia before drawing.

## Additional questions only when they change a decision

- **Development stage:** bench prototype, field trial, or product? Would an
  integrated development PCB or modules better serve this stage? Preserve the
  requested scope instead of either defaulting to breakout wiring or building
  a final product prematurely.
- **Mechanics and access:** fixed enclosure/outline, height, mounting points,
  connector positions, accessible programming/debug interfaces, measurement
  points, calibration access, or repair needs? Distinguish a size limit from
  a general wish for compactness.
- **Operating requirements:** environment, service life, input/power states,
  accuracy and bandwidth, or power budget still missing from the technical
  brief? Ask for the required result, then derive component specifications;
  do not ask the user to choose every resistor's tolerance.
- **System tradeoffs:** acceptable calibration or firmware work, removable
  storage versus soldered memory, or a particular sleep/wake behavior? Raise
  these only if they materially change the architecture, cost, or usability.

These supplement the technical requirements; package preferences cannot replace
an input-range or supply requirement. Defer questions that cannot yet affect a
choice, and do not send this entire list just because fields are blank.

## Persist and apply the answers

Keep a compact profile in existing project notes (create a small project note
if needed), with the source of consequential decisions. Use four distinctions:

- **Hard constraint:** must be satisfied; an unknown or conflicting constraint
  blocks the affected choice, not unrelated research or drawing work.
- **Preference and priority:** optimize within requirements. A preferred size
  is not a minimum, and a cost target is not automatically a strict ceiling.
- **Verified engineering fact:** supported by the exact device, package, or
  service documentation; research it rather than asking for a preference.
- **Delegated choice or provisional assumption:** identify which it is and
  the rationale. An assumption is not approval to violate a known constraint.

Make routine component decisions autonomously within this profile. Ask later
only for a material conflict, a consequential uncovered preference, or a changed
requirement. Give the concrete options, impact and recommendation in that
question. Batch related exceptions; do not turn a BOM review into one question
per part. If the user already delegated the tradeoff, act and record the reason.

For example, if a required IC is available only in a package excluded by the
brief, explain the conflict before committing to that implementation. An allowed
larger passive that meets the cost priority needs no new question. If a candidate
fails an electrical requirement, reject it or propose a system-level tradeoff;
do not treat an unsuitable part as acceptable merely because it is preferred.
