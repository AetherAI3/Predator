<p align="center">
  <a href="https://aethersystems.net/"><img src="docs/assets/aether-website-mark.svg" width="46" height="46" alt="Aether AI"></a><br>
  <strong>AETHER AI · SOFTWARE ANALYSIS &amp; SECURITY RESEARCH</strong>
</p>

<p align="center">
  <img src="docs/assets/readme-hero.svg" alt="PREDATOR — Reason deeply. Prove the result." width="100%">
</p>

<p align="center">
  <img src="docs/assets/predator-console.png" alt="Predator’s private operator console. The pictured session is illustrative, not a research result." width="100%"><br>
  <sub>Private operator console · Illustrative session, not research evidence.</sub>
</p>

<p align="center">
  <a href="#gen12--live-assurance"><img src="docs/assets/tag-gen12-live.svg" height="32" alt="Gen1–2: live assurance"></a>
  <a href="#gen3--push-the-reasoning-frontier"><img src="docs/assets/tag-gen3-research.svg" height="32" alt="Gen3: active research"></a><br>
  <a href="#gen4--replicate-the-gain-upgrade-the-profiles"><img src="docs/assets/tag-gen4-gated.svg" height="32" alt="Gen4: conditional roadmap"></a>
  <a href="#operator-controlled-by-design"><img src="docs/assets/tag-private-cli.svg" height="32" alt="Research CLI: private"></a>
</p>

**Understand the code. Model the threat. Verify the fix.**

Predator is Aether AI’s software analysis and security research program. We combine **frontier AI reasoning, adaptive compilation, and QUBO-based quantum optimization** to investigate how the next generation of tools can understand complex code, trace connected security risks, and verify ways to resolve them.

**Available today:** automated repository checks through **Predator CI / Aether Actions**. **Our research goal:** use repeated AI → quantum → AI steps to push analysis further, with each round building on verified evidence from the last.

<p align="center">
  <a href="https://aethersystems.net/actions"><img src="docs/assets/button-actions.svg" alt="Explore Aether Actions" width="270" height="64"></a>
  <a href="docs/research/generations.md"><img src="docs/assets/button-generations.svg" alt="Read the research roadmap" width="270" height="64"></a><br>
  <sub><a href="https://aetherai3.github.io/predator-cli/">Predator showcase</a> · <a href="https://aethersystems.net/defense-stack#defense-stack">Defense stack</a> · <a href="https://aethersystems.net/contact?intent=general&amp;product=aether_predator_cli&amp;cta=research_readme">Discuss an authorized engagement</a></sub>
</p>

> [!IMPORTANT]
> **Quantum advantage is a research goal, not an established result.** Gen3 is private research; Gen4 depends on independently reviewed findings. Neither is presented as a completed product upgrade.

## How the research works

| Approach | In plain language |
| :--- | :--- |
| **Frontier AI reasoning** | Advanced AI models examine code, trace how weaknesses connect, and propose solutions. |
| **Adaptive compilation** | Turn suitable unresolved questions into computational tasks, then update those tasks as new evidence arrives. |
| **QUBO-based optimization** | Model yes/no choices and their interactions so classical and quantum methods can search for promising combinations. |

**Quantum depth** means repeating the AI–quantum loop so a later step uses verified information from an earlier one—not simply building a longer circuit. Proposed fixes must be checked against the original software; a model’s confidence is not proof.

## From today’s product to tomorrow’s research

<a id="gen12--the-product-already-exists"></a>

### Gen1–2 · Live assurance

**Choose the checks. Review the result.** Gen1–2 established the AI and quantum-assisted research foundation behind today’s Predator Actions. Each action uses a *locked profile*: a fixed, versioned set of checks and execution rules.

<p align="center">
  <a href="docs/assets/flow-gen12-actions.svg"><img src="docs/assets/flow-gen12-actions.svg" alt="Connect a repository, choose a supported action, approve its usage, and review the checks, permitted fixes and evidence from Aether’s servers." width="100%"></a>
</p>

Aether checks whether the repository is supported before the customer approves **UVT usage—Aether’s usage credits**. The result identifies the code version and checks covered, with an evidence replay. Approval does not guarantee that every defect has been found.

<a id="gen3--push-the-reasoning-frontier"></a>

### Gen3 · Deeper software analysis

**Can each verified result make the next round of analysis more useful?** AI investigates the code; the compiler prepares a suitable quantum search; software tests check the proposed solutions. The evidence then guides the next round of AI reasoning and recompilation.

<p align="center">
  <a href="docs/assets/flow-gen3-research.svg"><img src="docs/assets/flow-gen3-research.svg" alt="Research goal, not a completed run: AI and Q1 propose solutions; software checks return evidence; that evidence guides AI, Q2 and later steps." width="100%"></a>
</p>

We compare progress with strong AI-only and classical methods under comparable budgets, studying when additional rounds help, level off or stop helping. Research covers **complex C++ software, database systems, and binary-format processing**. Specific benchmarks and private tests are not disclosed.

<a id="gen4--replicate-the-gain-upgrade-the-profiles"></a>

### Gen4 · From research to product

**Prove the benefit. Reproduce it. Then release it.** If Gen3 establishes an advantage, Gen4 tests whether it carries over to existing Cloud, Agent, Atlas, CLI and open-source assurance profiles. Deeper research continues alongside this work.

<p align="center">
  <a href="docs/assets/flow-gen4-transfer.svg"><img src="docs/assets/flow-gen4-transfer.svg" alt="Conditional roadmap: review Gen3 evidence, compare with previous profile versions, verify the improvement, and release approved updates through Aether Actions." width="100%"></a>
</p>

**Each profile must earn its own upgrade.** We compare it with the previous version and independently review the result. A new kind of check may need a new profile. Approved public replays should show the improvement, costs and limits without exposing customer code or private tests.

**[Read the detailed research and release guidance →](docs/research/generations.md)**

<a id="operator-controlled-by-design"></a>

## Access and safety

**Customers use approved Actions. Aether operates the private research engine.** Connecting a repository does not grant access to Predator’s research command-line tool (CLI), unrestricted research loops, internal profile settings or quantum hardware.

Code and infrastructure engagements require an agreed, authorized scope. Public replay means access to approved evidence—not control of the research system.

<details>
<summary><strong>View the generation map</strong></summary>

<p align="center">
  <img src="docs/assets/generation-roadmap.svg" alt="Gen1–2: existing assurance product. Gen3: active AI–quantum research. Gen4: future profile upgrades that require proven results. Arrows show goals, not achieved advantage." width="100%">
</p>

</details>

<details>
<summary><strong>🟣 Published hardware study · IBM Fez compiler pilot</strong></summary>

**September 6, 2026 · author-reported pilot.** The joint5 compiler reduced native two-qubit gates from **144 to 103 (28.5%)** in each of two related test cases. Four circuits ran at 1,024 shots each; recorded billed QPU time was 3 seconds.

| Distance from the ideal distribution ↓ | Ordinary | joint5 |
| :--- | ---: | ---: |
| Vulnerable test case | 0.395175 | **0.316523** |
| Fixed test case | 0.403859 | **0.307958** |

These total-variation distances improved, but the optimization score—expected energy—worsened. **One fixture, two related cases, one hardware job; no independent confirmation.** This does not establish better optimization, deeper reasoning or quantum advantage. It is not a Gen3 trial result.

[Full measurement note & uncertainty →](docs/research/ibm-fez-pilot.md) · [Full-precision results →](docs/research/ibm-pilot.json)

</details>

<details>
<summary><strong>🔴 Tools behind the research</strong></summary>

**Serena / Arbiter** develop and challenge proposed solutions. **Joint5, AQRC, Atlas and Crucible** support compilation, verification and the return of evidence to the next round.

[Nano](https://github.com/AetherAI3/Nano) provides structured workflow rules; [Unlimited Context](https://github.com/AetherAI3/Unlimited-Context-LLM) retains context; [Aether Protocol](https://github.com/AetherAI3/PROTOCOL-C) provides signed records to help detect changes to evidence. Signatures alone do not prove scientific claims.

<p align="center">
  <img src="docs/assets/workflow-pulse.gif" alt="Illustration of reasoning, computation and verification—not a recording of an experiment" width="100%"><br>
  <sub>Illustrative workflow, not a live experiment or evidence of advantage.</sub>
</p>

</details>

---

**Public overview and selected research notes. The proprietary CLI and backend remain private.** This README does not change research permissions or production profiles.

<sub>© 2026 Aether AI LLC. All rights reserved. IBM is identified as a hardware provider; no affiliation or endorsement is implied. <a href="docs/assets/SOURCES.md">Visual sources</a>.</sub>
