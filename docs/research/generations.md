# Predator generations

<a id="plain-english"></a>
## In plain English

These generation labels are Aether's own. They describe how Aether's own work has evolved. They are not an industry standard, and other teams use the same words to mean other things.

| Generation | What it means here |
| :--- | :--- |
| **Gen1** | Chat and copilot help. One model, one answer. |
| **Gen2** | Agent loops. Tool use, multi-step tasks, self-checks. Most public agent work today sits here. |
| **Gen3** (Aether now) | AI and quantum workflows run together across the Aether stack (Aether Agent, Aether Cloud, Nano, ATLAS, UCL, CodePro, AQRC, Predator). A shared, verified evidence bank with signed receipts. Swarm coordination of hundreds of small agents. Predator lanes for bounty, open-source (OSS), mission and training work. Predator is the public showcase. |
| **Gen4** | Conditional. See [What ends Gen3](#what-ends-gen3) and [Gen4, as far as we can see](#gen4). |

### What Gen3 means day to day

Aether does not train models from scratch. It builds the systems around models.

- **Weight adaptation.** A frontier model proposes an exact edit to at most 1 % of a small open-weight local model's weights. A separate judge, which the proposer never sees, scores the edit on hidden tasks. Only a clean gain with no collateral loss is promoted. Status on November 3, 2026: built and reviewed offline, not yet run on the real model.
- **API model systems.** CodePro, AQRC and Predator are built on hosted models through their APIs.
- **Local model modifications.** Small open-weight models run locally and would be adjusted through the weight-adaptation loop above (built, not yet run on a real model).
- **Quantum cybersecurity research.** The measured evidence so far: 400 agent briefings delivered through IBM quantum hardware in one job billed 5.0 seconds, 400 of 400 intact, with scripted agents. No quantum advantage has been shown. Details are in the [Gen3 quantum comm-ops section of the overview](../../README.md#gen3-quantum-comm-ops).

### Scale, stated plainly

The Quantum Comm Ops hardware missions had used 254 of the 600 seconds per period on IBM's open plan as of November 2, 2026. Model spend was about $42.50; the cap was raised to $75 on November 3, 2026. This is a small budget. Every run was gated by a preregistered pass/fail criterion written before the run.

<a id="what-ends-gen3"></a>
## What ends Gen3

No year is attached to Gen3. It is the default until one of three triggers fires. Each trigger is an observable, not a feeling.

1. **Predator shows a quantum route beating the best classical route on a security task.** The comparison must be preregistered, run on a matched budget, and reproduced by someone outside Aether. This has not been shown. Nothing in this repository claims it.
2. **Another team shows the same on a workload relevant to security research.** It will be cited here when it happens, not before.
3. **A lab demonstrates models that improve themselves without human-written training runs**, and the result holds up under independent review.

Another lab may reach Gen4 before Aether does. That is why this map is drawn now rather than inherited later. Aether's bet, stated as a hypothesis and not a result: hybrid AI + quantum workflows may matter before raw quantum hardware does. If that is right, the "date" cannot be read off quantum hardware roadmaps alone.

<a id="why-now"></a>
## Why now: the threat landscape

Public reports from model labs, platform vendors and standards bodies describe the environment this work sits in. Each item below links to the primary source, with its publication month.

- **Anthropic, "Disrupting the first reported AI-orchestrated cyber espionage campaign" (November 2025).** Reports a campaign detected in September 2025, attributed with high confidence to a state-sponsored group, in which Anthropic assesses the model carried out most of the operation with human involvement only at a few decision points. [anthropic.com/news/disrupting-AI-espionage](https://www.anthropic.com/news/disrupting-AI-espionage)
- **Anthropic, "Detecting and countering misuse of AI: September 2026" (September 2026).** Covers activity disrupted between December 2025 and August 2026 across seven harm areas, including cyber operations, influence operations, surveillance, scams and fraud, and illicit model distillation, and describes the role of AI in cyber operations as increasingly autonomous. [anthropic.com/threat-intelligence-report-september-2026](https://anthropic.com/threat-intelligence-report-september-2026)
- **OpenAI, "Disrupting malicious uses of AI" (February 2026).** Case studies of detected misuse in which threat actors typically combine AI with more traditional tools such as websites and social media accounts; the series hub lists further case studies through October 2026. [openai.com/index/disrupting-malicious-ai-uses](https://openai.com/index/disrupting-malicious-ai-uses/) · [series hub](https://openai.com/index/disrupting-malicious-uses-of-ai/)
- **Google Threat Intelligence Group, "AI Threat Tracker: From Prompting to Autonomy" (September 2026).** Covers Q2 2026 and reports that forward-leaning adversaries have moved "from basic prompting to agentic AI workflows and AI-enabled automation" (GTIG), including multi-agent frameworks used for scanning and credential harvesting. [cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai)
- **Microsoft, "Microsoft Digital Defense Report 2026" (2026).** Drawing on data from July 2025 to June 2026, it says AI is compressing attack timelines, lowering the cost of sophisticated capabilities and letting attackers operate with more speed, scale and autonomy, while the same capabilities help defenders. [microsoft.com/.../microsoft-digital-defense-report](https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/reports/microsoft-digital-defense-report/)
- **NIST, FIPS 203, 204 and 205 (August 2024).** The first three finalized post-quantum cryptography standards: ML-KEM for key establishment ([FIPS 203](https://csrc.nist.gov/pubs/fips/203/final)), ML-DSA for digital signatures ([FIPS 204](https://csrc.nist.gov/pubs/fips/204/final)) and SLH-DSA, a hash-based signature alternative ([FIPS 205](https://csrc.nist.gov/pubs/fips/205/final)). [nist.gov announcement](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips)

This is context for why Gen4 is being shaped early. It is not evidence about Predator.

<a id="gen4"></a>
## Gen4, as far as we can see

Everything in this section is intent, not measurement. No date is predicted. Gen4 starts when a trigger above fires.

**Defense first (near-term, real).**

- Post-quantum migration of the evidence bank's signatures and receipts to the NIST standards: ML-KEM (FIPS 203) for key establishment, ML-DSA (FIPS 204) and SLH-DSA (FIPS 205) for signatures.
- A "harvest now, decrypt later" exposure review: which stored or transmitted material would matter if recorded today and decrypted later.
- Quantum-safe verification of research packages, so that a package verified today still verifies after the migration.

**Authorized research.**

- Resource estimation: tracking published estimates of when quantum hardware becomes cryptographically relevant, so migration timelines rest on numbers rather than guesses.
- Testing post-quantum implementations for implementation flaws, within scoped, authorized engagements only.

**Workflows.**

- Carry the Gen3 loop (evidence bank, signed packets, swarm coordination, weight adaptation) onto whatever hardware or model generation exists at that time.
- The formal transfer gate below still applies. A Gen3 finding crosses into Gen4 only through that gate.

## The formal roadmap

#### Live assurance → private depth research → gated profile replication

Predator combines **adaptive compilation, advanced frontier-AI reasoning, and quantum-depth research** to advance **software analysis, vulnerability analysis, threat modeling, and resolution modeling**. The program investigates software failures, models possible consequences and evaluates changes against the behavior that must be preserved. Quantum depth refers to successive dependent quantum-method interventions; each campaign must identify whether those methods ran in simulation or on quantum hardware.

[← Predator overview](../../README.md) · [Completed Q3 result](charls-q3.md) · [Aether Actions](https://aethersystems.net/actions) · [Separate hardware pilot](ibm-fez-pilot.md)

> **Research posture:** Gen1–2 established the live assurance foundation. Gen3 explicitly pursues quantum advantage and investigates deeper AI–quantum reasoning chains. Gen4 is conditional: transfer qualifying findings into independently validated, locked Predator assurance profiles. No quantum-advantage result or Gen4 release is claimed by this roadmap. For the same material in plain language, including what would end Gen3, see [In plain English](#plain-english) above.

**Completed milestone, active program:** CharLS Q3 is Aether Predator’s first Gen3 dependent-repair win. The completed C0→Q1→C1→Q2→C2→Q3→C3 case reached **24/24 protected cases**, up from 16/24 at C2, with 16 prior passes preserved and eight gained. The producer reports native signature/lineage verification and durable C3 banking. This is a program milestone, not completion of Gen3 or a quantum-advantage result. The [public result note](charls-q3.md) distinguishes the recovered private replay from what readers can reproduce here.

### 1. Preserve the foundation

Gen1–2 encompass the frontier-AI and quantum-assisted Crucible lineage behind Predator’s locked assurance profiles, Cloud execution and replay through Predator CI / Aether Actions. The production product is not being reinvented as a quantum-computing service.

Historical executions remain part of the program record. Their existence and operational usefulness do not convert a disputed metric, a development fixture or a compiler-quality pilot into evidence of quantum advantage. In particular, the [published IBM pilot](ibm-fez-pilot.md) retains its original narrow scope and limitations.

Customer workflow remains:

```text
Connected repository → locked action → capability / eligibility precheck
→ approved UVT usage → bounded Aether server execution
→ verification / permitted remediation → scoped result and replay
```

Research CLI access, arbitrary loops, model-panel configuration, circuit settings and hardware operations are not customer controls. Private research remains Aether-operator-controlled; engagements remain contract- and scope-bound.

### 2. Gen3: study the mechanism and its limits

**Objective:** establish whether adaptive AI → quantum → AI recompilation can produce a verified advantage over competitive alternatives, and determine how useful progress changes with additional dependent interventions and resources.

In the completed case, C0–C3 label banked evidence checkpoints carried into frontier-AI reasoning, including the existing Serena / Arbiter process. They are not scores for a brute-force baseline. Conventional solvers remain necessary challengers alongside the primary AI-only comparison.

The completed CharLS chain now instantiates the loop through Q3; broader research continues under separately registered contracts:

```text
C0 → Q1 → native verification → AQRC → C1
   → adaptive recompilation → Q2 → native verification → C2
   → residual-directed Q3 → native PASS → C3 banked
```

The compiler should preserve relevant obligations, constraints and provenance while changing the representation of the unresolved problem. The bridge should carry verified information forward instead of replacing it with unsupported model assertions. In the completed Q3 case, the candidate and its parent binding changed; the compiler and decoder arithmetic remained unchanged and the catalog contained one candidate. The next research objective is attributable quantum advantage, not an automatic Q4.

Research targets include complex C++ systems, database/query processing and stateful binary-processing workloads. The owner-approved CharLS case summary publishes its identity, aggregate outcome, concise mechanism and selected fingerprints. Hidden inputs, patch bytes, private model configurations and campaign infrastructure remain private.

#### Three distinctions that stay explicit

| Concept | What it establishes |
| :--- | :--- |
| **Executed dependent Q-depth** | How many quantum interventions in one evidenced chain actually ran and satisfied the registered parent-dependence rules. Unrelated Q1 runs are not added together. |
| **Verified frontier progress** | Newly established outcomes under the fixed native acceptance contract. A sampled candidate, a new trace or a changed hash is not automatically a verified improvement. |
| **Advantage** | A scoped comparative result against credible alternatives, with the required accounting, uncertainty and replication. Depth alone does not establish it. |

Physical circuit depth is separate from reasoning-chain depth. The compiler may produce a shallower circuit at a later stage. A plateau may reflect saturation, an unsuitable intervention, noise, budget limits or bridge defects; it is not automatically a compiler failure.

#### Keep the study simple

Reuse Predator’s existing progression, separation-peak, stopping and replay mechanisms where their contracts apply. Do not add a separate dashboard, utility system or orchestration layer just to describe the study.

The compact record is: **depth, verified treatment utility, verified control utility, their difference, resource use, and stop reason**. For a registered utility `U`, the descriptive separation at depth `i` is:

```text
S_i = U(treatment_i) − U(control_i)
Incremental separation = S_i − S_(i−1)
```

These expressions do not replace a campaign’s sealed estimand. Fix utility, comparison budgets, primary endpoint, depth schedule and stopping rules before the confirmatory run. An observed best depth is a descriptive peak—not an unbiased advantage estimate selected after inspecting the same data. Confirm it on independent held-out material under a prospective policy.

Investigate sustained positive lift, accelerating lift, diminishing returns and falloff. Do not assume a scaling law from a short chain. Report where evidence ends rather than extrapolating an unobserved maximum depth.

### 3. Ratchet the bridge without rewriting the result

Use the existing breaker / builder loop on a frozen failed transition. First reproduce the defect: lost obligations, omitted evidence, invalid constraints, a misleading surrogate, a decoder mismatch or physical-compilation damage. Preserve a verified incumbent; do not overwrite it with an unverified candidate.

A changed graph or newly reachable path alone does not establish a quantum contribution. Require provenance from the preceding execution and test credible non-quantum routes to the same information. A classical continuation may reach the same state independently; that is comparison evidence, not a reason to hide the result.

For development, a small, budgeted compile portfolio may compare alternative representations under a declared selection rule. Its compilation, selection and verification costs are part of the accounting. More candidates do not receive free compute or privileged verifier information.

Keep native verdicts separate from model confidence and surrogate energy. In particular, failing one candidate does not justify excluding an entire unsampled region without an additional valid argument.

**A compiler fix starts a new versioned development attempt.** Do not repair a confirmatory run after seeing its result, retry the same depth secretly or move its budget/holdout. A residual-directed continuation from an authenticated C2 is Q3, prospectively bound to that parent; it does not replace Q2. Preserve the original evidence, then qualify any revision prospectively. A continuation beyond a frozen depth or budget requires a new authorized protocol; it does not silently extend an old seal.

### 4. What can cross from Gen3 into Gen4

Gen4’s advantage-transfer track opens only when Gen3 produces an independently reviewed result with a precise, defensible scope. A successful execution, positive development example or lower gate count does not open that gate by itself.

The handoff must identify the frozen engine and method; source and verifier identities; matched comparison; the claimed benefit and its uncertainty; resource accounting; replay material; retained negative results; and independent review/replication status. Simulation and hardware evidence must remain separately labelled. Simulated quantum routines run on classical hardware and do not, by themselves, demonstrate a quantum-hardware computational advantage.

Gen3 research continues after a qualifying handoff. Gen4 does not wait for the research program to finish, but neither does it assume that the advantage will transfer.

```text
Qualifying Gen3 evidence
          ├─ Gen3: deeper chains, limits and independent replication
          └─ Gen4: reproduce the effect on existing assurance workloads
```

No scientific priority, universal advantage, guaranteed scaling or completed-transfer claim follows from a roadmap. “First Gen3 repair win” identifies the completed milestone within Aether Predator’s program, not a first in the wider research field.

### 5. Gen4: reproduce against the last locked profiles

Target the existing Cloud, Agent, Atlas, CLI and open-source assurance families. Freeze the last locked profile as the baseline and prepare a separately versioned candidate using the qualifying Gen3 path.

Compare on the same declared source workload and acceptance contract, with prospectively comparable resources. Document verified findings and fixes, retained obligations, false positives/refutations, completion, runtime and cost. A different test corpus or extra verifier access cannot silently explain the claimed lift.

Every profile receives its own disposition:

| Disposition | Meaning |
| :--- | :--- |
| **Promote** | The candidate satisfies the profile’s preregistered improvement/no-regression requirements and passes replay, review and release gates. |
| **Retain baseline** | Benefit is absent, uncertain or accompanied by unacceptable regressions. |
| **Create a new locked profile** | The capability needs a different supported workload or assurance contract; it must not silently change the old profile’s promise. |

A research finding is not a blanket profile bump. Shared engineering improvements may be reviewed separately, but advantage language must stay tied to the evidence for the specific method, workload and comparison.

Hardware replication, where necessary and separately authorized, remains internal Aether research. It is not a user-selectable IBM backend or permission to submit arbitrary circuits.

### 6. Deliver through the existing product

The release path is **reviewed profile candidate → exact-source CI → native replay → protected release → bounded rollout through Predator CI / Aether Actions**. Preserve eligibility prechecks, user-approved UVT usage, server-side containment, profile versioning, rollback and audit records.

Publish a concise old-versus-new account of the result and an appropriate public replay example once publication is approved. A public replay should expose the reasoning/evidence structure and verification limits without disclosing customer source, secrets, protected evaluator material or arbitrary execution access.

“Replay” must say what was performed: evidence inspection, deterministic verification or a newly authorized execution. A visible replay is not permission for the viewer to operate Predator’s private research loops.

The public message after a successful transfer is an **upgrade to the existing assurance service**, not the launch of a general-purpose quantum tool.

### 7. Public disclosure boundary

This repository contains overview material, selected research notes and visual assets. Publish generation goals, bounded results, relevant uncertainty and approved replay examples. The owner has approved publication of the completed CharLS Q3 case identity, aggregate outcomes, concise fragment-advance mechanism, recorded Q2 selection summary and checkpoint/durability fingerprints. The owner also approved the GEN3 QPACK experiment #1 summary, its controlled-fault corpus identity, aggregate and paired outcomes, and sanitized stage/check fingerprints. [That exploratory result](gen3-qpack-experiment1.md) records 2/8 → 5/8 for AI_Q with feedback, with incomplete classical comparison and optimizer attribution unresolved. Public arithmetic and figures are rebuildable; full independent campaign reproduction still requires retained private materials. This approval does not authorize publication of other benchmark identities, hidden corpora, patch bytes, raw signed receipts, trust material, private infrastructure, account identifiers or research execution controls.

The Q3 figures and arithmetic are reproducible from the public JSON. Independent end-to-end reproduction of the private campaign is not enabled by this repository alone; the recovery, signature and lineage verification remain producer-reported from retained private materials. Historical Q2 remains `CHARLS_Q2_EXECUTED_NATIVE_FAIL`, Q3 is native PASS/C3 banked, and the separate hosted completion failure is preserved. Gen3 remains active with quantum advantage unestablished.

When a gate has not passed, say so. When a result is negative or fails to transfer, preserve it. **Reason deeply. Prove the result. Promote only what survives.**
