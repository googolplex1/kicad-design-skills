# Dependencies and compatibility

## Scope

The two design skills own design decisions and acceptance criteria. CAD access
uses external tooling. Install the complete supported dependency environment;
copying these instruction folders alone does not add drawing, routing or ERC/DRC
commands.

| Dependency | When needed | Source or requirement |
| --- | --- | --- |
| KiCad and `kicad-cli` | Native CAD validation, exports and rendering | Install the intended KiCad version and locate its actual CLI path |
| `kicad-tool` CLI and skill | Structured queries and changes to KiCad design files | [mash/kicad-skills](https://github.com/mash/kicad-skills); follow that project's installation instructions and dependency pins |
| `kicad-workflow` skill | CAD editing sequence and validation baselines | Same external project; use instructions compatible with the installed CLI |
| `kicad-sch-cleanup-loop` skill | A requested later schematic refinement pass | Same external project; normal creation still includes visual review |
| `kicad` analysis skill | Applicable design review | Separate integration; record the installed implementation/version before claiming review coverage |
| Python | The bundled `check_pinmap.py` helper | Standard library only; the helper was exercised with Python 3.13 |
| Image/PDF viewing capability | Inspection of native renders, and optional supplied examples | The agent environment must be able to inspect the exported views |

The external tool project's dependencies include its selected `kiutils` fork.
Do not independently replace a pinned dependency with a similarly named upstream
package. Check the external project's current installation instructions. No
third-party tool or dependency implementation is vendored in this extraction.
Selected third-party **documentation and illustrations** are bundled separately:
the [offline KLC pack](../kicad-schematic/references/klc/NOTICE.md) requires no
internet or website build tool. It supplies conventions, not CAD execution.

## Known development environment

The source development work used Windows, KiCad 10.0.7, Python 3.13 and
`mash/kicad-skills` revision `a74dbcb96d0fcd98aa597061ef89e4f1b1aec7b4`.
That environment also had a workspace creation extension exposing `sch build`
and `sch render-project`, with PyMuPDF for rendered page images.

That experimental extension is not bundled here and those command names must
not be assumed to exist in a stock installation. Before a creation task, inspect
actual capabilities for project/sheet creation, symbols, connections, rendering
and validation. Follow the supported tool-extension or fallback workflow for
missing capabilities and report concrete blockers. The package is not yet a
self-contained installer for reproducing the development environment.

## Platform boundaries

Use the host's supported shell and discover tools rather than hardcoding an
account path or assuming a macOS/Linux installation. An explicit `KICAD_CLI`
setting may be needed by the selected wrapper. Keep agent-specific UI metadata
separate from the shared design instructions.

| Claim | Current evidence |
| --- | --- |
| Standard skill folder/frontmatter structure | Both skills pass the local skill validator |
| Internal and cross-skill references | Checked with both skills installed as siblings |
| Bundled helper | Its existing unit tests are included; report their actual result when run |
| Codex / Claude Code skill discovery format | Supported by the respective official documentation linked in the root README |
| Clean-machine CAD execution of this extraction | Not yet tested |
| Equivalent behavior across models, hosts or OSes | Not established |

A public release should document a reproducible tooling route and a small
end-to-end smoke trial before advertising out-of-the-box CAD creation. The
image pilot and historical development results are not substitutes for that
installation check.
