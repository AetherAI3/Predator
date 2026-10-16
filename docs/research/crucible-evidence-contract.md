# Crucible: execution and evidence contract

[← Crucible overview](../../README.md#crucible-adaptive-quantum-threat-modeling) · [Research roadmap](generations.md)

The lockpick in the README illustrates a research loop. A drawing of four pins is not a receipt for four dispatched workers, four native checks, or a quantum-hardware run. Each case should name the path that actually ran and the evidence it produced.

| Path | What it can establish | What still needs proof |
| :--- | :--- | :--- |
| **Manual research** | A source-backed hypothesis, candidate graph, or analyst-defined QUBO. | Provider dispatch, native behavior, and finding status unless separately recorded. |
| **CFC selector** | An admitted fanout can collect worker receipts, compile a bounded search problem, and select candidates. The current selector can use a classical minimum; other methods need their own receipts. | Its selection alone runs no native test and mints no vulnerability verdict. The independent native gate must be cited. |
| **Exploit ratchet** | A signed run can bind source and target observations, a revised artifact, provider usage, native outcome, optional typed JEV packet, and paired repair record across attempts. | A candidate is not a verified finding until independently reproduced and challenged. A repair proposal is not a validated fix. |
| **Simulation or hardware study** | A recorded solver, circuit, device or simulator, shots, output, and comparison for a specific workload. | Quantum advantage requires matched alternatives, resource accounting, uncertainty, and independent replication. |

## What a banked result means

1. **Pin the question.** Record scope, source revision and regular-file hashes, target observations, acceptance checks, and the owner-approved limit for that run. Preserve the parent checkpoint.
2. **Separate facts from choices.** Target facts come from source or test evidence; an optimizer cannot change them to make an exploit work. Candidate bits and QUBO coefficients describe test choices. Their energy is a model value, not probability, severity, or impact.
3. **Record the method.** Name the model routes, worker receipts, solver, and selected candidate. `C` and `Q` labels identify lineage and depth; they do not by themselves prove provider calls, quantum circuits, or native execution. A JEV adapter, enable flag, or offline preflight likewise does not prove a JEV call: cite a qualified deployed stage's typed field, call count, and settled spend when JEV participated. `NOT_CONFIGURED` means it did not.
4. **Run the decisive check.** Save the native receipt with the shipped product version and build, operating system, relevant trust and sandbox settings, trigger actions, observed effect, controls, and negative results. If a protection cannot start, that run is inconclusive about bypassing a working protection. A miss stays a miss. An inconclusive result is not a HIT, and a HIT on synthetic owner data is not a deployed victim impact.
5. **Carry and repair.** Bank the attack observation with a linked repair hypothesis and regression plan. Test the fix separately. Preserve earlier passing obligations and contrary evidence when continuing to a later checkpoint.

## Minimum record for each candidate pin

Before a native check, freeze the parent checkpoint digest, source revision, owned fixture, proposed path, and observables that would confirm and falsify it. Record the selected method and solver receipt separately from the software result. A candidate record should then carry the exact native action, outcome, receipt hash, paired control, and remaining obligation into its lane-local checkpoint. Mark a failed check **REJECT** and an unrun or ambiguous check **inconclusive**, with the reason; do not reuse either as a HIT because a model suggested the same path later. Choose the next distinct candidate from the banked outcomes and open obligations.

An impact claim needs its own observed effect. For example, a zero-click claim requires a native trace showing the trigger and consequence without a user action after the lower-trust input arrived. An automatically scheduled task, an agent suggestion, or a source path that could run is only a candidate until that trace exists. Keep synthetic owner-controlled tests separate from any claim about real victims or deployed services.

The [chain catalog](../../README.md#mitre-attck-chain-library) contains source definitions and unmodeled profile slots as well as a small set of evidence-linked energy examples. A catalog count measures coverage of definitions. A completed ordinal stage assignment has energy zero by construction; it does not mean a vulnerability reached maximum severity or is easy to exploit. Scores from different targets, variable sets, or coefficient versions are not comparable as a bounty ranking.

For a public case study, distinguish **hypothesized**, **modeled**, **native-observed**, **independently reproduced**, **privately reported**, and **vendor-confirmed** states. Give the preconditions and the strongest negative control near the result. Keep unreleased reproduction steps, private credentials, and live target details out of this showcase. The [CharLS result](charls-q3.md) and [IBM Fez pilot](ibm-fez-pilot.md) demonstrate why a verified software improvement and a measured compiler property are different claims.
