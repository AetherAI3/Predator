<p align="center">
  <a href="https://aethersystems.net/"><img src="docs/assets/aether-website-mark.svg" width="46" height="46" alt="Aether AI"></a><br>
  <strong>AETHER AI · SOFTWARE ANALYSIS &amp; SECURITY RESEARCH</strong>
</p>

<p align="center">
  <img src="docs/assets/readme-hero.svg" width="100%" alt="Predator by Aether AI — Reason deeply. Prove the result. AI reasoning, adaptive compilation and software verification.">
</p>

<p align="center">
  <a href="#start-here"><img src="docs/assets/tag-actions-profiles.svg" height="32" alt="Aether Actions: locked profiles"></a>
  <a href="#research-loop"><img src="docs/assets/tag-gen3-private.svg" height="32" alt="Gen3: private research"></a><br>
  <a href="#published-quantum-data"><img src="docs/assets/tag-hardware-pilot.svg" height="32" alt="Hardware: published compiler pilot"></a>
  <a href="#generation-map"><img src="docs/assets/tag-gen4-gated.svg" height="32" alt="Gen4: conditional roadmap"></a>
</p>

<p align="center">
  <a href="#start-here"><strong>Start here</strong></a> &nbsp; · &nbsp;
  <a href="#published-quantum-data"><strong>Quantum data</strong></a> &nbsp; · &nbsp;
  <a href="#research-loop"><strong>Research loop</strong></a> &nbsp; · &nbsp;
  <a href="#access-and-scope"><strong>Access</strong></a>
</p>

**Understand the code. Model the problem. Check the result.**

Predator is Aether AI’s software analysis and security research program. It brings together **AI-assisted investigation, adaptive compilation and verification on real software**. Supported customer checks run through **Predator CI / Aether Actions**; the research CLI and backend remain private.

This public repository contains the showcase, research guidance and selected measurement notes. It is not an installable distribution of the research engine.

## Start here

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Use supported checks</h3>
      <p>Connect a repository, choose a supported action and review the permitted scope before approving usage.</p>
      <p><a href="https://aethersystems.net/actions"><strong>Explore Aether Actions →</strong></a></p>
    </td>
    <td width="50%" valign="top">
      <h3>Explore the research</h3>
      <p>See the published hardware measurements, the reasoning-loop hypothesis and the evidence needed for future upgrades.</p>
      <p><a href="docs/research/generations.md"><strong>Read the research roadmap →</strong></a></p>
    </td>
  </tr>
</table>

**Check coverage first.** Predator Security requires an approved assurance profile. The [current product page](https://aethersystems.net/actions) lists AetherCloud backend coverage; customer-specific profiles are private preview. Hosted Build &amp; Test is a separate Actions service.

<p align="center">
  <a href="https://aetherai3.github.io/predator-cli/">Visual showcase</a> &nbsp; · &nbsp;
  <a href="https://aethersystems.net/defense-stack">Aether defense stack</a> &nbsp; · &nbsp;
  <a href="https://aethersystems.net/contact?intent=general&amp;product=aether_predator_cli&amp;cta=research_readme">Discuss an authorized engagement</a>
</p>

## Published quantum data

**IBM Fez · September 6, 2026 · author-reported compiler pilot**

The **joint5** compiler reduced native two-qubit gates from **144 to 103 per circuit — 28.5% fewer gates**. The measured output also moved closer to the fixed ideal distribution in both related test cases.

<p align="center">
  <a href="docs/research/ibm-fez-pilot.md"><img src="docs/assets/readme-hardware-data.svg" width="100%" alt="Published IBM Fez pilot. Ordinary compilation in blue and joint5 in purple: 144 to 103 native two-qubit gates. Output-distribution distance decreased in both cases. Expected energy increased, which is worse for the objective. One fixture, four circuits, one hardware job; no independent confirmation."></a>
</p>

| Published measure | Ordinary | joint5 | Interpretation |
| :--- | ---: | ---: | :--- |
| Native two-qubit gates, each circuit | 144 | **103** | **28.5% fewer** |
| Output distance · vulnerable case | 0.395175 | **0.316523** | Closer to ideal ↓ |
| Output distance · fixed case | 0.403859 | **0.307958** | Closer to ideal ↓ |
| Expected energy · vulnerable case | −2.345352 | −2.013768 | Higher; minimization worsened ↑ |
| Expected energy · fixed case | −2.366837 | −1.954590 | Higher; minimization worsened ↑ |

**What that means:** fewer gates and better agreement with the fixed ideal output in this acquisition. **It did not improve the optimization objective.** Output distance is total-variation distance; lower is better. Expected energy is the objective score being minimized.

**Scope:** one six-variable fixture, two related cases, four circuits at **1,024 shots each**, one hardware job and **3 seconds of recorded billed QPU time**. That billed time is not end-to-end runtime. The cases are not independent confirmations. This pilot is separate from Gen3 depth trials and establishes no quantum advantage.

**[Measurement note and uncertainty →](docs/research/ibm-fez-pilot.md)** &nbsp; · &nbsp; **[Full-precision public data →](docs/research/ibm-pilot.json)**

## Research loop

<a name="how-the-research-works"></a>

**Can verified feedback make the next round of reasoning more useful?** That is the Gen3 question.

| Step | What it does |
| :--- | :--- |
| **Reason about the code** | AI examines behavior, traces connected risks and proposes repair hypotheses. |
| **Compile the unresolved choice** | Express suitable decisions and constraints as a QUBO: yes/no choices with interaction costs. |
| **Compare and check** | Classical or quantum methods propose candidates; tests on the original software determine their outcomes. |
| **Carry evidence forward** | Use the verified result and remaining obligations to prepare the next intervention. Preserve negative results. |

<p align="center">
  <a href="docs/research/generations.md"><img src="docs/assets/flow-gen3-research.svg" width="100%" alt="Conceptual Gen3 research loop, not an execution record: AI, Q1 and software checks feed evidence into AI, Q2 and later interventions under the registered stop rule."></a>
</p>

**Reasoning-chain depth counts dependent interventions; circuit depth measures a different thing.** The research plan calls for competitive AI-only and classical comparisons, declared budgets and native acceptance criteria. Simulation and hardware evidence are recorded separately. More rounds, lower surrogate energy or a changed graph do not establish an advantage on their own.

> [!NOTE]
> **Quantum advantage remains a research goal.** The published hardware pilot measures compiler behavior. It does not establish deeper software reasoning, a Gen3 advantage or a completed Gen4 upgrade.

## Generation map

<a name="from-todays-product-to-tomorrows-research"></a>
<a name="gen12--live-assurance"></a>
<a name="gen12--the-product-already-exists"></a>
<a name="gen3--push-the-reasoning-frontier"></a>
<a name="gen3--deeper-software-analysis"></a>
<a name="gen4--replicate-the-gain-upgrade-the-profiles"></a>
<a name="gen4--from-research-to-product"></a>

| Generation | Role in the program | What a reader should expect |
| :--- | :--- | :--- |
| **Gen1–2 · Assurance foundation** | The foundation behind locked Predator Actions profiles | Supported checks, approved usage and scoped evidence |
| **Gen3 · Private research** | Study dependent AI–quantum reasoning and its limits | Prospectively defined comparisons; results bounded by their evidence |
| **Gen4 · Conditional transfer** | Reproduce qualifying findings against earlier profile versions | Independent review and a separate release decision for each profile |

A **locked profile** is a fixed, versioned set of checks and execution rules. Repository eligibility is checked before the customer approves **UVT usage — Aether’s usage credits**. Results identify the code version and checks covered. Passing a profile does not mean every defect has been found.

**Each upgrade must earn its own release.** Gen4 depends on qualifying, independently reviewed Gen3 evidence and successful profile-level replication. Read the [generation and release guidance](docs/research/generations.md) for the comparison, preservation and stopping rules.

## Access and scope

<a name="operator-controlled-by-design"></a>
<a name="access-and-safety"></a>

**Customers use approved Actions. Aether operates the private research engine.** Connecting a repository does not expose the research CLI, arbitrary loops, internal model settings or quantum hardware controls. Engagements require an agreed, authorized scope.

Public replay provides approved evidence for inspection; it does not grant research-execution access. This repository publishes selected summaries, not customer code, current private benchmark details or raw acquisition bundles.

<details>
<summary><strong>View the private operator console · illustrative</strong></summary>

<p align="center">
  <img src="docs/assets/predator-console.png" width="100%" alt="Owner-supplied image of the private Predator operator console. Its session and counters are illustrative, not research measurements."><br>
  <sub>Private operator console · The pictured session is illustrative, not a research result.</sub>
</p>

</details>

<details>
<summary><strong>Explore the tools behind the research</strong></summary>

**Serena / Arbiter** develop and challenge proposals. **Joint5, AQRC, Atlas and Crucible** support compilation, verification and the return of evidence to later reasoning.

[Nano](https://github.com/AetherAI3/Nano) supplies structured workflow rules. [Unlimited Context](https://github.com/AetherAI3/Unlimited-Context-LLM) retains context. [Aether Protocol](https://github.com/AetherAI3/PROTOCOL-C) provides signed records that help detect changes to evidence. Signatures establish integrity within their trust assumptions; they do not independently prove a scientific claim.

</details>

## Read the evidence

| Resource | What is available |
| :--- | :--- |
| [IBM Fez measurement note](docs/research/ibm-fez-pilot.md) | Setup, both outcomes, sampling uncertainty and limitations |
| [Public numerical record](docs/research/ibm-pilot.json) | Full-precision values and retained-artifact fingerprints |
| [Research and release roadmap](docs/research/generations.md) | Generation boundaries, comparisons and promotion criteria |
| [Visual showcase](https://aetherai3.github.io/predator-cli/) | Designed public overview |
| [README consistency review](docs/readme-consistency-review.md) | Claim, link, rendering-structure and disclosure checks for this revision |

---

<p align="center"><strong>Reason deeply. Prove the result. Promote only what survives.</strong></p>

<p align="center"><sub>Public overview and selected research notes · Proprietary research CLI and backend<br>© 2026 Aether AI LLC. All rights reserved. IBM is identified as the hardware provider; no affiliation or endorsement is implied.<br>Badges are editorial labels, not live CI or validation indicators. <a href="docs/assets/SOURCES.md">Visual sources</a>.</sub></p>
