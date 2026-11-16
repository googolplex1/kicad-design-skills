---
name: kicad-pcb
license: MIT
description: >-
  Create and refine KiCad PCB layouts using practical design preferences:
  functional placement, consistent widths within routed runs, direct routing,
  usable debug access, and concrete manufacturing checks. Use for schematic-to-PCB
  implementation, footprint placement, routing, board-wide layout cleanup, and
  requested fabrication or assembly outputs. For review-only requests use the
  KiCad analysis skill; for schematic creation use kicad-schematic.
---

# KiCad PCB design

Turn the project's circuit into a practical, buildable and debuggable board.
Apply these layout preferences within the actual electrical, mechanical and
assembly requirements. Scale the work to the requested stage: a development
board, a routing cleanup and a manufacturing release have different completion
criteria. Preserve existing design decisions outside the requested change.

## Use the existing tools

- `kicad-tool` owns structured schematic/PCB queries, edits, renders, netlists
  and checks. Read its current instructions before file operations; do not
  inspect or rewrite `.kicad_sch` / `.kicad_pcb` as raw text.
- `kicad-workflow` owns editing sequence, dry runs and validation baselines.
  Read it when modifying design files. Resolve approval requirements against
  the user's existing authorization and higher-priority instructions rather
  than adding a new checkpoint for each placement or routing operation.
- `kicad-schematic` owns circuit creation and schematic presentation. Use it
  when the task requires schematic changes, including a package/MPN change
  that must propagate through the project.
- `kicad` provides electrical/physical analysis for design review. Use its
  applicable review workflow when review is requested or needed; a bounded
  layout correction does not automatically become a full production audit.

Confirm the installed tool/version supports the operations needed for this
task, including board creation/synchronization or routing where applicable.
Follow the supported tool-extension/fallback workflow for missing operations;
do not invent commands or promise a routed board from an editing command's
name alone. On Windows, locate the installed tools rather than assuming macOS
paths. Check concrete compatibility consistently across KiCad versions.

## 1. Reuse the project brief

Read the existing project notes and schematic handoff before choosing packages,
stackup or fabrication settings. Reuse the one project-level brief through
schematic, BOM, PCB and ordering work. Do not repeat the preference interview
at the PCB stage or ask the same questions per component.

For unresolved preferences, use the shared [project brief](../kicad-schematic/references/project-brief.md)
reference directly; loading the whole schematic-creation workflow is unnecessary
for that purpose. Ask only missing, relevant questions. Record hard constraints,
soft priorities, sourced facts and provisional/delegated choices separately.
Later questions address new constraints or material conflicts, not routine
choices already covered by the brief.

Establish which constraints are fixed: board outline and height, mounting and
connector positions, layer stackup, intended fabrication/assembly service,
package/rework limits and required debug or calibration access. Research the
chosen service's current capabilities rather than asking the user to supply
every manufacturing limit. Do not infer a fixed layer count, supplier, passive
size or stencil specification from another project's example.

Read [completion checks](references/completion-checks.md) before implementation
and apply the relevant checks to the final saved board. A partial layout task
may leave unrelated work open, but must identify its scope and actual result.

## 2. Establish physical and electrical intent

For an existing board, capture the relevant baseline and inspect its outline,
stackup, rules, net assignments and locked/fixed placements. Retain them unless
the task requires changing them. For a new board, reconcile the schematic,
footprints and intended connectivity before treating imported parts as ready
to route. Do not erase unexplained schematic/PCB differences to make parity pass.

Reuse suitable library footprints before creating custom ones. Verify the exact
package, pad identities, orientation, dimensions and assembly needs; a matching
part-family name is insufficient. Resolve an incompatible package choice in the
shared project rather than silently substituting a footprint only on the PCB.
Carry forward selection-sensitive passive requirements and unverified choices.

Derive net classes, widths, clearances, via dimensions and any impedance or
length constraints from the actual electrical requirements and selected process.
Keep the source and assumptions with consequential limits. Manufacturer minimum
capabilities are limits, not a reason to use the smallest geometry everywhere.

## 3. Place for circuit operation and access

Start from fixed mechanics and the circuits whose placement most constrains
routing. Place by functional relationships and current/return paths rather than
copying schematic page coordinates. Keep the relevant device layout guidance
visible in decisions about converters, analog/reference paths, clocks and
interfaces. Reconsider placement when it creates avoidable routing detours.

Preserve bypass ownership and critical placement intent from the schematic:
capacitors drawn in a separate bank still serve specific ICs and supply pins.
Check their physical connection and return path. Preserve deliberate domain
boundaries; schematic grouping is not a directive to split a ground plane.

Provide usable programming, probing and ground access according to the brief,
including access after nearby connectors or components are fitted. Rail
disconnects, optional filters and extra test points need an identified purpose.
Prior requests to remove fuses or change unused-pin connections apply only to
their original project unless the current brief says otherwise.

When mechanical assets are required, find or create missing 3D models and track
their accuracy. Distinguish an approximate body model from verified clearance.
Review an early dense or critical placement at useful detail before repeating
the pattern across the board.

## 4. Route with consistent, purposeful geometry

- Keep width consistent where practical within a continuous routed run between
  meaningful endpoints, such as pads and vias. A run is not each individual
  KiCad line primitive, nor every branch of an entire net. Avoid arbitrary
  narrow inserts and unexplained width changes within the run.
- Genuine pad escape, current, impedance or clearance requirements can justify
  a transition. Make it deliberate, keep constrained sections no longer than
  necessary, and assess the effect on the connection's requirements.
- Remove unnecessary kinks, tiny detours and changes of direction. Use an
  obvious direct corridor when electrical and clearance constraints permit it;
  avoid 90-degree corners where practical. Preserve return paths and required
  pair geometry when simplifying a route.
- Treat a screenshot as an example of a defect class when the user requests
  board-wide cleanup. Review the entire requested board for similar patterns,
  rather than repairing only the highlighted trace. Keep a local request local.
- Measure route lengths along the routed path. Name the net and endpoints,
  identify the branch for branched nets, and state layer/via coverage. A total
  net copper length or pad-to-pad distance is not a path measurement. Mark an
  unavailable measurement as unverified rather than estimating from the view.

During geometry-only cleanup, preserve intended pad-to-net connectivity, domain
separation and constraints. Recheck taps, branches and the effect of moving or
replacing vias/tracks; nominally identical net names do not prove copper remains
connected. Electrical changes must be deliberate and reconciled with the
schematic, not hidden inside a cosmetic edit.

## 5. Validate and deliver the requested stage

Refill zones and validate the saved board using the supported workflow. Inspect
the current DRC and parity reports, including unconnected items and exclusions;
a successful process exit is not sufficient. Review both the whole board and
relevant detail on the affected layers, not just a 3D beauty view. Correct
defects within scope and give concrete dispositions for remaining findings.

When fabrication/assembly outputs are requested, regenerate affected outputs
after relevant CAD edits and review the generated package using the
[completion checks](references/completion-checks.md). Determine stencil details
from the selected assembly process; an earlier prototype's frameless stencil
or particular thickness is not a universal rule.

Separate tool failures from board findings. Record the operation/version and
diagnostic, use a supported alternative where possible, and state what could
not be checked. An assertion is neither an electrical defect nor a passed check.
Independent review tools or model choices follow the current request and
available workflow, not a previous project's review setup.

Deliver the editable board/project and necessary local libraries, plus requested
outputs, useful views, actual check results and unresolved limits. Distinguish
placement complete, routing complete and release checked; do not imply that
unperformed stages are complete. Preparing manufacturing files does not itself
place a fabrication order.
