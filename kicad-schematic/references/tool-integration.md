# Tool integration

This skill owns schematic architecture and drawing decisions. It does not supply
a KiCad file generator or replace the installed editing/validation tools.

## Existing skill boundaries

- `kicad-tool` owns structured `.kicad_sch` / `.kicad_pcb` query, edit, render,
  netlist, and validation operations. Read its current instructions before use.
- `kicad-workflow` owns functional editing, dry runs, and structural baselines.
  Use it when modifying design files. Resolve workflow/approval instructions
  against the user's actual request and higher-priority session instructions;
  do not add an approval checkpoint just for presenting a sheet map.
- `kicad-sch-cleanup-loop` is for a requested later visual refinement pass.
  Readability during creation remains this skill's responsibility. Its layout
  score is diagnostic, not a reason to remove meaningful analog wires or labels.
- `kicad` supplies design-analysis methods when electrical review is needed.
  Loading this creation skill does not require an unrelated full PCB audit.

Do not modify these installed skills as a side effect of using this one. If a
dependency is unavailable, report the specific missing capability and use an
available supported route within the user's scope. Do not promise a complete
schematic solely because a style guide exists.

## Check capabilities before committing to execution

Locate `kicad-tool` and `kicad-cli`, then confirm versions and actual command help.
Use the dependency's supported bootstrap if needed. On Windows, use
`Get-Command` and check installed KiCad directories rather than assuming a macOS
CLI path. Use `KICAD_CLI` for an explicit CLI path if the wrapper requires it.
Do not silently upgrade the user's project format to the newest installed version.

For creation, establish support for the operations actually required:

- Creating a project and empty root schematic.
- Creating/linking child sheets, sheet pins, and hierarchical labels.
- Importing/placing symbols and setting values/properties/footprints.
- Creating or reshaping custom symbols, units, and any pin-stack representation.
- Adding wires, junctions, notes, frames, labels, and power symbols.
- Exporting whole-project nets/ERC and rendering the edited sheets.

The presence of `sch edit symbol add` does not establish support for new projects,
sheet creation, drawing custom bodies, or moving library pins. Never invent a
`create`, `sheet add`, or similar subcommand from its apparent naming pattern.
Check current help. If the required command is missing, follow the installed
tool workflow for extending it or another explicitly supported route. Keep a
capability gap separate from a design uncertainty; complete unaffected planning
without claiming requested KiCad artifacts exist.

## Validation that supports the drawing

Where supported, these existing wrapper patterns are useful; confirm current help
and replace placeholders with actual project paths:

```text
kicad-tool sch validate <top> --sheet <child>
kicad-tool sch validate <top> --save-baseline <baseline-dir>
kicad-tool sch validate <top> --sheet <child> --baseline <baseline-dir>
kicad-tool sch render-region <child> <X1,Y1,X2,Y2> --output <image-path>
```

Run hierarchy-wide ERC/netlists from the root and inspect each edited sheet.
Before deleting/replacing a wire, enumerate all taps, including mid-span pins,
junctions, labels, and branch endpoints. A clean ERC count alone can miss a lost
connection. Compare net membership, not just net counts or automatically assigned
names. Check both unintended disconnections and unintended net merges.

For a new design, define critical intended connections from the design brief
and verified pin maps before checking the exported netlist. Include interface
polarity, feedback, supply/reference domains, and sheet boundaries. Use justified
no-connect markers and power-source declarations; do not mask unexplained errors.

Render the root and every created/changed sheet. Inspect complete-sheet reading
order plus detail around dense circuitry, feedback loops, and custom symbols.
If rendering or validation cannot run, deliver the actual available artifacts
with the limitation, rather than reporting checks as passed.

If an automated inspector stalls, bound its run and use an available native
render for the visual check; do not repeatedly wait on the same failing route.
Record the unavailable score separately from whether the pages were inspected.
The [pin-map helper](../scripts/check_pinmap.py) reads structured query JSON and
a separately sourced expected map, never schematic text. Generator manifests
and pin inventories describe what was generated; by themselves they cannot
establish which pins or circuits should have existed.
