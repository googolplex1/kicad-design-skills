# KiCad design skills

Agent instructions for readable schematics and practical PCB layouts, by
[googolplex1](https://github.com/googolplex1).

| Skill | Use |
| --- | --- |
| [kicad-schematic](kicad-schematic/SKILL.md) | Circuit architecture, component selection, schematic creation and symbol planning |
| [kicad-pcb](kicad-pcb/SKILL.md) | PCB placement, routing, layout cleanup and requested manufacturing outputs |

The schematic skill emphasizes functional hierarchy, visible local circuits,
recognizable symbols, clear label geometry and explicit decoupling ownership.
The PCB skill carries that intent through placement, routing and assembly.
Both use one project-level preference brief; preferences are established once
per project and retained through schematic and PCB work.

## Using the skills

Keep both complete skill folders together in your agent's skills directory;
they share references. They use the [Agent Skills format](https://agentskills.io/specification).
The `agents/openai.yaml` files provide optional OpenAI display metadata.

CAD creation requires separately installed KiCad and the supported editing and
validation tools. These folders provide guidance and a pin-map checker, not a
complete CAD engine. See [dependencies and current limitations](docs/dependencies.md),
including the unbundled creation extension. Clean-environment CAD execution
across agent hosts has not yet been tested.

## References

[Written schematic patterns](kicad-schematic/references/examples.md) explain
whole-circuit presentation. The [KLC applicability profile](kicad-schematic/references/klc-profile.md)
routes to 19 selected KiCad Library Conventions rules and their 20 illustrations
for offline use. Upstream rules and project exceptions are kept separate.

## License

Original instructions and helper code are licensed under [MIT](LICENSE).
Each skill folder includes its own copy of the license.

The imported KLC rules and illustrations are attributed to **KiCad Library
Conventions contributors** and included under **CC BY 3.0**. They retain their
separate [license, attribution and provenance](kicad-schematic/references/klc/NOTICE.md).
External tools and KiCad libraries retain their respective licenses.

## Helper checks

Run the bundled pin-map checker tests from this directory with Python 3:

```text
python -m unittest discover -s tests -v
```

These tests check the helper's comparison behavior; they do not validate a
complete schematic, PCB, or tool installation.
