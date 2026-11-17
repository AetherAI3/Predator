# Search order: organise by mechanism, not by position

**November 9–17, 2026 · seventeen preregistered steps on the older Gen2 swarm (P1 to P17), then one replay in Gen3 (P18).** Every step is *measured on fixtures, no quantum-computer time* (scripted test targets with a known answer, scored by code) unless it says *measured on IBM hardware* (P7) or *recorded Gen3 outcomes* (P14, P15, P18). [Public data](search-order.json) · [Back to the README](../../README.md#search-order)

<p align="center">
  <img src="../assets/search-order.svg" width="960" alt="Search by mechanism, not by position. Panel 1, recorded Gen3 outcomes, not blind: 125 recorded checks over 17 anonymised mechanisms; the mechanism alone predicts 111 of 125; one mechanism hit 17 of 18, another 0 of 45; the best 3 mechanisms hold 65 percent of the hits on 34 percent of the checks. Panel 2, scripted test targets, development round, at the old 15 percent explore rate: targets reached of 200: every technique once, then focus, 200; no sweep 142; narrowing by position at 1, 2 and 3 levels 124, 111 and 107. On 200 fresh targets: 200 of 200 against 136 with no sweep, 5.4 times the hits. Panel 3, scripted: mechanisms found per target peak at 90 percent exploring (0.646) and fall to 0.371 with all digging; on fresh targets 0.660 against 0.600 for all exploring and 0.392 for all digging; worst loss 0.012 as the share of working variants moved. One IBM hardware run on ibm_marrakesh, where the hardware only carried the probes: narrowing found 1.7 to 3.4 times random order's good candidates per billed second, 27.0 billed seconds. A replay of recorded Gen3 missions (P18): 12 of 12 mechanisms against 11 for Gen3's current next-test rule on one mission; the win rests on one mechanism. Gen2 work: scripted targets, no real target, nothing replayed or trained into Model 1.">
</p>

## In plain words

Seventeen small, preregistered steps tested how the older Gen2 swarm orders its search. One lesson came out of them: **organise a search by mechanism (the kind of attack), not by where a candidate sits in a list.** Predator's recorded Gen3 outcomes point this way: the mechanism alone predicts 111 of 125 recorded checks (not blind). The Nano lockpick's scripted-reader result (L0), which searches by the features of a stuck state, agrees. The scripted steps assume that outcomes follow the mechanism, and measure what searching by it is worth.

Trying every technique once, then focusing, reached all 200 scripted test targets, against 68 % with no sweep, with 5.4 times the hits (P15, run at the old 15 % explore rate). A second test then set the balance: exploring 90 % of the time and digging 10 % found the most distinct mechanisms per target (P16). Both are now the swarm's defaults, on a draft, not on main, and settings switch them back. A follow-up replay on recorded Gen3 missions then favoured the rule over Gen3's current next-test rule, on one mission (P18). This is Gen2 work: no real target was contacted, and nothing was replayed or trained into Model 1.

## The eighteen steps

| Step | Date | Question | Result | Verdict |
|---|---|---|---|---|
| P1 | Nov 9 | Does the swarm's original sweep order home in on the good areas of a test field? | No: its final focus zone held fewer good items than random at every size; narrowing's zone also fell short (it met the line at 1 of 3 sizes; the gate needed 2) | NOT MET |
| P2 | Nov 9 | A new order, narrowing, against random order where good items sit together | 15.9, 15.4 and 14.9 times as many good items as random at three sizes; the original order 3.6 to 4.8 times | MET |
| P3 | Nov 9 | The same on messier fields | 13.5 to 14.5 times random on the messiest fields | MET |
| P4 | Nov 10 | Fields built from banked Gen3 task evidence (80 tasks) | 7.5, 4.5 and 9.6 times random at drive lengths 6, 7 and 8; above 1.5 at all three, and length 7 failed only the significance check | MET |
| P5 | Nov 10 | 200 fresh tasks, with read noise and dropouts | 10.2 and 9.4 times random clean; 7.9 to 10.1 with noise or dropouts | MET |
| P6 | Nov 10 | Narrowing as a hint inside a scripted solver | No net gain: 1.10 and 1.06 against the solver's own search; the hint cost more than it saved | NOT MET |
| P7 | Nov 11 | Narrowing on IBM hardware, against random order | 1.7 and 3.4 times as many good candidates per billed second; 27.0 billed seconds over six jobs. The hardware only carried the probes, with no quantum computation in the search; the smaller size passed by one billed second per job (*measured on IBM hardware*) | MET, "shown" |
| P8 | Nov 11 | A hardware repeat with a bad-qubit screen | The offline gate passed; the live repeat was never released or run | live NOT RUN |
| P9 | Nov 12 | Does aligning the sweep make it a solver? | No: the aligned sweep solved 4.8 and 4.0 times as many tasks as the unaligned order, but only 0.48 and 0.24 of them against a 0.50 line | NOT MET |
| P10 | Nov 12 | Wire narrowing into the swarm behind a setting | Built, off by default at the time | built |
| P11 | Nov 12 | A Gen3 probe-mission driver that can use narrowing | Built and tested; nothing calls it yet | built |
| P12 | Nov 13 | Inside the real swarm loop: narrowing against the original order | 6.6 times as many good items (2.2 times from the order alone, the rest from sweeping the list's real length). The original order only moved on when its time ran out (200 of 200 sessions), and in 9 of 200 sessions it sent 3 of 5 agents past the end of the list | MET |
| P13 | Nov 15 | The swarm's real list, with outcomes driven by technique | No difference from the original order (0.95), below no sweep (0.77): the list spreads each technique's variants evenly through its category, so position carries little | no difference |
| P14 | Nov 15 | What decides success in recorded Gen3 outcomes? | The mechanism: it predicts 111 of 125 recorded checks (permutation p 0.00001). A technique-grouped list won big on some targets and lost on most (only "above", not shipped) | Part R MET, not blind |
| P15 | Nov 16 | Try every technique once, then focus (at the old 15 % explore rate) | 200 of 200 targets against 68 % with no sweep, 5.4 times the hits; narrowing by position reached fewer targets than no sweep (0.535 to 0.620 against 0.710) | MET, shipped |
| P16 | Nov 16 | How much to explore against how much to dig | 90 % exploring found the most mechanisms per target: 0.660 against 0.600 all exploring and 0.392 all digging (the old setting explored 15 %). Total hits fall as exploring rises (1,723 at 90/10 against 2,896 all digging): the mix trades repeat finds for coverage | MET, shipped |
| P17 | Nov 17 | Does 90/10 hold when the share of working variants changes? | Yes: its worst loss against the best rate was 0.012 across shares from 5 % to 100 % | 0.90 STANDS |
| P18 | Nov 17 | The rule against Gen3's current next-test rule, replayed on recorded missions | 12 of 12 mechanisms against 11 on the one mission large enough to count; the win rests on one mechanism (see below) | SHIP by its rule; not wired yet |

**Recorded outcomes, read blind (P15, reported, not gated).** The same recorded verdicts were read in two orders. Trying one test per mechanism in turn reached a hit in 11 of 17 mechanisms within the first 17 tests; the mission's own order reached 6. The mission's own order found more hits early (29 against 20 in the first 34 tests), because it kept digging where it had already found something. Coverage and depth pull apart in the real record just as in the scripted tests.

## Since then: the rule in Gen3, as a replay (P18)

P18 replayed the rule on recorded Gen3 missions at no cost, against Gen3's current next-test rule, unchanged. Each rule could take only tests the missions recorded, up to three tests per mechanism. On the one mission large enough to count, the rule reached all 12 mechanisms that hit in the record; the current rule reached 11. **The win rests on one mechanism**: its first recorded test missed and it hit later, and the current rule drops a candidate after one miss. Two smaller missions were not counted (one more win, one tie). The current rule's hit count is not comparable, because it ran out of recorded tests after 23 of 51.

The replay also exposed two properties of the current rule worth Gen3's attention: every hit scores the same, so ties are broken by candidate id, and it scores only a candidate's latest test, with no memory of its record. The rule passed its preregistered ship rule, but it is not wired into Gen3 yet. Gen3's next-test step works in cycles with a shrinking fanout, while the tested rule works test by test, so fitting it in would be a different, untested algorithm. Next: build the cycle form as an opt-in Gen3 rule, replay it on the same frozen missions, and only then offer it.

## What it means for the program

- **The old swarm is better and less broken.** On scripted test targets it now reaches every target instead of about half: earlier rounds put the old defaults at 0.48 to 0.56, and no sweep at about 0.70. It no longer depends on its original sweep order.
- **The lesson matches the Gen3 direction.** In the recorded data the mechanism decided outcomes. That agrees with the adaptive energy tokenizer, which describes a stuck point by its features.
- **A search rule worth reusing.** Check every option once, then mostly explore with a little digging, and stop digging once it only re-finds what it already found. P18 then replayed it against Gen3's current rule, above.
- **Two pieces set aside for the self-improvement loop, kept private.** A held-out set of 17 recorded mechanisms, to score a future Model 1 choice of which mechanism to test next. And 879 narrowing steps logged on the scripted test fields, which could become replayable steps in Atlas.

## What it does not do

- Most of it is Gen2 work on the legacy swarm; P18 is a replay, not a live Gen3 run.
- The test targets were scripted: no real judge and no real target.
- Nothing was replayed or trained into Model 1.
- It does not touch the Gen4 test: each Model 1 generation reaching further with fewer outside rescues.
- No quantum advantage. The hardware run is one run on one device, with no repeat; the hardware only carried the probes, and the gain is fewer billed seconds per useful find.

## Still open

- A smaller swarm defect wastes turns when a focus zone is smaller than the number of agents: 2.7 % at the old 15 % explore rate, about 0.3 % at the shipped 90 %.
- The live hardware repeat (P8) was never run.
- The Gen3 probe-mission driver (P11) has no caller, and neither does the P18 rule until its cycle form is built and replayed.

## Method and provenance

- Each step was preregistered before it ran, with its gates and predictions; verdicts are reported as written, misses included. The scripted test fields use invented numbers (how many techniques are open on a target, what share of variants work); P17 varied the second.
- The recorded outcomes come from local reproductions in Gen3 private security missions, with no live target; this page counts them only. Mechanisms are anonymised. The P14 read was not blind (the counts were seen before the preregistration, and promising mechanisms were tested more often); the P15 replay was blind; P18 replayed the recorded verdicts off-policy from files frozen before any order was read.
- The swarm's original sweep order is the owner's own earlier method and stays private; this page describes only how it behaved in these tests.
- The hardware run (P7) used the open IBM plan through a direct route from a laptop, not Predator's production route. It used 27.0 of the experiment's 120 allowed quantum-seconds, the only spend in these steps. 85 % of probe indices arrived exactly; one unstable qubit carried almost all the errors.
- Pins: the first seventeen reports at private commit [`a66d8f223892bdd17f3debb46083486c863828b0`](https://github.com/AetherAI3/AETHER-PREDATOR-M/tree/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field), for example [P12](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field/REPORT_P12.md), [P14](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field/REPORT_P14.md), [P15](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field/REPORT_P15.md), [P16](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field/REPORT_P16.md) and [P17](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/a66d8f223892bdd17f3debb46083486c863828b0/bench/qcomms/r_gen2_field/REPORT_P17.md); the P7 hardware result `a57364d6db38f772ff4a7ca87613152d989d74f7`; the default changes `c77d20e2d7589b9166d2c6b1ffde7d0cf09e7776` (P13), `c84a6c0ec8293ea97b224855f1ab79a44254c7da` (P15) and `722dc603218a64620a7a8c3cf2151056e750d516` (P16); P18's preregistration `aeee5af202293774d745b185f11eeb4c7bc4ef6b`, build `3aa21a57f9758138511575fc9b8398e129e50ceb` and [result](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/1c3d9b2150265d64bdd8fb3e76c6fdc463850e32/bench/qcomms/r_gen2_field/REPORT_P18.md) `1c3d9b2150265d64bdd8fb3e76c6fdc463850e32`. All are on draft [PR #489](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/489), into a feature branch, not main.

## Rebuild the figure

```bash
python docs/assets/build_search_order_assets.py --check
```

The builder reads only [search-order.json](search-order.json), uses the Python standard library, and fails if any label would overflow its box or if the figure's wording no longer matches the data.
