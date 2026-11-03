# Gen3 Quantum Comm Ops

**Useful context for each worker. Verified handoffs. Less repeated work.** Quantum Comm Ops is Predator's research into coordinating large agent workflows through compact messages, a shared evidence bank, and controls that concentrate further work on promising branches.

**Current review: November 1, 2026, updated November 2 for IBM's final accounting and the agent-lane figures, and November 3 for [Experiments L and M](#experiments-l-m), which were built and reviewed offline and have not run.** The 400-agent message delivery mission has now run on **IBM quantum hardware**: one IBM job per mission, billed **5.0 seconds**, and all 400 agents received their message intact on the first try in each of five missions across three message sets, two devices and two secret keys. The simulator configuration that preceded it (three shots with capped six-shot rescue) remains the adopted **research baseline** on `feat/qcomms-i`; neither is a production rollout. This public review checks committed reports and their arithmetic. It is not an independent experimental rerun. [Public aggregate data](quantum-comm-ops.json) carries the measurements; [current source records](#current-source-records) identify the private evidence inspected.

## Purpose and message path

The goal is to give a worker the evidence needed for its next task without repeatedly sending the full mission history. A shared bank holds the records. A small packet identifies or reconstructs the relevant entries, and the receiver resolves them into structured context. Model usefulness is tested separately from delivery.

1. **Compile assignments.** Choose each recipient's message, encoding and validation requirements before execution.
2. **Deliver.** Compare ordinary delivery with the experimental Nano → ATLAS quantum-search route. In the latter, the message is encoded as a lowest-energy answer and sampled on an IBM backend: **FakeFez**, a simulator configured to model an IBM device, during the D–I hillclimb, and the real **ibm_fez** and **ibm_kingston** devices in the J missions below.
3. **Check and recover.** Verify the receipt, reconstruct the message, and check its keyed tag. A refused message remains unaccepted; a bounded retry can deliver it again.
4. **Continue from supported results.** The intended workflow resolves the accepted message against the evidence bank, runs the next worker task, and preserves evidence for the next planning round.

The demonstrated benchmark uses scripted agents (called "recipients" in the earlier simulator sections below) and synthetic messages. It does not establish that 400 LLMs can reason successfully from the handoffs, transfer model weights or internal states, or operate across independently isolated sandboxes. Communication uses service requests and files. The hardware missions in the next section ran on IBM devices; every other Comm Ops result on this page is a simulator or dry-run result, or (for the agent lanes) a fixture-task model result with no quantum-computer time. The separate [joint5 IBM Fez pilot](ibm-fez-pilot.md) is a different hardware experiment about circuit compilation.

<a id="ibm-hardware-missions"></a>

## IBM hardware missions: October 31 – November 1, 2026

### The mission in plain words

Picture **400 AI worker agents** on one team. Before each agent can start its task it needs its own short **briefing**: which records in the shared evidence bank it should use. Quantum Comm Ops writes those 400 briefings, sends each one through an IBM quantum computer, and checks that every agent received exactly the briefing meant for it. The words used below:

| Word | What it means here |
| :--- | :--- |
| **Agent** | One of the 400 workers. In this research the agents are **scripted stand-ins** that only check and record their briefing; they are not 400 reasoning language models. |
| **Message / briefing** | A 96-bit code that names the agent's records in the shared bank. It is cut into three 16-bit pieces, each sent as one tiny quantum circuit, so one mission is 400 × 3 = **1,200 circuits**. |
| **Shot** | One run of a circuit on the quantum computer, giving one reading of its bits. Running a circuit five times gives five readings; a **majority vote** across them decides each bit. |
| **Check code (tag)** | A 32-bit code attached to every message, computed with a key, like a tamper seal. The agent recomputes it; a mismatch means the message is refused. |
| **Receipt** | IBM's signed record of the job, kept by Predator so the delivery can be re-checked later. |
| **Verified / intact** | The agent's three pieces were decoded, reassembled, and the check code matched. |
| **First try** | No piece had to be re-sent. **After re-send**: the count after one bounded round of re-sending refused messages at six shots. |
| **Billed seconds** | The seconds of quantum-computer time IBM charged for the job. IBM does not bill queue time. |

The owner authorized one research day on IBM's free open plan (600 billed seconds) with a $50 model budget. Each hardware run was **preregistered** (its pass/fail targets were published before the run) and **rehearsed on the FakeFez simulator**, then submitted through the production **Predator → Nano → ATLAS → IBM** route. A ledger holds every job's reserved seconds until IBM's bill is final, so an unbilled job is never counted as free. The missions below use the same 400-agent message construction and compiler as the simulator missions.

### The ladder: from 81 jobs to one

| Mission | Device | IBM jobs | Shots per circuit | Intact on first try | After re-send | Billed seconds |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| J5, first full mission | ibm_fez | 81 (80 packed + 1 re-send) | 3 | 399 of 400 | 400 of 400 | **162 s** |
| J6, whole first try in one job, two compiler settings | ibm_kingston | 2 per setting | 3 | 395 and 392 of 400 | 400 of 400 both | 6 s per setting |
| **J7, one job at five shots** | ibm_kingston | **1** | 5 | **400 of 400** | 400 of 400 | **5.0 s** |
| J8, two more fresh message sets | ibm_kingston | 1 each | 5 | **400 and 400** | 400 of 400 | 5.0 s each |
| J9, secret key chosen at run time | ibm_kingston | 1 | 5 | **400 of 400** | 400 of 400 | 5.0 s |
| **J11, second device, new secret, message set reused from J8** | ibm_fez | 1 | 5 | **400 of 400** | 400 of 400 | **5.0 s** |

**How the cost fell.** J5 put 15 circuits in each IBM job; IBM billed about 2 s per job, so 81 jobs cost 162 s. J6 put all 1,200 circuits in **one** job and the first try cost 4 s, but with only three readings per circuit, 5–8 of the 1,200 pieces had a wrong majority vote. The check code caught every one and the re-send round fixed them, so J6 met its "after re-send" target but missed its "first try" target of 396. J7 raised the readings to five per circuit: that cost one more billed second and **no piece came out wrong**. J8, J9 and J11 then repeated that exact setup on new message sets, with a secret key, and on a second device.

Across the five one-job five-shot missions: **2,000 of 2,000 agents got their message intact on the first try, with 0 wrong bits after the vote in 480,000 single readings**; before the vote, 0.41–0.52% of single readings were wrong. These are five missions from one synthetic message generator on two devices over two days; they are not a production reliability measurement.

### The packing test: same circuits, same device

The 162 → 5 s comparison mixes different devices, days and shot counts. The clean test is small: the first agent's three circuits, compiled **once** for ibm_fez and reused byte for byte, were sent as one three-circuit job and as three one-circuit jobs, in both orders (J11 part C). The packed job was billed **2.0 s**; the three separate jobs were billed **2.0 + 2.0 + 2.0 = 6.0 s**, each time. The first hardware message on October 31 (J0) had found the same 2.0 vs 6.0 s with freshly compiled circuits. This establishes the saving at three circuits; it does not measure it at 1,200, and IBM does not reveal how it splits a packed request internally.

### Secret-key delivery and controls

In J9 and J11 every check code was computed from a secret chosen on the research host at run time and never written to any report; only a one-way fingerprint of it is recorded. With the secret, 400 of 400 messages passed the check. With the public (wrong) key, **0 of 400** passed, which is the intended refusal. A scan of the run's output files for the secret and its 800–1,600 derived values found **0 hits** in both missions. The check code proves a message was not altered; it does not hide the message (nothing is encrypted). A secret in a file on the research host is not production key management.

### Evidence that flows onward

- **J1, superposed records on hardware (ibm_fez, direct Sampler submission):** a shallow circuit delivered two records across its samples with a coherence witness of 0.813 ± 0.013 (a classical mixture would give 0). Per-record delivery was about 0.43 versus 0.91 for one record per circuit, and a deeper ten-layer arm delivered only 0.19–0.21 per record, so this track **ran on hardware but did not beat ordinary packing**; the witness is not a full-state fidelity.
- **J10, typed-message model qualification (no QPU):** with models emitting ordered typed path rows and deterministic code packing the 96-bit pin, a frontier model verified **12/12 held-out tasks** (two task families) with 0 serializer mismatches; controls: full table 12/12, no hint 0/12, wrong record 0/12. Cost $3.24. Repeated replies were identical, so repeats are not independent.
- **J12, end to end from hardware briefing to checked task (no new QPU):** four hardware-delivered briefings (J0's agent on ibm_fez; three J9 agents on ibm_kingston under the secret key) were re-checked from their signed receipts, decoded, check-code verified, matched to the bank, turned into J10's typed message, read by the model, and the model's answer was scored by the deterministic checker: **4 of 4 correct**, including the exact 96-bit pin that every earlier free-form model reply had missed. Cost $0.35.

### Attempts that did not succeed

| Attempt | What happened | Status |
| :--- | :--- | :--- |
| J6 first-pass gate | 395/400 and 392/400 at three shots, gate ≥ 396 | **Not met**; all-in 400/400; five shots adopted |
| J2 calibration-ranked layout | A modelled success probability (ESP) of 0.951 versus 0.810 did not appear as lower hardware error: 0.604% vs 0.597% raw error, p ≈ 0.56 | **Rejected on hardware**; option stays default-off |
| J11 on ibm_kingston after a recalibration | Job queued 11 h 21 min and was cancelled before running | **Not run**; claim pending; 30 s reserved, released November 2 when IBM reported final usage 0 s |
| J11 retry on ibm_marrakesh | Stopped by a 10 s provider execution limit that had been sized from billed seconds; the provider's limit is not the billed figure, and jobs billed 5 s had run 31–71 s of wall clock | **Error**; 10 s reserved, settled November 2 at IBM's final 5 s; replaced by the ibm_fez run |
| J6 on ibm_fez | Queue of 1,596–1,946 pending jobs for two hours | **Not run**; fell back to ibm_kingston |

The two reserved amounts (40 s in total) stayed counted against the programme until IBM reported their usage as final; at the time of the November 1 review both still read "pending" at the provider. A zero that has not been finalized is never treated as free.

**Settled November 2, 2026.** A host watcher polled the provider's usage record every 15 minutes (44 polls, no job submitted, ledgers backed up before each change). About 13 hours after each job ended, IBM reported final usage: the cancelled ibm_kingston attempt at **0 s** (its 30 s reservation released) and the stopped ibm_marrakesh attempt at **5 s** (its 10 s reservation settled at 5 s; the provider billed the stopped job for the time it ran before the limit). That 5 s was already inside the 254 s account total as a previously unattributed step, so the programme total is unchanged; the J11 line fell from 61 s charged to **26 s**. The ibm_kingston-after-recalibration claim remains pending because that job never ran.

### Budget

| Budget | Cap | Used |
| :--- | ---: | ---: |
| IBM free open plan | 600 s | **254 s** (J0 16, J1 8, J3 4, J5 162, J6 12, J7 11, J8 10, J9 5, J11 26 (R 5 + C 16 + the marrakesh attempt 5, attributed when IBM finalized it on November 2); J7's 11 s includes a separate seven-shot arm billed 6 s, and J6's 12 s covers both compiler arms) |
| IBM pay-as-you-go instance | 0 | 0 |
| Aether model calls | $50 | ≈ **$18.65** (model-hint arm $14.70, reviews $0.35, J10 $3.24, J12 $0.35) |

The 5 s for the ibm_marrakesh attempt was an account-counter step that stayed unattributed while that job's own usage read 0; IBM finalized it at 5 s on November 2 and it is now counted in the J11 line.

### What the hardware missions do not show

A production reliability guarantee; confidentiality (tags authenticate, nothing is encrypted; J0–J8 used public tag keys); that IBM runs a packed request as a fixed number of internal sub-jobs; a packing ratio beyond three circuits; and **any quantum advantage**. The mission circuits prepare known classical frames with no two-qubit gates. The billed saving is IBM's accounting for batched circuits, and the device is used as a sampling backend for a verifiable delivery protocol, not as a faster computer.

<a id="earlier-simulator-milestone"></a>

## Earlier simulator milestone: three fresh datasets

*In this section and below, "recipient" means the same thing as "agent" above: one of the 400 scripted workers that receives and checks its own message.*

Each mission starts with 400 recipients and fresh frames, keys and sampling seeds. The datasets come from the **same synthetic generator**, so these repetitions test that configuration rather than generality across workloads. A job requests repeated samples; each sample is a **shot**.

| Three-shot mission | First pass | After rescue | All-in jobs | All-in shots | Reported mission wall |
| :--- | ---: | ---: | ---: | ---: | ---: |
| I2 | 400/400 | 400/400 | 1,200 | 3,600 | 2,828.1 s (47.1 min) |
| I6 repeat 1 | 400/400 | 400/400 | 1,200 | 3,600 | 2,946.9 s (49.1 min) |
| I6 repeat 2 | 399/400 | 400/400 | 1,203 | 3,618 | 3,061.0 s (51.0 min) |

Across the three missions, **1,199/1,200 deliveries passed initially and 1,200/1,200 verified after rescue**. These are observed sample counts, not a production reliability guarantee. In repeat 2, a chunk's majority vote was wrong. Its 32-bit tag refused the message, and resampling that recipient's three chunks at six shots recovered it: three extra jobs and 18 shots. A separate forced-corruption drill also exercised the six-shot rescue successfully; it is not counted as another scored mission.

Three readings cannot tie on a single bit, but they can agree on a wrong value. The tag and receipt checks remain necessary. Compared with four shots on this same three-chunk layout, initial sampling falls from 4,800 to 3,600 shots (**25% fewer**). The run with a rescue used 3,618 shots, saving **24.625% all-in** against that 4,800-shot reference. Fewer shots do not imply an equal reduction in runtime or price.

## What changed since the earlier 400-recipient run

| Improvement | What it contributes |
| :--- | :--- |
| **Denser framing** | This generator's 96-bit chain can be reconstructed from 12 variable bits under the shared prior. Adding a 32-bit tag and padding produces three 16-bit chunks per recipient, instead of eight. The compiler admits only compatible inputs. This is fixture-specific encoding, not arbitrary 96-bit knowledge compressed into 12 bits. |
| **Lower sampling with verified rescue** | Three-shot initial sampling plus one capped six-shot rescue round passed the recorded gates on all three datasets. |
| **Pooled simulator setup** | Eight service processes reuse their expensive backend setup while producing fresh samples and receipts for each job. Backend reuse does not replay earlier evidence. |
| **Exact structural certificates** | The compiler proves the supported QUBO's ground-state properties directly. Every job receives a certificate check; 2% also receive the exhaustive cross-check. The sample audits the implementation rather than replacing per-job certification. |

F2 cycle 4 used **3,232 all-in jobs and 13,056 shots** for 400 final verified recipients, with 396/400 passing initially. The latest missions use **1,200–1,203 jobs and 3,600–3,618 shots**. These are measured mission totals from different configurations and datasets. The earlier F2 timing comprises a 3h16m33s first-pass window and a separate approximately six-minute rescue; the current table uses reported mission wall and excludes separate smoke runs. No matched end-to-end speedup ratio is claimed.

The compiler's earlier **87–170× faster structural check** was a local component microbenchmark. Its effect on a complete mission is smaller. Likewise, the reported **10.614–10.667 verified logical bits per shot** counts reconstructed 96-bit chains under the shared prior; it is not an arbitrary-information capacity measurement.

## Coordination, context and the cost comparison

**Custom Fanout Controls (CFC)** decides how broadly to explore and which candidates receive more detail. The earlier scripted controller benchmark found the same synthetic winners while transmitting about 0.9% of the baseline's estimated tokens. That number measures transmitted information, not actual model processing or LLM bills. Exact repeat deliveries could reuse cached results with zero new samples; other computation still remained.

![Illustrative adaptive CFC policy: start with up to 400 candidates, narrow to 40, then focus on four. These are policy caps, not the measured recipient counts of the delivery missions.](../assets/quantum-comm-ops.svg)

H3 showed why the baseline matters: its rendered compact hints cost more than a cached full table. I3's **IRv2** revision preserved the resolved facts and passed 40/40 scripted cases at an illustrative 0.442× baseline cost. It used 17–18 benchmark accounting tokens, but **54–60 Qwen tokenizer tokens**. The advantage depends on caching the legend; without that caching, the Qwen-token comparison was 1.064× baseline. Useful real-model continuation remains unqualified in this programme.

H6 also compared superposition multiplexing with ordinary circuits packed under the same assumptions. **The tested superposition scheme did not win at any of the 42 modeled cost points.** Sampling counts were measured on FakeFez; provider usage and prices were modeled. Superposition did not produce the successful framing or backend-pooling gains.

## System2 evidence accounting

A separate **tested draft** repairs how System2 counts support for claims: repeated statements from one source no longer create extra corroboration, and substring matching is removed. The producer reports **314 System2 tests passing** across the Python and native paths. The draft remains unmerged at this review. Its incremental ledger and new caller metadata are not integrated, and full contradiction handling and summary-window retention remain unfinished. This is progress toward trustworthy shared context, not evidence that a complete model handoff workflow has shipped.

## Agent lanes: November 1, 2026 (evening)

After the hardware missions, the programme turned to the agents on either side of the channel. Every number here is from
fixture tasks with known answers, scored by a deterministic checker; the workers are API models, one locally hosted recurrent-depth model on a CPU host, or scripted stand-ins;
**no IBM job and no quantum-computer time** were used. Six lanes ran, each preregistered before its first call.

The rows follow the lockpick order used in the README (hold tension, feel many pins, keep the pins that bind, set the binding pin, only as many hands as we have, next cycle).

| lane (lockpick) | question | verdict | result |
|---|---|---|---|
| Encoder (hold tension) | does a stronger encoder pick the right evidence for each agent? | **MET** | voyage-code-4 recall@8 **0.87** within the evidence pool (0.57 across the whole bank) vs keyword search 0.38 / 0.17; harmful records in the top eight 0.21 / 0.09 against the earlier reranker's 0.29; a permutation control at chance. |
| Selection → agent (hold tension) | does that top eight let an agent verify? | **MET** with the compiler filter (not met as first registered) | scripted agent **5 of 110** on the raw top eight; **99 of 110** once the briefing compiler drops other chains' records and contradicted records before the cut. Keyword search with the same filter 0 of 110. The lesson: status must be a *filter*, not a label. |
| Worker survey (feel many pins) | which cheaper worker verifies ≥ 11 of 12 at ≤ 25% of the frontier price? | **NOT MET** at the 25% bar | none: the best mid-cost model verified **12 of 12 at 63%**; the free tier 7 of 12 at 2%; two models refused the strict JSON envelope (0 of 12), a format failure rather than a content failure. A plain majority of seven workers equalled the truth on 9 of 12. |
| Selection vote (keep the pins that bind) | does a quantum-style selector beat a vote where agents disagree? | **MET** | 12 tasks, 3 of them where a plain majority split or was wrong (9 of 12 overall); a reliability-weighted vote **12 of 12**; one-hot and coherence QUBO selectors on a classical MPS simulator also 12 of 12. An offline re-read of the survey's replies, no new model calls. A weighted vote suffices; the quantum-style selectors matched it and did not beat it. |
| "Think longer" worker (set the binding pin) | does a recurrent-depth model verify a typed path when allowed more loops? | **NOT MET** | **0 of 12** at depths 4, 8 and 16 on a CPU host (depth 32 for one task only; stopped by the memory rule). Depth 16 produced three schema-valid records whose transitions were invented in state order. Every reply hit the 192-token cap. Deep cells stay frontier-only. A follow-up cycle with the model's adaptive exit (stop looping on a token once its internal state settles, threshold 0.03) was inert: the state never settled (change 1.14–1.18 per loop), 8 of 192 tokens exited early, the mean was 31.5 of 32 loops, and the host's memory rule stopped the run after one off-task reply; 11 tasks not run. The preregistered hardness ladder (next row) gives deep cells a calibration target: a family where the frontier model alone verifies **2 of 12**. |
| Narrow, then deepen (only as many hands as we have) | does deepening on survivors beat narrowing alone at matched budget? | **NOT RUN** | The preregistered hardness ladder found a family where the frontier model alone verifies **2 of 12** (33 evidence rows; 9 of 12 at 23 rows). In the narrowing pass the free tier verified **0 of 24** (19 invalid records, 4 MISS, 1 flagged wrong answer) and the mid-cost model verified **9 of the 9** hard leads it reached before the lane's $5 cap halted the run with 15 leads pending and no deep cell opened — so the family is solvable by one shallow worker, and the set left for deepening may be small. The cost model had under-shot 2–5×: per-call rates had been measured on 12-row prompts and the hard family's prompts are three times longer. Resumable; the cap is an owner decision. |
| Compounding (next cycle) | does one round's bank make the next round cheaper per verified record? | **MET** on the rehearsal corpus | three rounds over the **same 40 fixture chains** (the bank seeded by a scripted warm-up round on other chains), paid first-tier worker paced at 40 s: first-try verified **24 → 38 → 39**, hand-offs **16 → 2 → 1**, cost per verified record **0.45×** round one, 0 errors, $4.06. Fresh, non-fixture tasks are open. Two earlier runs with a free-tier first model replicated rounds one and two (23 → 39; cost per verified down 7.6–14×) and were stopped in round three by the model gateway's per-hour call quota (about 100 accepted calls per hour; a refused call carries no usage and is charged its reservation). |

<p align="center">
  <a href="../assets/quantum-comm-ops-compounding.svg"><img src="../assets/quantum-comm-ops-compounding.svg" width="960" alt="Compounding measured on fixture tasks with no quantum-computer time: across three cycles over the same 40 chains, agents verified first try 24, then 38, then 39 of 40; hand-offs to the mid-cost model fell from 16 to 2 to 1; and the cost per verified record fell to 0.45 times cycle one."></a>
</p>

<p align="center">
  <a href="../assets/quantum-comm-ops-agent-loop.svg"><img src="../assets/quantum-comm-ops-agent-loop.svg" width="960" alt="One cycle of the agent loop: the shared evidence bank feeds the encoder, which picks each agent's records (measured on fixtures: about 87 percent of relevant records in the top eight); the compiler drops other chains' and contradicted records (fixtures: 99 of 110 verified with the filter, 5 of 110 without); 400 briefings go out in one IBM job (hardware: 400 of 400 intact, 5 seconds billed); verified records are banked with their receipts; disagreements go to a reliability-weighted vote (fixtures: 12 of 12); deep cells on surviving leads are not run; and the bank feeds the next cycle (fixtures: first-try 24, 38, 39 of 40)."></a>
</p>

Model spend for the agent lanes: about **$24**; the programme's ledger stands at **$42.50 of $50**. Source pins for every
lane are in the JSON under `agent_lanes`.

<a id="experiments-l-m"></a>

## Experiments L and M: built and reviewed, not yet run (November 3, 2026)

On November 3 the programme built its next layer and stopped before spending. **Experiment L** adds a *model lane* (a frontier model proposes a small, exact weight patch to a small local model, and a separate evaluator promotes or rejects it on tasks the proposer never sees), *96-bit control packets* that let the attack, repair and model lanes reference evidence in the shared bank instead of carrying it, a *sealed research package* with one lineage per lane, and a *scale model* with a three-lane orchestrator dry run. **Experiment M** adds the *economics* of running the wide cycles on self-hosted open models instead of the gateway, and the *switch fabric* for moving a lead from a small model to a big one without moving weights. Everything ran offline at **$0**: no provider call, no IBM job, no GPU rental. The frontier model is unnamed here and was never called. Each row says what kind of evidence it is.

| lane | what it is | gate | verdict | key numbers | evidence |
|---|---|---|---|---|---|
| L1 model lane | a frontier programmer repairs one reproducible failure of a 0.8-billion-parameter local model; an independent evaluator promotes or rejects the patch | L-1a / L-1b / L-1c | **NOT RUN** on the real model | harness complete; offline rehearsal with a fake model promoted one patch and rejected the repeat; the real baseline cycle was in progress at review; no candidate, no promotion | built, not run |
| L2 control packets | one 96-bit authenticated frame per message: lane, operation, cycle, a 32-bit evidence reference, a 32-bit keyed tag | L-2a | **MET** | **1,200 of 1,200** compile, verify and resolve; wrong key **0**, one flipped bit **0**, replay **0** of 1,200; 378 packets reference real prior records, 822 reference ids the gate minted (a codec round trip), 21 more reference the hardware record | measured offline, no QPU |
| L3 research package | one lineage record per node, a manifest with the model version at each checkpoint, a Merkle root, an outer seal and a 15-check verifier | L-3a | **MET** | **147** records PASS; **87,304 of 87,304** single-bit corruptions (every byte of both files) FAIL, 0 escaped; a rejected patch can never become a parent | measured offline, no QPU |
| L4 scale | a cost and time model from measured parts, and a 3-lane x 3-cycle x 40-agent dry run with scripted workers | L-4a / L-4b | **MET** | dry run: **379** packets verified and resolved, 0 unexpected rejects, **8 of 8** ops, package PASS; model: a 400-agent 3-lane cycle about **$30** (cold), 3.18 packets per agent, so **4 IBM jobs of about 20 s** from the measured 5 s one-job mission; 50 inputs, 1 unmeasured (packing beyond three circuits) | scripted (dry run) / modelled (ladder) |
| M1 economics | per verified record, the gateway mid-cost model versus self-hosted open models at dated GPU prices | M-1a | **MET** (conditional) | 400 agents: gateway **$0.063** per verified, **6.2 h** quota-bound; hosted full-size model on 12 H100s **$0.118** at $2.34 per GPU-hour and 50 % utilisation; batched 9 B **$1.72** per cycle with no measured verified rate | modelled |
| M2 GPU rental | one rented GPU runs the survey and one compounding cycle to measure $ per verified | M-2a / M-2b | **NOT RUN** | **0 GPU hours**; an owner line of about $25, at most 3 h, preregistered first | not run |
| M3 registry and routing | a weight-group registry, a model-agnostic PatchSpec (no weights), packet ops ROUTE = 8 and TRANSPORT = 9, and Q selection over (lead, model, variant) against a plain rule | M-3a / M-3b | **MET** | switched dry run: **40 ROUTE + 40 TRANSPORT**, **462** frames, 0 unexpected rejects, **10 of 10** ops, package PASS, switch off byte-identical; routing on 12 fixture cases: Q agrees with the plain rule **10 of 12**, equals the classical control **12 of 12**, **2,734.5 vs 2,763.6** modelled UVT per verified | scripted (dry run) / modelled (routing) |

**How the model lane is built.** A patch is a `ModelPatch v1`: exact deltas against the base weights with one stated intent from three failure classes (F1 loop: the reply hits the token cap; F2 invalid: schema or compile failure; F3 fabrication: the record compiles but its transitions are not supported by the evidence). A patch that touches more than 1 % of the weights is rejected before evaluation. The programmer sees only the 96 practice tasks. The evaluator holds the 36 unseen tasks and three adjacent suites of 40 (compile validity, family-B arithmetic, strict format) and runs as a separate subprocess; the lane seals the promotion receipt with a key kept out of the repository; the proposer never sees the unseen set or that key. The rule is fixed in advance: promote only if unseen verified rises by at least 4 of 36 (mean of 3 seeds) *and* no adjacent suite falls by more than one item *and* the token-cap rate does not rise. Otherwise the patch is rejected and the previous checkpoint stays authoritative. Every verdict is a sealed `PromotionReceipt`. None of this has run on the real model.

**Independent review.** Before anything could run, a read-only review of Experiment L against its contract found 0 critical, 4 high, 17 medium and 8 low findings, all applied. The one that mattered most: the programmer's sandbox could reach the repository, and with it the hidden tests and the answer tables. It now runs each block as an isolated subprocess on a copy of the runtime bundle with the repository off the import path, and every outbound message is checked against the unseen ids and their content fingerprints; a hit voids the cycle. The same review turned the package corruption test into a sweep of every byte and made the ladder derive IBM job counts from packets. A second review of the M diff found 0 critical, 3 high, 7 medium and 8 low, also applied, including the allow-list that keeps weights out of a PatchSpec.

**Economics, modelled.** At 400 agents the gateway mid-cost model costs about $0.063 per verified record and $25 per cycle, and the gateway's quota of 90 calls per hour sets the wall at 6.2 hours. A self-hosted full-size open model on 12 H100s at the dated mid rate of $2.34 per GPU-hour and 50 % utilisation costs about $0.118 per verified. That ranking is conditional and near a flip: the hosted option wins only if the gateway's per-call cost rises above 2,492 UVT (the in-situ projection is 1,579) or the H100 rate falls below **$1.25 per GPU-hour**; the dated range runs from $1.00 to $2.34. A batched 9-billion-parameter model is the cheapest per cycle at $1.72, but no hosted model has a measured verified rate, so no $ per verified exists for it; it must verify at least 6.8 % of records to break even. No token count for any hosted option has been measured; UVT is the proxy throughout.

**Q selection, read honestly.** On 12 fixture routing cases at one budget, Q selection agrees with the plain rule ("escalate after two cheap failures") on 10 and is about 1 % cheaper per verified (2,734.5 vs 2,763.6 modelled UVT). The whole difference is that Q sees the evidence-row count and the plain rule does not: a classical argmin-plus-knapsack control that sees the same factor makes exactly the same 12 choices. The plain rule with a row cutoff runs over budget and is not compared. The verify probabilities are an assumed model, not measurements. Weights never transfer between models; a PatchSpec carries intent, probes, evidence references and evaluation deltas, and the destination model re-derives the behaviour in its own sections under its own gate.

**Budget.** Model spend in L and M: **$0**; the ledger stands at **$42.50**. The owner raised the cap from $50 to **$75** on November 3 (harness stop $45 to $70). 0 new IBM seconds; 0 GPU hours. Tests at the pins: 174 (L) and 300 (L plus M), all passing offline.

**Pins.** Experiment L: [`b6d3ebb04d5d2fbaf054e6123bfcb614ca821e1b`](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b6d3ebb04d5d2fbaf054e6123bfcb614ca821e1b/docs/specs/predator/PREDATOR_QCOMMS_EXPERIMENT_L_MISSION_V1.md) on `feat/qcomms-l`, draft [PR #462](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/462); `bench/qcomms/l1_model_lane/PREREGISTRATION_L1.md`, `l2_control_packets/results/l2-gate-a.md`, `l3_research_package/results/l3-gate-a.md` and `l3-gate-a-package/manifest.json`, `l4_scale/results/l4-ladder.md` and `orchestrate-summary.md`. Experiment M: [`b384c5a5b54d3da41fb473a3cc3a2eeafc40c5e0`](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b384c5a5b54d3da41fb473a3cc3a2eeafc40c5e0/docs/specs/predator/PREDATOR_QCOMMS_EXPERIMENT_M_MISSION_V1.md) on `feat/qcomms-m`, draft [PR #463](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/463); `bench/qcomms/m1_economics/results/m1-ladder.md`, `m3_registry/results/m3-gate-a.json`, `m3-gate-b.md` and `dry-run/orchestrate-summary.md`. The JSON carries every figure under `experiments_l_m`.

## Remaining validation work

- **Model usefulness:** a bank of verified records now measurably raises first-try verification across rounds on fixture tasks (above). Still to qualify: models that use delivered records on *fresh*, non-fixture tasks, and the total inference, selection, verification and retry cost against cached ordinary delivery.
- **Model lane on the real model:** the harness is built, reviewed and rehearsed with a fake model; the baseline cycle, a first frontier-programmer cycle under its monthly allowance, and a paired compounding run with a promoted model have not run. No repair claim exists yet.
- **Hosted economics, measured:** every hosted-model figure is modelled; one preregistered GPU rental is needed to measure a verified rate and $ per verified for a self-hosted open model, and the flip points above are only as good as the dated prices and the assumed throughput.
- **Hardware inside a cycle:** no three-lane cycle has yet run with the IBM step inside it; the packets have been exercised offline through the same codec, and the 400-agent rung is modelled at 4 jobs of about 20 s. The ladder's next rungs (40 live, 400 classical, 400 with one IBM job) each need their own preregistration and an owner line.
- **Deepening on survivors:** the narrow-then-deepen comparison at matched budget on the hard family found above, with the first-tier worker gated on evidence size.
- **Different data:** test a corpus from another construction and preserve the fallback when the compact layout cannot represent an input.
- **Hardware economics:** packed requests now run on IBM hardware with billed savings measured at three circuits (2.0 vs 6.0 s) and the whole mission at one job (5.0 s). The ratio at 1,200 circuits and IBM's internal partitioning remain open; the two reserved attempts were finalized by IBM on November 2 (0 s and 5 s).
- **Timing and memory:** the latest host runs stayed below one hour, but calibration showed substantial per-core variability. The slowdown's precise cause remains unidentified. Use paired comparisons and report memory headroom before attributing small runtime changes to code.
- **Deployment and trust:** production dispatch and independent sandbox deployment need their own validation. Keyed receipt seals establish integrity under the configured shared-key trust model; they do not prove hardware execution or establish provenance against another key holder. A 32-bit tag is not a general security-strength guarantee.

## Current source records

The public numbers above are aggregate summaries. The following source links require private repository access; raw messages, keys and full execution artifacts are not published here. Source inspection is distinct from an independent rerun.

| Record | Frozen source |
| :--- | :--- |
| Experiment L: model lane harness, control packets, research package, scale model (built offline, not run) | [`b6d3ebb04d5d2fbaf054e6123bfcb614ca821e1b` · contract](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b6d3ebb04d5d2fbaf054e6123bfcb614ca821e1b/docs/specs/predator/PREDATOR_QCOMMS_EXPERIMENT_L_MISSION_V1.md), [L1 preregistration](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b6d3ebb04d5d2fbaf054e6123bfcb614ca821e1b/bench/qcomms/l1_model_lane/PREREGISTRATION_L1.md), [L2 gate](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b6d3ebb04d5d2fbaf054e6123bfcb614ca821e1b/bench/qcomms/l2_control_packets/results/l2-gate-a.md), [L3 gate](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b6d3ebb04d5d2fbaf054e6123bfcb614ca821e1b/bench/qcomms/l3_research_package/results/l3-gate-a.md), [L4 ladder](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b6d3ebb04d5d2fbaf054e6123bfcb614ca821e1b/bench/qcomms/l4_scale/results/l4-ladder.md), [L4 dry run](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b6d3ebb04d5d2fbaf054e6123bfcb614ca821e1b/bench/qcomms/l4_scale/results/orchestrate-summary.md), draft [PR #462](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/462) |
| Experiment M: hosting economics, registry, PatchSpec, ROUTE / TRANSPORT ops, Q-vs-rule routing (offline, modelled) | [`b384c5a5b54d3da41fb473a3cc3a2eeafc40c5e0` · contract](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b384c5a5b54d3da41fb473a3cc3a2eeafc40c5e0/docs/specs/predator/PREDATOR_QCOMMS_EXPERIMENT_M_MISSION_V1.md), [M1 ladder](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b384c5a5b54d3da41fb473a3cc3a2eeafc40c5e0/bench/qcomms/m1_economics/results/m1-ladder.md), [M3 gate A](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b384c5a5b54d3da41fb473a3cc3a2eeafc40c5e0/bench/qcomms/m3_registry/results/m3-gate-a.json), [M3 gate B](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b384c5a5b54d3da41fb473a3cc3a2eeafc40c5e0/bench/qcomms/m3_registry/results/m3-gate-b.md), [M3 dry run](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/b384c5a5b54d3da41fb473a3cc3a2eeafc40c5e0/bench/qcomms/m3_registry/results/dry-run/orchestrate-summary.md), draft [PR #463](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/463) |
| Experiment J close-out: hardware ladder, budgets, rejected items | [`c99594c26804d8801d6aec8ac590e7d2fa23b760` · REPORT_J](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c99594c26804d8801d6aec8ac590e7d2fa23b760/bench/qcomms/skt/REPORT_J.md), integration draft [PR #453](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/453) |
| J0 first hardware message and packing (ibm_fez) | [`c99594c2…` · REPORT_HW0_LIVE](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c99594c26804d8801d6aec8ac590e7d2fa23b760/bench/qcomms/hw0/REPORT_HW0_LIVE.md) |
| J5 full mission in 81 jobs (ibm_fez) | [`c99594c2…` · REPORT_J5_LIVE](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c99594c26804d8801d6aec8ac590e7d2fa23b760/bench/qcomms/hw0/REPORT_J5_LIVE.md) |
| J6 one-job first pass, gate not met (ibm_kingston) | [`c99594c2…` · REPORT_J6_LIVE](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c99594c26804d8801d6aec8ac590e7d2fa23b760/bench/qcomms/hw0/REPORT_J6_LIVE.md) |
| J7 one job at five shots, J8 two more datasets, J9 secret key (ibm_kingston) | [`c99594c2…` · REPORT_J7_LIVE](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c99594c26804d8801d6aec8ac590e7d2fa23b760/bench/qcomms/hw0/REPORT_J7_LIVE.md), [REPORT_J8_LIVE](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c99594c26804d8801d6aec8ac590e7d2fa23b760/bench/qcomms/hw0/REPORT_J8_LIVE.md), [REPORT_J9_LIVE](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c99594c26804d8801d6aec8ac590e7d2fa23b760/bench/qcomms/hw0/REPORT_J9_LIVE.md) |
| J11 second device, new secret, packing control, failed attempts (ibm_fez) | [`c99594c2…` · REPORT_J11_LIVE](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c99594c26804d8801d6aec8ac590e7d2fa23b760/bench/qcomms/hw0/REPORT_J11_LIVE.md) |
| J1 superposed records on hardware | [`c99594c2…` · REPORT_J1_LIVE](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c99594c26804d8801d6aec8ac590e7d2fa23b760/bench/qcomms/j1_multiplex/REPORT_J1_LIVE.md), [PR #451](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/451) |
| J10 typed-message qualification, J12 end-to-end chain | [PR #455](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/455), [`c99594c2…` · REPORT_J12](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c99594c26804d8801d6aec8ac590e7d2fa23b760/bench/qcomms/j12_e2e/REPORT_J12.md), [PR #456](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/456) |
| Hardware route and accounting gate (drafts) | AETHER-ATLAS [#182](https://github.com/AetherAI3/AETHER-ATLAS/pull/182), [#184](https://github.com/AetherAI3/AETHER-ATLAS/pull/184), [#185](https://github.com/AetherAI3/AETHER-ATLAS/pull/185); Nano #49–#54; Predator [#450](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/450) |
| Experiment I status, I1–I6 summaries and research-baseline adoption | [`43f2f8d863113670920da51c019794e1cf2aed37` · REPORT_I](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/43f2f8d863113670920da51c019794e1cf2aed37/bench/qcomms/skt/REPORT_I.md) |
| I6 repetitions, rescue drill and timing study | [`c090ec666beb15552c73600d57b3d78ae9c060ef` · REPORT_I6](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/c090ec666beb15552c73600d57b3d78ae9c060ef/bench/qcomms/skt/i6_3shot/REPORT_I6.md) |
| F2 fresh baseline, including rescue accounting | [`43f2f8d…` · REPORT_F2_cycle4](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/43f2f8d863113670920da51c019794e1cf2aed37/bench/qcomms/skt/f2_plan/REPORT_F2_cycle4.md) |
| H outcomes, including superposition and model limitations | [`43f2f8d…` · REPORT_H](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/43f2f8d863113670920da51c019794e1cf2aed37/bench/qcomms/skt/REPORT_H.md) |
| Exact product certificate and batch-planner audit | [`571c6e20183d3f926cd4ea144f7c813df7173f52` · compiler report](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/571c6e20183d3f926cd4ea144f7c813df7173f52/bench/qcomms/skt/compiler_planning/REPORT.md) |
| System2 draft | [AETHER-CLOUD #2168](https://github.com/AetherAI3/AETHER-CLOUD/pull/2168), reviewed head `8a45f120e10f0ed8719a26b13b4954aeca3765af` |

[Back to the current README overview →](../../README.md#gen3-quantum-comm-ops)

## Historical D–F snapshot

The October 28 public note is preserved below, including its then-current branch and queue statuses. It is a historical record; the current results and source records above supersede its status statements. Its resumed 303-plus-97-recipient milestone is separate from the later fresh missions.

<details>
<summary><strong>Read the October 28, 2026 public snapshot</strong></summary>

# Gen3 Quantum Comm Ops

**One mission, many agents, smaller messages.** Quantum Comm Ops studies how Predator can coordinate agent swarms through a compiled delivery plan, verifiable mailboxes, and a controller that concentrates information on promising candidates.

This is a public summary of the D → E → F hillclimb recorded on **October 26–27, 2026**, reviewed on **October 28**. Verification here means inspection of committed code, reports, and result records plus arithmetic checks. It does not mean an independent experimental rerun. The implementation and full run artifacts remain in the private research repository; [source pins](#source-pins) identify the exact versions inspected. [Public aggregate data](quantum-comm-ops.json) preserves the numbers and their scope.

## What problem does this solve?

Sending a complete mission prompt and every hint to every worker repeats information. Quantum Comm Ops explores a different delivery pattern: compile the common instructions once, send each agent a compact **shard**—its small piece of information—and use the results to decide who needs more detail next.

The intended use includes workers in different sandboxes. The current experiments demonstrate separate receiver processes and local mailbox files, not deployment across independently isolated operating-system sandboxes. Communication still uses ordinary service requests and files; “quantum” describes how the message is encoded and sampled, not an instant link between machines.

## How the mailbox works

1. **Compile the plan.** Assign a synthetic chain to each agent, pack its bits into jobs, and fix the tags, content digests, and resume map. A digest is a fingerprint used to recognize the same content again. This compiler is the master **C1** planning stage.
2. **Encode and sample.** Make the message the lowest-energy answer of a quantum-search problem. Predator builds the job; an authenticated Nano service compiles it; ATLAS samples it using FakeFez.
3. **Deliver and verify.** Check each recipient's receipt and message tag using the configured keys, reconstruct the message, and record the result. D2 exercised its receiver in a separate process; F2 checks each logical agent's mailbox against the compiled assignment. The runtime executes the plan instead of making new assignments.

**FakeFez is a simulator**, with a model of IBM-device behavior. The tested IBM-compatible service route used a zero-QPU budget. The receipt format's “hardware-sealed” label does not prove hardware execution: these are dry-run receipts authenticated with a shared symmetric key. A holder of that receipt key can produce a seal.

D2 completed **192/192 jobs** without transport refusal or retry. All eight channel/file pairs produced byte-identical model transcripts. This establishes delivery equivalence under the test conditions. Those models failed the task in both arms, so equivalent delivery does not establish useful reasoning.

## Adaptive CFC: send a little, learn, then focus

**Custom Fanout Controls (CFC)** sets three choices per round: the number of workers, the bits each receives, and the threshold for keeping a candidate. “Fanout” means how many workers get the task. In this benchmark, a winning candidate is a known answer in a synthetic task, not a verified vulnerability.

The default caps are **400 × 4 bits → 40 × 16 → 4 × 64**. The best measured configuration used **4 / 16 / 16 bits** instead. Across three random seeds, its actual worker counts were 400→29→4, 400→25→4, and 400→19→3. A seed makes a particular randomized test repeatable.

| F4 result | Evidence and meaning |
| :--- | :--- |
| Same winners, about 0.9% transmitted tokens | Cycle 5: **1,842 / 199,186 = 0.9248%**, pooled across three seeds. Scripted workers, synthetic 400-agent corpus, classical delivery stand-in, classical exact selection. Precision and recall both 1.0 on all three seeds. |
| Two selection rounds | Winners reached at **Q2**; a final **C3 confirmation** still ran. This is not two total processing stages. |
| Repeat without new sampling | Exact reruns had **100% cache hits and zero new shots**. Keys identify shard content and sampling settings. Other processing still exists; zero sampling is not zero total cost. |
| Transfer through the real service | Cycle 8: **40 agents, seed 0, 52/52 jobs verified** through Nano → ATLAS FakeFez. Decoded shards, selected candidates, plans, and cache outcomes matched the control. Two additional seeds were not run. |
| Smaller-run token limit missed | That 40-agent transfer used **154 / 6,846 = 2.2495%** estimated transmitted tokens, above its ≤2% target. It is a partial transfer result, not a full repeat of the 400-agent result. |

The 0.9% metric counts the compiled prompt once and estimates text/shard tokens. It does **not** count each model's actual prompt processing. In the separate Qwen 2.5 0.5B experiment, measured input tokens were **247,986 / 352,316 = 70.3874%** of baseline, and both precision and recall were zero. Effective model-prefix caching and a capable model are still unestablished here. Do not interpret 0.9% as a measured LLM billing ratio.

The production-code seam is behind `PREDATOR_CFC_ADAPTIVE=1`, unset by default. When enabled it is **advisory**: it records a plan beside the receipt without changing solver selection. The inspected production factory still refuses dispatch with `CFC_CODEPRO_SHARED_IR_UNWIRED`. The successful benchmark is not an enabled production swarm service.

## Capacity: useful information per sample

A **job** requests repeated samples; each sample is a **shot**. The early format spent a 12-bit identification tag on every 4 useful bits. The block format shares one 32-bit tag across a 96-bit chain, then splits the 128 bits into eight 16-bit jobs. That yields **12 useful bits per job on average**, including tag overhead.

| Metric | D2 baseline | F2 block scheme at 8 shots |
| :--- | ---: | ---: |
| Useful bits per chain | 96 | 96 |
| Jobs per chain | 24 | 8 |
| Useful bits per job | 4 | 12 |
| Shots per job | 256 | 8 |
| Useful bits per shot | 0.015625 | **1.5** |
| Jobs for a fresh 400-agent plan | 9,600 | **3,200** |

The improvement is **3× better packing × 32× fewer shots = 96×**. F2's committed cycle-3 completion confirms **1.5 useful bits per shot across 303 newly sampled agents and 2,424 jobs**. All 303 agents decoded successfully at eight shots; the other 97 agents in the completed 400-agent bank were sampled earlier at 256 shots. F1 separately verified all 72 chunks for three agents at each tested shot count: **8, 16, 32, 64, 128, 256**. These are measured results for this corpus and backend, not a universal reliability guarantee. All improvements are compiler, framing, and sampling changes in simulation; no hardware changed or ran.

### The 400-agent milestone

**Goal G is complete: 400/400 agents banked unique chains matching their assignments.** The compiler built the delivery plan from **400 unique 96-bit synthetic rule-machine chains**, pinned to a particular generated corpus. These are test messages, not 400 production security missions. [PR #391](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/391) now contains the completion report, ledger, plan, metrics, run summaries, and six worker logs. Recounting the committed ledger against the plan confirms **400 matches, 400 distinct chains, and zero duplicates or foreign chains**.

The resumed phase ran **303 agents × 8 jobs = 2,424 jobs**, using **19,392 shots** across six service instances. All jobs completed, all six workers exited successfully, and all 2,424 majority-decoded bitstrings matched their planned frames. There were **zero transport refusals or missing jobs**. The final bank combines these **303 newly decoded agents with 97 verified agents carried from cycle 2**. The useful information newly delivered was 29,088 bits: **29,088 / 19,392 = 1.5 bits/shot**.

The resumed run window was **3h30m49s**; acquiring the host lock through the last worker's finish took **3h33m16s**, the rounded **3h33** headline. This is the final phase's elapsed time, not the whole campaign. The run completed on October 27; its report was written on October 28 from retained artifacts because the launching session had stopped before completion. Individual job files and mailboxes remain on the research host; this review checks the committed records, not a fresh replay of those receipts.

The measured campaign total is **782 + 2,424 = 3,206 jobs** and **219,584 shots**, including the earlier 97 agents and partial work. The campaign-wide rate is **38,400 / 219,584 ≈ 0.175 useful bits/shot**. The **1.5** rate belongs to the improved cycle-3 scheme. A fresh 400-agent run entirely under that scheme would use **3,200 jobs and 25,600 shots**; that is a projection, not the job count of this resumed run.

The earlier **~20 hours** estimate belongs to the improved block plan on one service at 256 shots. The original 9,600-job baseline projects to **~61 hours** at the measured 22.7 seconds/job. Comparing 20h with 3h33 mixes a projection, different shot counts, concurrency, and carried work; it is not a measured end-to-end speedup ratio.

## Superposition multiplexing: several possible messages in one job

This is a separate track from block packing. It asks whether a circuit can place several message frames among its equally valid lowest-energy answers—a **degenerate ground-state set**—so repeated samples recover several recipients' messages. A shot produces one observed answer, not every message at once.

**QAOA** is the layered circuit method tested here. Its layer count, **p**, controls circuit depth and is separate from Crucible's C/Q research rounds. One layer was inadequate for the tested multi-frame construction. Deeper, tuned ideal circuits did much better:

| Experiment | Probability on desired answer set | Scope |
| :--- | ---: | :--- |
| F3, two frames, 20 layers | **0.904628** | Best single seed, ideal simulation; three-seed mean 0.8739. |
| F3, four frames, 12 layers, coupling weight 2 | **0.974073** | Best single seed, ideal simulation. |
| E1, two frames, 6 layers | **0.328** | Mean over three seeds with FakeFez noise. |
| E1, four frames, 4 layers | **0.253** | Mean over three seeds with FakeFez noise. |

These are probabilities on an answer set, not agent delivery-success percentages. The noisy QAOA sweep missed its 50% target, although decoding recovered every carrier in the tested cells from two layers onward. Its classical comparison performed better. Stronger couplings reduced required depth in some ideal settings; that benefit has not been established on hardware.

The current construction also limits independent content: **2^m frames carry only m+1 independent payloads**. Four frames therefore carry three independent payloads plus a forced parity frame, not four arbitrary messages.

The next preregistered noisy-depth test covers **6, 8, and 10 layers**. No result is committed at the reviewed F3 head; its model predicts a peak near eight layers but does not predict passing 50%. A pending test is not a measured improvement.

### The hillclimb continues

**October 28 status snapshot:** the owner reports additional **F4 controller seeds running**, **F3's noisy multiplexing runner staged** with an atomic lock-grab poller, and **F1's cycle-4 coding experiment preregistered and pushed**. The committed F1 log records the shared-host order **F4 → F3 → F1**; F2's close-out records the handoff to F4. F3's runner and frozen harness are committed. There are **no newly committed scored outcomes for these follow-ups** in this review, so the controller and multiplexing results above remain unchanged. The next updates depend on their completed reports.

## Limits the hillclimb exposed

| Area | What remains open |
| :--- | :--- |
| **Wider jobs** | Tested wider circuits were blocked by the ATLAS statevector dry run's memory needs; Nano also has a configurable width cap. This is a limit of the tested implementation and host, not a fundamental communication or device limit. |
| **Model use of hints** | The tested small models, including Qwen 2.5 7B under the frozen E2 prompt, failed to use the hint table. The 14B comparison did not run. This is not a claim about every small model or every prompt. Warm-up controls address Ollama's first-generation difference after loading. |
| **Confidentiality** | Tested keyless predictors recovered content only at chance; traffic and metadata remained visible. A holder of a message key can decode frames under that key. These tests are not a general security proof. |
| **Tags and ordering** | The D/E 12-bit tag is an identification check, not a security-strength authenticator. E3 found that its manifest index could be reordered without detection. F2's later whole-chain tag checks the reassembled block; the legacy format's issue must not be presented as universally fixed. |
| **Isolation and provenance** | Receiver-process guards are advisory, not OS sandbox boundaries. Shared receipt keys do not establish provenance against another holder. |
| **Hardware and advantage** | All results here are simulated or dry-run results. No IBM QPU was used and no quantum advantage was established. The separate [IBM Fez compiler pilot](ibm-fez-pilot.md) is a different experiment. |

## Source pins

The links below require access to **AETHER-PREDATOR-M**. They identify private source evidence; this public note and its JSON are an aggregate summary, not a public release of full run artifacts. The cited PRs were open at review; the original F2 and F1 PRs were drafts. The F lanes target `feat/qcomms-f`; **completion PR #391 targets F2's branch and is open and mergeable**, not yet merged. Results must be read at their individual heads rather than assumed merged. The ladder is `bench/qcomms/skt/f_ladder.md` on the respective branches. Runs and follow-ups have preregistrations and reports retain unmet or unestablished outcomes.

| Record | Pinned revision and files |
| :--- | :--- |
| D, PRs [#375](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/375) / [#376](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/376) | [`592b235ac921797df1a5f0d23936378ecfbd795e`](https://github.com/AetherAI3/AETHER-PREDATOR-M/blob/592b235ac921797df1a5f0d23936378ecfbd795e/bench/qcomms/skt/REPORT_D2.md): D2 report; `agents_llm.py` and `d2.py` for receipt and isolation behavior. |
| E, PR [#380](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/380) | [`4da32b6212ca1e5dd16cda7e7ec212ecebc7902a`](https://github.com/AetherAI3/AETHER-PREDATOR-M/tree/4da32b6212ca1e5dd16cda7e7ec212ecebc7902a/bench/qcomms/skt): `e1_depth/REPORT_E1.md`, `e2_models/REPORT_E2.md`, `e3_leakage/REPORT_E3.md`. |
| F4, PR [#384](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/384) | [`f75d00635c1c689b9dc05197a535f960eb7bb6e7`](https://github.com/AetherAI3/AETHER-PREDATOR-M/tree/f75d00635c1c689b9dc05197a535f960eb7bb6e7/bench/qcomms/skt/f4_cfc): cycle 5, 7, and 8 reports and result files; `predator/drive/cfc_adaptive_policy_v1.py`, `cfc_convergence_v1.py`, `cfc_production_factory_v1.py`. |
| F2, PR [#386](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/386) | [`a5aa6db4077380f7b0532d5f7ff2f9a146b7fa4c`](https://github.com/AetherAI3/AETHER-PREDATOR-M/tree/a5aa6db4077380f7b0532d5f7ff2f9a146b7fa4c/bench/qcomms/skt/f2_plan): `MISSION_LOG.md`, cycle 1 report, cycle 3 preregistration, compiler and block framing; `fixtures/skt/corpus.py`. |
| F2 completion, PR [#391](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/391) | [`655a5edc8aed37b43b66b75b759d787a1320a8c2`](https://github.com/AetherAI3/AETHER-PREDATOR-M/tree/655a5edc8aed37b43b66b75b759d787a1320a8c2/bench/qcomms/skt/f2_plan): `REPORT_F2_cycle3.md`, `MISSION_LOG.md` P11, and `results/cycle3/` ledger, plan, metrics, run summaries, and worker logs. |
| F1, PR [#389](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/389) | [`8815696e7cd99e823d1d44da4756ef31a4d4dd03`](https://github.com/AetherAI3/AETHER-PREDATOR-M/tree/8815696e7cd99e823d1d44da4756ef31a4d4dd03/bench/qcomms/skt/f1_width): cycle 1 and 2 reports. |
| F3, PR [#390](https://github.com/AetherAI3/AETHER-PREDATOR-M/pull/390) | [`2087aeb01bec9e3f4f822e2d1045222003c20cbb`](https://github.com/AetherAI3/AETHER-PREDATOR-M/tree/2087aeb01bec9e3f4f822e2d1045222003c20cbb/bench/qcomms/skt/f3_skt): cycle 1b report, result summary, cycle 2 preregistration and mission log; `../multiplex.py`. |
| F3 follow-up preparation | [`48ec000b75593e1226770a2dae3162e5f950cdae`](https://github.com/AetherAI3/AETHER-PREDATOR-M/tree/48ec000b75593e1226770a2dae3162e5f950cdae/bench/qcomms/skt/f3_skt): cycle 2 preregistration §7a, `c2.py`, and `run_c2_host.sh`; no completed cycle-2 report. |
| F1 follow-up preparation | [`931c21b5039acaa79b5e5ff9f237d4d20acb2bb5`](https://github.com/AetherAI3/AETHER-PREDATOR-M/tree/931c21b5039acaa79b5e5ff9f237d4d20acb2bb5/bench/qcomms/skt/f1_width): `PREREGISTRATION_F1_cycle4.md` and `MISSION_LOG.md` P3, including queue order; no completed cycle-4 report. |

[Back to the Quantum Comm Ops overview →](../../README.md#gen3-quantum-comm-ops)

</details>

