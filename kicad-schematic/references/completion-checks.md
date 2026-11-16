# Completion checks for schematic creation

Use these while building, not just as a disclaimer at delivery. Keep a compact
record in existing project notes: check, result, evidence, unresolved issue.
Separate pass, fail, and not checked. A successful export or clean ERC is only
one result. No numeric score or prescribed number of assertions replaces these
checks. Resolve correctable failures before calling the requested work complete.

## What must be demonstrated

| Check | Evidence needed | Failure that requires more work |
| --- | --- | --- |
| Project fit | One recorded project brief; selected architecture/packages respect hard constraints and apply the stated priorities; consequential exceptions are resolved | Silent package/process conflict, assumed preference presented as a requirement, unnecessary repeated preference questions |
| Requested circuit | Each requested function has connected circuitry and its required support, or an explicitly chosen module owns that support | Empty sheet, placeholder IC, missing power/reference/interface implementation |
| Package identity | Exact physical identifiers and functions match the sourced map; needed units are placed; native exports preserve pin mapping | Physical pins missing from the symbol/instance map (hiding is not omission), invented grouped identifiers, correct count with wrong numbers |
| Intended connectivity | Native exported nets match independently stated required connections **and separations**, including sheet boundaries | Wrong feedback, swapped interface, shorted domains, unconnected required pin hidden by a flag |
| Electrical prerequisites | Exact-part supply, support-component, logic-level and startup requirements are reconciled with the actual circuit | Known required circuit absent, operation depends on an enable/reset path that cannot work |
| ERC | Native hierarchy-wide report; disposition for each remaining finding and deliberate suppression | Unexplained errors, indiscriminate passive pin types or power flags used to conceal missing circuitry |
| Reading and layout | Final root and every sheet inspected at overview and readable detail scale | Unconnected overview boxes, hidden local topology, illegible pins/fields, missing bypass ownership |
| Delivery | Project and local libraries open with portable references; actual checks and remaining engineering limits are recorded | Claiming a concept is an implemented schematic, or claiming measured/validated performance without evidence |

The circuit-requirement check is proportional to the parts and requested scope,
not an unsolicited full production audit. For a powered mixed-signal prototype,
consider the actual supply sources and loads, input/common-mode limits, reference
network, level translation, boot/reset, clock, and data-path bandwidth. Check
power-off, startup and shutdown where they affect device limits or operation.
Distinguish a calculated or datasheet-based choice from a bench measurement still
needed. A warning note does not substitute for an implementable required circuit.

Footprints, firmware, PCB layout, simulations and hardware qualification may
remain outside a schematic-only brief. State their status without treating them
as either completed work or permission to omit schematic essentials.

When component selection is in scope, apply [component selection](component-selection.md):
justify added circuitry and cost-sensitive choices, distinguish exact-MPN from
specification requirements, and keep operating estimates, maxima and margins
separate. A sourced or order-ready BOM needs current evidence for exact variants
and availability; a provisional schematic BOM must identify what is unverified.
Carry the project brief and unresolved choices into any requested PCB handoff.

## Package identity check

Collect the expected map from the exact manufacturer's package/pin table before
or independently of generating the symbol. Include a source URL or local source
identifier with revision and table/page. Do not derive the expected map from the
schematic, generated inventory, or the same list used only as a drawing shortcut.
An extracted manufacturer table may be reused as a design input, but comparing
against it is not an independent audit of the extraction itself.

Example expected-map JSON (illustrative three-pin device):

```json
{
  "part": "ExamplePart-3",
  "package": "Example three-pin package",
  "source": "Manufacturer datasheet, Rev A, Table 2, page 4",
  "pins": [
    {"number": "1", "name": "VIN"},
    {"number": "2", "name": "GND"},
    {"number": "3", "name": "VOUT", "aliases": ["OUT"]}
  ]
}
```

Using actual absolute paths and the installed CLI:

```text
kicad-tool sch query lib-symbol <sheet.kicad_sch> <Library:Part> --format json
python <skill>/scripts/check_pinmap.py <expected.json> <query-result.json> --output <report.json>
```

Save the query's JSON output to `query-result.json`; it must contain `found: true`
and a `pins` array. Names are compared exactly except for explicit reviewed
aliases. Keep aliases about equivalent pin functions, not the intended net or
an operating voltage. Pin types and NC/DNC connection rules need their own
review: the helper deliberately does not infer these from a name.

The helper requires one record per physical identifier. If a supported native
stack is returned unexpanded, obtain its expanded identities using supported
tool/netlist operations. Do not reinterpret arbitrary slash-separated text as
a valid stack. Repeated records must be reconciled with the tool's handling of
common units or alternate graphics before running the check; never delete a
real pin just to make a duplicate report disappear.

This check proves agreement with the supplied map, not the map's authenticity,
completeness, correct pin types, footprint mapping, or electrical operation.
Cross-check the source table and exact variant. Then inspect native exported
pin-to-net membership, including hidden stacked pins and intentionally unused
pins. An intentionally unconnected pin may have no assigned net or net-member
entry, depending on export format: verify its identity in the full symbol/instance
map and its unconnected disposition in native export/ERC. Do not require it to
join a net just to satisfy a pin count. For schematic-only work, track
unassigned/unverified footprints separately.

## Connectivity independent of the generator

Derive a small set of meaningful expectations from device requirements and
circuit intent. Include required membership and forbidden merges: e.g. both
sides of a differential path, an op-amp feedback node, an internal regulator
output versus an external rail, and both ends of a cross-sheet interface.
Check the native exported netlist. Expectations copied automatically from the
same drawing recipe only test serialization and cannot expose a design omission.

For shared or stacked supply pins, reconcile physical pin groups with bypass
ownership. One visible supply pin must not erase required per-pin bypassing.
Read any firmware startup note against the actual enable, reset and translator
connections; ensure the stated controls can act in the states described.

Remove superseded drawing leftovers once their replacement is connected. A
no-connect marker explains an intentionally unused pin; it is not a substitute
for finishing or removing an abandoned resistor, capacitor or inductor. Retain
optional/DNP circuits only when their connections and purpose are explicit.

## Visual acceptance questions

Inspect the final saved output, not an earlier preview. For each sheet, identify
the region checked and any correction made; no screenshot collage is required.

- Can the root explain the main signal/control interfaces and which sheets
  consume the generated rails, without opening every child? Named boxes alone
  are insufficient.
- Can a reader recognize the analog path, feedback/filter networks, regulator
  energy and feedback paths, and crystal circuit without reconstructing a list
  of net names? Labels on a continuous wire are fine.
- Does each separated bypass group identify its IC and supply-pin group, with
  exceptional values visibly assigned?
- At readable detail scale, do labels, pin numbers, reference/value fields and
  notes remain distinct from unrelated wires, symbols and each other? Check the
  dense IC, power stage, connectors, and title-block area explicitly.
- Do label anchors remain connected while their lettering stays clear of wires,
  including left/right and vertical stubs? For outlined terminal labels, does
  the arriving wire meet the near-side electrical anchor without traversing the
  body? Check local-label text justification separately from anchor orientation.
- Are basic parts recognizable stock symbols or justified adaptations, with
  passives oriented by role and fields clear of their bodies and terminals?
  Are ordinary grounds dedicated symbols below the circuit, pointing downward?
- Does each local pull resistor join its IC node by a wire, without overlapping
  labels standing in for the connection? Inspect at least one vertical return
  as well as left/right signal labels.
- Are permanently unconnected pins individually hidden and unstacked, with
  their physical identities retained, without inflating the IC body?
- For new/adapted symbols, are the applicable [KLC rules and project exceptions](klc-profile.md)
  satisfied? Check simple functional interiors, endpoint positions, pin grid,
  fields, electrical types, units and target-version stack support. This is a
  selected-rule review, not certification of complete KLC compliance.
- Is A3 sufficient after sensible symbol sizing and block placement? Does the
  chosen page give every local circuit room and a clear reading order? A larger
  sheet or large blank area cannot excuse a cramped corner elsewhere.

Fix failures by repositioning, resizing or repartitioning the relevant circuit
and symbol. Recheck connectivity after moving pins or wires. An unavailable
collision scorer does not waive these visual checks.
