# Carry design intent into PCB work

Use [kicad-pcb](../../kicad-pcb/SKILL.md) for PCB placement, routing, layout
cleanup and requested manufacturing outputs. This handoff preserves schematic
intent; PCB-specific design preferences and completion checks live in that
skill. A schematic-only request does not require implementing a PCB.

## What to carry forward

- The same project-level brief, including assembly/package preferences,
  manufacturing choices, hard constraints and unresolved decisions. Do not
  repeat the interview at the PCB stage.
- Exact package/footprint choices and their verification status, including
  outstanding sourcing or pin-mapping questions.
- Selection-sensitive passive specifications, bypass ownership and critical
  placement/return-path requirements. A separated schematic capacitor bank
  does not imply interchangeable or remote placement on the board.
- Fixed mechanics and connector positions, required programming/debug access,
  and the intended completion stage: development board, layout or release.

Keep these in existing project notes rather than creating a second conflicting
brief. If layout exposes a circuit/package change, reconcile it with the
schematic and BOM and record the decision in that same project context.
