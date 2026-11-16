---
name: kicad-schematic
license: MIT for original material; KLC references retain CC-BY-3.0 (see references/klc/NOTICE.md)
description: >-
  Create or extend KiCad schematics using a circuit-first drawing style:
  functional sheet hierarchy, readable wired signal paths, labeled local blocks,
  explicit decoupling ownership, and symbols arranged for their circuit role.
  Use for schematic creation, architecture, component selection, and custom-symbol
  planning. For existing-sheet cosmetic cleanup or design review alone, use the dedicated
  KiCad cleanup or analysis skill instead. Multi-board implementation is out of scope.
---

# KiCad schematic creation

Make circuit intent understandable at three scales: project overview, sheet,
and local circuit. Optimize for finding and understanding a function quickly,
not minimum wire length, minimum sheet count, or a layout score alone.

These are the default drawing conventions for new work. Explicit project requirements override
stylistic preferences; electrical requirements constrain implementation. Extend
an existing project without silently restyling unrelated sheets.

## Read what the task needs

- Read [drawing decisions](references/drawing-decisions.md) for sheet planning,
  connections, passives, and annotation.
- Read [symbol design](references/symbol-design.md) before selecting or changing
  a nontrivial IC symbol. Symbol design is an expected part of creation.
- For custom-symbol work, read the [KLC applicability profile](references/klc-profile.md)
  and its task-relevant offline rules. Selected upstream text and illustrations
  are bundled with attribution; project exceptions are kept in the profile.
- The text instructions are sufficient to apply this style. Consult the
  [illustrative patterns](references/examples.md) when examples would clarify
  a drawing decision. Supplied visual references are optional supplements;
  treat them as presentation examples and verify electrical choices separately.
  Do not depend on access to an earlier conversation.
- Read [tool integration](references/tool-integration.md) before file operations.
  It defines the boundary with the installed KiCad skills and capability checks.
- Read [completion checks](references/completion-checks.md) before building a
  new design and use them on the final saved project.

## 1. Establish the design boundary

Extract known functions, interfaces, rails, critical performance requirements,
parts/package variants, and intended KiCad version from the request and project.
Establish one project-level preference brief using [project brief](references/project-brief.md)
before consequential component selection. Reuse answers already in the request
or project; ask the remaining relevant questions together, once per project,
not per component or again at the PCB stage. Record hard constraints separately
from preferences and delegated choices. Continue independent work while answers
are pending; do not silently turn assumptions into user requirements.

Use [component selection](references/component-selection.md) when choosing the
architecture or BOM. Meet the actual requirement with proportionate circuitry,
then optimize within the project's priorities. Check existing device functions
before adding hardware. Later questions are for consequential exceptions or new
requirements that the brief does not cover, not routine choices within it.

State consequential implementation choices, such as a bare MCU versus a module,
input range, gain, and acquisition/streaming mode. A module containing the named
IC can satisfy an open brief; do not silently substitute one when chip-level
support circuitry was requested. For each new nontrivial IC, derive its required
supplies, external circuits, pin dispositions, and startup constraints from the
exact part documentation before placing it. Keep those requirements independent
of the drawing or generator recipe so omissions can be detected later.

Look for evidence of separate physical boards: remote sensor heads, independent
mounting/enclosures, replaceable modules, or explicit board-to-board connectors.
Notify the user with the evidence and candidate boundary if multiple projects
appear appropriate. Complexity or galvanic isolation alone does not establish
that need; a remote head might be passive and need no PCB. Continue architecture
work independent of the unresolved boundary. If multiple boards are confirmed,
summarize their functions and connector/interface boundary, then hand off the
multi-board implementation. Do not create separate projects or silently choose
one board to implement. This skill can create a selected board's schematic once
the user's request establishes which board is in scope.

## 2. Plan sheets before placing parts

For a multi-sheet design, make the root an understandable system overview with
functional sheet names, major signal links, and power relationships. Do not make
it merely a row of unexplained page boxes. A small circuit can remain one sheet.
When acquisition, digital support, and supply generation each form a substantial
circuit, prefer separate functional sheets. If keeping them together, check that
each function is immediately locatable and its local circuits remain readable;
fitting everything on a large page is not by itself a reason to avoid hierarchy.

Default new sheets to A3 landscape. A smaller sheet is suitable for a genuinely
small circuit; use A2 or larger only when a coherent circuit needs the space
after sensible symbol sizing and block placement. Do not enlarge the page to
accommodate oversized symbols or leave one local circuit cramped in a corner.

Write a compact sheet map, preferably as a table, with each sheet's purpose,
owned circuitry, and interfaces. The map can live in the response or existing
project notes; it is not an extra mandatory planning artifact or approval gate.

Typical starting partition:

- **Microcontroller:** MCU, flash, crystal, reset/boot, USB, SWD, and associated
  decoupling. Keep support circuits where a reader would look for them.
- **ADC and analog front end:** combine when the conversion chain reads easily
  as one circuit; split **Analog front end** from **ADC** when range switching,
  current paths, or independent analog functions obscure that story.
- **Power:** supply generation and its regulation/filtering circuits. Multiple
  modest LDOs or converters normally belong together.

These are examples, not compulsory pages. Prefer function and reader navigation
over one sheet per IC, an arbitrary component count, or premature fragmentation.

## 3. Compose the circuit, then its connections

For each sheet, identify the main path and support blocks. Reserve space for
functional passives, readable fields, notes, and the decoupling area.

- Main signal flow runs left to right. Positive rails generally sit above the
  circuit; ground and negative rails below. Feedback and bidirectional links
  are natural exceptions, not reasons to distort topology.
- Wire a local functional circuit directly. Keep amplifier feedback, filters,
  dividers, crystal networks, and reset conditioning visible.
- Usually connect separate local blocks by meaningful labels. Preserve a
  continuous wired analog path across blocks when it explains the transfer
  function more clearly, including mux → amplifier → filter → ADC.
- Place each label's electrical anchor on the intended net while keeping its
  lettering clear of the wire and pin fields. At a terminal stub, face the anchor
  toward the arriving wire and extend the label body away from it. Rotate a
  reversed label rather than routing the wire through its body to the far anchor.
  Check local-text justification separately.
- Normally put ordinary supply bypass capacitors in an organized area on the same sheet,
  with explicit IC/supply-pin ownership. Keep regulator, filter, compensation,
  and other function-defining capacitors within their circuits.
- Use dedicated power/GND symbols for ordinary rails and returns, with ground
  below and pointing downward. Repeat them where useful; boxed GND labels and
  long rail wires are not substitutes for the standard symbol.
- Use whitespace and optional unobtrusive named frames to separate blocks.
  Neither a frame nor a label should conceal the signal path.

For ordinary supply bypassing, prefer a consistent 100 nF plus 1 µF pattern
where the part's requirements and rail loading permit it. This is a conditional
starting preference, not a universal component prescription. Check exact-part
requirements before adding or standardizing values. Keep exceptional values,
such as an additional 10 µF for one IC, visibly assigned to their owner.

## 4. Design symbols for the drawing

Start with installed library symbols, especially for basic passives, connectors,
switches, and power/GND symbols. Reuse their conventional graphics and put values,
ratings, MPNs and footprints on instances; those differences do not require new
drawings. Inspect candidates in their intended circuit before routing around them.
Customize or create a symbol when none is correct or its pin grouping, units, or
shape obstructs understanding, not merely because custom generation is easier.
Do not use package pin order as the default visual arrangement.

Use triangular op-amps. Prefer a recognizable converter outline for ADCs when
it helps. Consider a simplified functional interior for a central complex part
such as a precision reference, without obscuring external connections.
Keep that interior simple; do not add functional diagrams inside multifunction
MCUs. Follow the selected KLC graphics and pin conventions through the profile.

Keep pin numbers, package mapping, electrical types, and supply-domain identity
correct while changing graphics or pin positions. Physical pin coverage does
not require every pin to be visible: normally hide pins that must remain
unconnected, retaining their identifiers and correct unconnected type as
described in the symbol reference. Electrically joined stacks need a justified
common net; permanently unconnected pins remain individually hidden and unstacked.
Use representations
supported by the target KiCad/tool versions. Revalidate connected
instances after a symbol change; moving a pin can disconnect an unchanged wire.

Before routing a custom IC, compare its complete physical pin identifiers and
functions against the independently collected package pin map. A total count
alone is insufficient. The symbol definition must represent every real pin,
including hidden pins; names such as `GND balls` are not physical pin numbers. A graphic-only placeholder
does not satisfy a request for a connected schematic. See the symbol reference
for the repeatable check.

## 5. Create and validate in manageable increments

Use supported structured tools and the existing functional-editing workflow;
do not invent commands for missing creation/hierarchy/symbol capabilities.
Make functional correctness and readability part of creation. A later cleanup
pass is optional refinement, not permission to deliver an unreadable first draft.
Render one representative dense IC and one local functional circuit early,
before repeating their placement or label pattern across the design. This catches
systematic collisions and label-only circuits while they are cheap to correct.

For existing circuitry, capture a connectivity baseline before structural work.
For new circuitry, validate against a small explicit list of intended connections
and domains; an empty baseline cannot establish that the new design is correct.

After each meaningful circuit or sheet:

1. Check connectivity and ERC from the project root, including cross-sheet
   interfaces, intended power domains, unused pins, and all symbol units.
2. Verify critical pin-to-pin connections and symbol-to-package mapping. For
   visual changes, require connectivity equivalence; for electrical changes,
   account for intended additions/removals as well as accidental merges.
3. Render and inspect the overview and relevant detail at a readable scale.
   Correct collisions, ambiguous junctions, broken visual paths, and missing
   decoupling ownership. A score or successful export is not a visual review.
4. Record actual checks and unresolved requirements. Never claim ERC, simulation,
   device suitability, or PCB placement has been verified when it has not.

Use the final saved files for the final checks. An unavailable layout scorer does
not prevent inspection of a native render. Fix visible defects found during that
inspection; merely listing them in a README does not complete the drawing work.

## Completion criteria

A reader can find the MCU clock without searching every sheet; understand an
amplifier's gain path without chasing labels; trace the ADC input chain; locate
each IC's bypass parts and special requirements; and identify every sheet's
purpose from the root. Components, notes, and symbols support that reading order.

Apply the separate package, connectivity, circuit-requirement, and visual checks
in [completion checks](references/completion-checks.md). Clean ERC cannot replace
any of them. Mark failed or unrun checks accurately and continue work that is
possible within the requested scope. Do not stop at a concept while requested
circuit implementation remains feasible. Bench measurements, firmware, and PCB
release checks remain separate when they were not requested.

Deliver the editable project and custom libraries when creation was requested,
plus useful rendered views and a concise validation summary. If only planning
was requested, deliver the sheet map and design decisions without inventing a
completed project. Report actual tool gaps explicitly rather than silently
substituting a plan for a requested schematic.

Carry the same project brief and component decisions into PCB work. When PCB
implementation is requested, use [kicad-pcb](../kicad-pcb/SKILL.md). The
[PCB handoff](references/pcb-handoff.md) identifies the schematic intent to carry
forward; PCB placement, routing and release guidance belong to that separate
skill. This does not expand a schematic-only request into a PCB release.
