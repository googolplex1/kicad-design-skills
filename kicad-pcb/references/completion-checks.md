# PCB completion checks

Use checks proportional to the requested work and record pass, fail or not
checked with evidence from the saved design. A layout edit, complete board and
manufacturing release have different scope. Keep the record in existing project
notes rather than producing an unrelated audit package for a small correction.

## Layout and connectivity

| Check | Evidence and acceptance |
| --- | --- |
| Project fit | Outline, mounting, height, connector access, stackup and assembly choices match the recorded brief; material conflicts are resolved or explicitly open |
| Footprints | Exact package and pad mapping, orientation/pin 1, relevant dimensions and assembly requirements are checked; substitutions are reconciled with the schematic |
| Circuit intent | Critical placement, bypass ownership, current/return paths and domain boundaries are respected; expected pad/net membership and required separations remain intact |
| Routing | Required connections are routed for the claimed completion stage; widths within runs are consistent or justified; requested cleanup covers its whole stated scope |
| DRC and parity | Zones freshly refilled; current native report inspected for unconnected items, clearances and other configured rules; schematic/PCB differences accounted for; exclusions and remaining findings explained |
| Visual review | Whole-board and relevant layer/detail views inspected for detours, neckdowns, stray copper, placement conflicts, access and unreadable or obstructed markings |
| Mechanical/debug access | Required programming/probing points and ground access are usable; connector mating and enclosure checks have evidence; missing or approximate mechanical models are identified |

Preserve a baseline before structural changes to an existing board and account
for intended changes after editing. Existing findings may be outside a local
cleanup's scope, but are still relevant to a later release verdict. Do not
disable a rule or exclude a violation merely to obtain a clean report.

Check the resolved report path and freshness. The installed `kicad-tool` DRC
workflow refills and saves zones; treat it as a board mutation and inspect the
saved result. Confirm current behavior from the tool instructions/help rather
than assuming that any direct CLI invocation also refills zones. Read reported
findings even when the process exits successfully.

For a measured length, retain the endpoint/branch definition and measurement
method. For a claimed impedance, current capability, thermal result or mechanical
clearance, identify the calculation, source or measurement supporting it. DRC
checks only the configured rules; evaluate relevant performance constraints
separately and label unrun checks accurately.

## Manufacturing outputs, when requested

- Verify the actual fabricator/service, stackup and process constraints used
  for the design. Reuse existing answers; ask only about consequential gaps.
- Generate the requested copper, mask, silkscreen, outline and drill outputs
  from the final saved board. Inspect their layers, units, outline and holes
  for consistency with that board and the chosen process. Check plated and
  non-plated hole handling where applicable.
- For assembly, reconcile BOM and placement files by reference, exact part,
  footprint, board side and population/DNP status. Check origin/rotation
  conventions against the intended service rather than assuming an export's
  numerical conventions are accepted unchanged.
- For a stencil, verify intended paste layers and process/package requirements.
  Frame choice, thickness and aperture changes are project decisions. Do not
  reproduce an earlier prototype's stencil settings as defaults.
- Regenerate affected artifacts after any relevant CAD change and recheck them.
  Identify the source design revision and which output set was reviewed so
  stale files cannot be mistaken for the final release.

State concrete blockers, remaining engineering questions and checks not run.
Distinguish a generated output package from a checked release. A tooling error
needs its diagnostic and impact on confidence, not an invented board defect.
Fix work that remains feasible within scope before reporting completion.
