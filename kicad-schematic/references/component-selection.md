# Practical architecture and component selection

Apply the recorded [project brief](project-brief.md) throughout selection. Do
not reopen its questions for each component. Choose suitable parts within the
agreed priorities; escalate only meaningful conflicts or uncovered tradeoffs.

## Require a reason for added circuitry

Before adding a switch, isolation device, regulator, or support block, identify
the requirement it solves. Check whether an existing component function or
firmware-controlled state meets that requirement, including startup, shutdown,
fault and wake behavior where relevant. Software standby and true power removal
are different capabilities; compare them against the required result.

For switched supplies, examine every connected path, including independently
driven analog inputs, references, clocks and digital signals. Making MCU pins
inputs does not resolve another source driving an unpowered device. Establish
limits from exact-part documentation before adding or removing protection.

Compare a simple implementable architecture with more complex alternatives in
terms of the requirement, added BOM/firmware work, cost and remaining limitation.
Do not add hardware for a hypothetical requirement or remove required circuitry
to achieve a low part count. A development PCB can simplify bench work without
including the whole eventual product; choose its boundary from the brief.

## Quantify the concern before paying to solve it

Keep estimated operating loads, specified maxima, simultaneous load assumptions,
conversion losses and explicit design margin distinguishable. Trace a power
budget from loads to sources without silently applying the same margin twice.
Identify whether a bound is typical, worst-case, calculated, or measured.

Translate offset, temperature drift, noise, tolerance and reference errors into
the relevant input-referred or system measurement error under stated conditions.
Compare with the required accuracy, range and bandwidth before choosing a more
expensive part or extra circuitry. State what calibration can remove and what
remains. Do not equate ADC resolution with system accuracy or claim calculated
performance as a measurement.

## Select and consolidate by requirements

- Reuse qualified BOM items where their requirements overlap. Common value and
  package alone do not prove equivalence; consolidation can also over-specify
  inexpensive nodes. Compare actual cost and the project's assembly/sourcing
  priorities before standardizing.
- Keep a short table for selection-sensitive passives: references, circuit role,
  required characteristics and reason, selected part, and substitution limits.
  Group equivalent uses. Explain why a premium is needed; do not make every
  passive a precision part merely because the project contains a precision ADC.
- Distinguish an **exact MPN requirement** from a **specification requirement**.
  For the former, record the dependency that fixes the MPN; for the latter,
  assess alternatives against the relevant specifications and footprint.
- For capacitors, consider the requirements that actually matter at that node,
  such as effective capacitance at bias/temperature, tolerance, voltage rating,
  ESR/stability, leakage, dielectric behavior and physical fit. Nominal value
  alone is not a substitution check. Derive these requirements from the circuit
  and device documentation rather than prescribing one dielectric everywhere.
- Review cost outliers and repeated costs across the BOM. When the user flags a
  class of problems using examples, review the requested class (e.g. all
  capacitors), not just the listed references. User-proposed alternatives are
  candidates for evaluation unless explicitly established as qualified.

Avoid fixed price thresholds carried over from another project. Assess whether
an outlier is justified at this project's quantity and priorities. Compare a
cheaper credible candidate when a premium materially affects the board cost;
documentation convenience alone does not establish superior capability or
quality. Account for integration effort when it is a real project cost.

## Source exact orderable parts

Before committing a sourced BOM, verify exact manufacturer/orderable suffix,
package, lifecycle and availability using current manufacturer information and
the project's chosen suppliers. Record source/date, quantity and currency for cost or
stock claims. Use the intended region and purchase quantity; include minimum
order quantities, packaging, assembly setup and shipping when claiming total
cost. Stock at a different distributor or a different suffix is not proof that
the chosen item is purchasable through the project's sourcing route.

Missing search results alone do not prove EOL. Confirm status and distinguish
unavailable, obsolete, unverified and unsuitable. Recheck volatile availability
before ordering when ordering is in scope. For schematic-only work, provisional
choices may remain clearly marked; do not describe that as an order-ready BOM.

Record justified departures from soft preferences with the chosen part or in
existing project notes. Carry package/footprint assumptions and unresolved
sourcing choices forward so PCB work does not silently turn them into facts.
