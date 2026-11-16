# Illustrative schematic patterns

These written patterns illustrate presentation choices. They are not verified
reference circuits: establish the applicability of parts, numerical values,
ground strategies and capacitor selections for the actual design. The skill's
text is the working specification; no original screenshots are required.

For normative symbol examples, use the separately attributed [offline KLC
selection](klc-profile.md). Its illustrations explain individual library rules;
these written patterns explain whole-circuit and sheet presentation.

## 1. Continuous analog chain

Two input muxes feed op-amp stages and a converter. Direct wiring makes the main
path and feedback recognizable. Separate reference buffers feed named nets;
notes sit near the circuitry they explain. Ordinary bypassing and amplifier
power units are below the main path. The converter outline communicates role.

Apply: preserve the main analog story even when it crosses local block boundaries.
Keep the reset pull-up/filter near the ADC because it explains behavior.
Refine: identify the owner of every remote bypass group. Do not adopt the
buffer output loading or numerical annotations without checking the new circuit.

## 2. Power generation

Several regulator stages share a sheet. Input filtering, input/output capacitors,
SET networks, and associated resistors are directly wired beside each regulator.
This is the exception to treating supply-connected capacitors as a remote bank:
these components define the local circuit.

Apply: preserve source-to-regulator-to-output flow and keep regulator support
components visible. The exact row spacing and long branches are not templates
that every power sheet must reproduce.

## 3. Functional frames and supporting notes

A reference path, analog input stages, ADC/interface, temperature paths, and
decoupling are separated by named frames. Op-amp shapes and wired gain networks
remain recognizable inside them.

Apply: named frames can help when a sheet contains several local functions.
At greater complexity, move independent functions into separate sheets instead
of continuing to shrink text or add nested frames. The old ground-connection
and capacitor notes are not general rules.

## 4. Parallel signal paths and calculation notes

Voltage and current front ends read left to right, with calculations and range
notes close to the relevant stages. Optional reference circuitry, power, and
ordinary bypassing occupy separate regions.

Apply: organize by function, keep useful rationale local, and distinguish optional
features clearly. A drawn isolation line does not verify electrical isolation;
estimates and open simulation questions are not validated results.

## 5. Central precision-reference symbol

A detailed ADR1001 symbol makes the central reference function visible, with
buffer stages wired beside it. Regulator, sensors/EEPROM, and connectors occupy
their own groups; ordinary bypass parts sit separately.

Apply: a central device can justify a richer functional symbol, while supporting
parts stay simpler. This level of detail is optional, not a requirement to copy
every datasheet block diagram into a symbol. Apply KLC S3.4: keep functional
interiors simple and omit them for multifunction MCUs. Keep pin mapping and
the external circuit legible, and assign remote capacitors to their intended ICs.
