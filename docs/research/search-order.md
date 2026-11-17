# Search order: organise by mechanism, not by position

**November 9–17, 2026 · seventeen preregistered steps, P1 to P17 · Gen2 work on the older swarm, with its lesson carried to Gen3.** Every step is *measured on fixtures, no quantum-computer time* (scripted test targets with a known answer, scored by code) unless it says *measured on IBM hardware* (P7) or *recorded Gen3 outcomes* (P14, P15). [Public data](search-order.json) · [Back to the README](../../README.md#search-order)

<p align="center">
  <img src="../assets/search-order.svg" width="960" alt="Search by mechanism, not by position. Panel 1, recorded Gen3 outcomes, not blind: 125 recorded checks over 17 anonymised mechanisms; the mechanism alone predicts 111 of 125; one mechanism hit 17 of 18, another 0 of 45; the best 3 mechanisms hold 65 percent of the hits on 34 percent of the checks. Panel 2, scripted test targets, development round: targets reached of 200: every technique once, then focus, 200; no sweep 142; narrowing by position at 1, 2 and 3 levels 124, 111 and 107. On 200 fresh targets: 200 of 200 against 136 with no sweep, 5.4 times the hits. Panel 3, scripted: mechanisms found per target peak at 90 percent exploring (0.646) and fall to 0.371 with all digging; on fresh targets 0.660 against 0.600 for all exploring and 0.392 for all digging; worst loss 0.012 as the share of working variants moved. One IBM hardware run on ibm_marrakesh: narrowing found 1.7 to 3.4 times random order's good candidates per billed second, 27.0 billed seconds. Gen2 work: scripted targets, no real target, nothing replayed or trained into Model 1.">
</p>

## In plain words

Seventeen small, preregistered steps tested how the older Gen2 swarm orders its search. One lesson came out of them: **organise a search by mechanism (the kind of attack), not by where a candidate sits in a list.** Three separate lines of evidence agree. These steps say so. The Nano lockpick's scripted-reader result (L0), which searches by the features of a stuck state, says so. And in Predator's recorded Gen3 outcomes, the mechanism alone predicts 111 of 125 recorded checks.

The swarm now tries every technique once, then spends 90 % of its turns exploring and 10 % digging. On 200 scripted test targets it reached all 200, against 68 % with no sweep, and found 5.4 times the hits. These are the swarm's defaults on a draft, not on main, and each is one setting away from the old behaviour. This is Gen2 work: no real target was contacted, and nothing was replayed or trained into Model 1.

## The seventeen steps

| Step | Date | Question | Result | Verdict |
|---|---|---|---|---|
| P1 | Nov 9 | Does the swarm's original sweep order home in on the good areas of a test field? | No: its final focus zone held fewer good items than random at every size; narrowing's zone also fell short | NOT MET |
| P2 | Nov 9 | A new order, narrowing, against random order where good items sit together | 15.9, 15.4 and 14.9 times as many good items as random at three sizes; the original order 3.6 to 4.8 times | MET |
| P3 | Nov 9 | The same on messier fields | 13.5 to 14.5 times random on the messiest fields | MET |
| P4 | Nov 10 | Fields built from banked Gen3 task evidence (80 tasks) | 7.5, 4.5 and 9.6 times random at drive lengths 6, 7 and 8 | MET |
| P5 | Nov 10 | 200 fresh tasks, with read noise and dropouts | 10.2 and 9.4 times random clean; 7.9 to 10.1 with noise or dropouts | MET |
| P6 | Nov 10 | Narrowing as a hint inside a scripted solver | No gain: 1.10 and 1.06 against the solver's own search; the hint cost more than it saved | NOT MET |
| P7 | Nov 11 | Narrowing on IBM hardware, against random order | 1.7 and 3.4 times as many good candidates per billed second; 27.0 billed seconds over six jobs (*measured on IBM hardware*) | MET, "shown" |
| P8 | Nov 11 | A hardware repeat with a bad-qubit screen | The offline gate passed; the live repeat was never released or run | live NOT RUN |
| P9 | Nov 12 | Does aligning the sweep make it a solver? | No: 0.48 and 0.24 of tasks solved against a 0.50 line | NOT MET |
| P10 | Nov 12 | Wire narrowing into the swarm behind a setting | Built | built |
| P11 | Nov 12 | A Gen3 probe-mission driver that can use narrowing | Built and tested; nothing calls it yet | built |
| P12 | Nov 13 | Inside the real swarm loop: narrowing against the original order | 6.6 times as many good items. The original order only moved on when its time ran out (200 of 200 sessions), and in 9 of 200 sessions it sent 3 of 5 agents past the end of the list | MET |
| P13 | Nov 15 | The swarm's real list, with outcomes driven by technique | No difference from the original order (0.95), below no sweep (0.77): the list spreads each technique's variants evenly through its category, so position carries little | no difference |
| P14 | Nov 15 | What decides success in recorded Gen3 outcomes? | The mechanism: it predicts 111 of 125 recorded checks (permutation p 0.00001); a technique-grouped list won big on some targets and lost on most, so it was not shipped | MET, not blind |
| P15 | Nov 16 | Try every technique once, then focus | 200 of 200 targets against 68 % with no sweep, 5.4 times the hits; narrowing by position did worse than no sweep | MET, shipped |
| P16 | Nov 16 | How much to explore against how much to dig | 90 % exploring found the most mechanisms per target: 0.660 against 0.600 all exploring and 0.392 all digging (the old setting explored 15 %) | MET, shipped |
| P17 | Nov 17 | Does 90/10 hold when the share of working variants changes? | Yes: within 0.012 of the best at every share from 5 % to 100 % | 0.90 STANDS |

**Recorded outcomes, read blind (P15, reported, not gated).** The same recorded verdicts were read in two orders. Trying one test per mechanism in turn reached a hit in 11 of 17 mechanisms within the first 17 tests; the mission's own order reached 6. The mission's own order found more hits early (29 against 20 in the first 34 tests), because it kept digging where it had already found something. Coverage and depth pull apart in the real record just as in the scripted tests.

## What it means for the program

- **The old swarm is better and less broken.** On scripted test targets it now reaches every target instead of about 70 %, and it no longer depends on its original sweep order.
- **The lesson matches the Gen3 direction.** Features such as the mechanism decide outcomes; position does not. That supports the adaptive energy tokenizer, which describes a stuck point by its features.
- **A search rule worth reusing.** Check every option once, then mostly explore with a little digging, and stop digging once it only re-finds what it already found. Gen3's "what to test next" step could use it, with the balance set by the search's own count of repeat finds rather than a fixed number. Not tried there yet.
- **Two pieces set aside for the self-improvement loop, kept private.** A held-out set of 17 recorded mechanisms, to score a future Model 1 choice of which mechanism to test next. And 879 recorded narrowing decisions that could become replayable steps in Atlas.

## What it does not do

- It is Gen2 work on the legacy swarm.
- The test targets were scripted: no real judge and no real target.
- Nothing was replayed or trained into Model 1.
- It does not touch the Gen4 test: each Model 1 generation reaching further with fewer outside rescues.
- No quantum advantage. The hardware run is one run on one device, with no repeat; its gain is fewer billed seconds per useful find.

## Still open

- A smaller swarm defect wastes about 3 % of turns (2.7 %) when a focus zone is smaller than the number of agents.
- The live hardware repeat (P8) was never run.
- The Gen3 probe-mission driver (P11) has no caller.

**Proposed next step (not started).** Stop work on the old swarm here; it has answered its questions. Bring "every mechanism once, then mostly explore" into Gen3's "what to test next" step, and measure it at no cost on recorded Gen3 missions. That is where it can feed the Model 1 loop.

## Method and provenance

- Each step was preregistered before it ran, with its gates and predictions; verdicts are reported as written, misses included. The scripted test fields use invented numbers (how many techniques are open on a target, what share of variants work); P17 varied the second.
- The recorded outcomes come from local reproductions in one Gen3 private security mission, with no live target. Mechanisms are anonymised. The P14 read was not blind (the counts were seen before the preregistration, and promising mechanisms were tested more often); the P15 replay was blind.
- The swarm's original sweep order is the owner's own earlier method and stays private; this page describes only how it behaved in these tests.
- The hardware run (P7) used the open IBM plan through a direct route from a laptop, not Predator's production route. It used 27.0 of the experiment's 120 allowed quantum-seconds, the only spend in these steps. 85 % of probe indices arrived exactly; one unstable qubit carried almost all the errors.
- Pins: every report, P1 to P17, at private commit [`a66d8f223892bdd17f3debb46083486c863828b0`](https://github.com/AetherAI3/AETHER-PREDATOR-M/tree/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field), for example [P12](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field/REPORT_P12.md), [P14](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field/REPORT_P14.md), [P15](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field/REPORT_P15.md), [P16](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field/REPORT_P16.md) and [P17](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field/REPORT_P17.md); the P7 hardware result `a57364d6db38f772ff4a7ca87613152d989d74f7`; the default changes `c77d20e2d7589b9166d2c6b1ffde7d0cf09e7776` (P13), `c84a6c0ec8293ea97b224855f1ab79a44254c7da` (P15) and `722dc603218a64620a7a8c3cf2151056e750d516` (P16). All are on draft [PR #489](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/489), into a feature branch, not main.

## Rebuild the figure

```bash
python docs/assets/build_search_order_assets.py --check
```

The builder reads only [search-order.json](search-order.json), uses the Python standard library, and fails if any label would overflow its box or if the figure's wording no longer matches the data.
