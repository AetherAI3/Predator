<p align="center">
  <a href="https://aethersystems.net/"><img src="docs/assets/aether-website-mark.svg" width="46" height="46" alt="Aether AI"></a><br>
  <strong>AETHER AI · PREDATOR</strong>
</p>

<p align="center">
  <img src="docs/assets/readme-hero.svg" width="100%" alt="Predator by Aether AI — Map the chain. Fix the risk. Prove the result.">
</p>

# Predator

**Understand the path. Fix what matters. Show the evidence.**

Predator is Aether AI's family of security tools and services. Its private CLI is the operator console: it directs a router to the right kind of analysis for the job. A focused code fix, a repository check, deep software research, and a live red-team engagement have different scopes and use different methods. Predator can draw on more than one quantum approach; no single research result proves every service.

This public repository explains the work and shares selected research records. It does not contain the private engines or give access to run an engagement.

## Attack-chain coverage

The [Predator Red Team overview](https://aethersystems.net/defense-stack) lists **359 modeled chains** across the MITRE ATT&CK Enterprise tactics, plus an Aether category for attacks on AI workflows. The chain library helps plan an assessment; it does not mean 359 findings in a customer system.

| Part of a chain | What Predator maps |
| :--- | :--- |
| **Find a way in** | Reconnaissance, resource development, and initial access |
| **Establish access** | Execution, persistence, privilege escalation, and defense evasion |
| **Move through a system** | Credential access, discovery, and lateral movement |
| **Reach an objective** | Collection, command and control, exfiltration, and impact |
| **Assess AI workflows** | Prompt, retrieval, context, tool-use, and model-behavior attacks; this is Aether's extension, not an ATT&CK tactic |

The actual coverage in any job depends on the assets and methods the owner authorizes. A possible chain becomes a finding only when the relevant behavior is checked and supported by evidence.

## The CLI, Crucible, and the research loop

The Predator CLI is the **operator console and router**. For deep software analysis, it directs work through Crucible. Crucible starts with a *frozen corpus*: a named source revision, a defined problem, and checks that cannot be quietly changed to make a result look better. It investigates bugs and vulnerabilities, compares known vulnerable code with the fixes that resolved it, and searches for zero-day vulnerabilities and deeper chains.

The compounding loop is easy to describe even when the work behind it is complex:

**Frontier model → ATT&CK chain hypotheses → Q1 search → Jev candidate triage → native check → frozen classical comparison → Q2 search → new evidence → repeat.**

[Jev](https://docs.typesafe.ai/introduction) is TypeSafe AI's decision model. It can help route or score candidates; it does not verify a vulnerability. A native check records what happened, including a failed attempt. That evidence becomes the next starting point, so later searches can push a known chain deeper or test a new path. In the published Gen3 work, the saved checkpoints and interventions are written **C0 → Q1 → C1 → Q2 → C2 → Q3 → C3**. A Q step is a quantum-method intervention; it does not necessarily run on a quantum processor.

**We have not published a fresh, previously undiscovered CVE finding.** Zero-day discovery is an active research lane, not a claim about the public results below. We are continuing matched classical and quantum research to test whether the quantum component provides an advantage.

The public record is promising but narrow. In one controlled CharLS repair case, the final step moved from **16/24 to 24/24** protected tests, keeping all earlier passes. In an exploratory QPACK study, the feedback variant found **5/8 controlled faults**, versus **2/8** for its no-feedback control. These were controlled faults, not new customer vulnerabilities or CVEs. Neither result proves quantum advantage or a measured Jev contribution. [Read the CharLS result](docs/research/charls-q3.md) and [the QPACK study](docs/research/gen3-qpack-experiment1.md).

## Live Predator Red Team

A live engagement is a separate, operator-led path. With the owner's permission, the team uses open-source intelligence (OSINT), network reconnaissance, and adversary tactics, techniques, and procedures (TTPs) to build and test plausible paths through the agreed environment. Findings are reviewed and handed over with evidence and remediation guidance.

This lane uses a **different quantum approach** from Crucible's software research. Aether describes its live-engagement method as a **patent-pending fractal model run on IBM Quantum hardware**. The [Red Team page](https://aethersystems.net/defense-stack) describes the hardware-assisted selection and engagement scope. The separate [public IBM Fez pilot](docs/research/ibm-fez-pilot.md) in this repository is a compiler experiment; it is not evidence that a customer engagement or Crucible's CharLS result used that pilot.

Live testing needs a bounded contract and a longer approval process. The owner and operator agree on targets, permitted methods, timing, contacts, and stop conditions before work begins. The [published process](https://aethersystems.net/defense-stack) allows **2–4 weeks of scoping before testing**.

## Ways to work with Aether

| Path | When it fits | Public terms |
| :--- | :--- | :--- |
| **Predator Strikes** | A known CVE fix, focused discovery, bug fix, CI/build repair, or another clear repository task | The [AetherAI3 profile](https://github.com/AetherAI3#predator-strikes) lists **$199 Known CVE Fix**, **$299 Predator Discovery**, and **$499 Deep Discovery** for one authorized repo. Broader work is [quoted by scope](https://aethersystems.net/strikes/). |
| **Predator CI** | A repeatable security check for an eligible repository and exact commit | The profile lists **$39/month per qualified repo plus hosted usage credits**, in private preview. Aether works with each team to [qualify an assurance profile](https://aethersystems.net/actions/design-partner). |
| **Predator Red Team** | An authorized assessment of a live environment | The [Red Team page](https://aethersystems.net/defense-stack) lists **$4,500** for one scoped assessment, **$8,500/month** for up to four, and custom enterprise terms. |

A Strike is a focused contract with a clear handoff, not an automatic red-team authorization. The [current Strikes page](https://aethersystems.net/strikes/) also offers broader development and repair work; its listed amounts are starting deposits toward a quoted total. Scope, price, schedule, and what can be verified are agreed before payment.

### Join the early Gen3 and Predator CI conversation

We are looking for a small number of teams interested in how Predator CI develops. You would work directly with Aether to identify one useful repository surface, discuss the checks that matter, and understand what a qualified profile could cover. We will explain what ran, what passed, and what remains outside the check. There is no need to operate the research CLI yourself.

[Talk with Aether about a Predator CI profile →](https://aethersystems.net/actions/design-partner)

## Developers: join the research program

We also welcome developers who want to help advance the research itself. Work can include the CLI, repair chains, verification tools, and careful classical/quantum comparisons. Tell us what you have built and which part of the program interests you.

Aether reviews applications and grants access to relevant private work areas only after approval. This is a development and research opportunity, separate from a customer red-team engagement.

[Apply to join the research →](https://aethersystems.net/contact?intent=general&product=site_wide&cta=footer_updates_contact)

## Read the evidence

- [CharLS Q3 result](docs/research/charls-q3.md) and [public data](docs/research/charls-q3.json): the completed dependent repair and its limits.
- [Gen3 QPACK study](docs/research/gen3-qpack-experiment1.md) and [episode data](docs/research/gen3-qpack-experiment1.json): feedback results, comparisons, and missingness.
- [IBM Fez pilot](docs/research/ibm-fez-pilot.md): a separate hardware measurement with mixed outcomes.
- [Research roadmap](docs/research/generations.md): what must be shown before research moves into a customer profile.
- [Safety model](SAFETY.md): the boundaries required for long-running research agents.

Predator research runs only within an approved scope. A model suggestion, a mapped chain, and a passing repository profile are different kinds of evidence; none is a guarantee that every vulnerability has been found.

<p align="center"><sub>Public overview and selected research notes · Private operator engines<br>© 2026 Aether AI LLC. All rights reserved. IBM is identified as a hardware provider; no affiliation or endorsement is implied. <a href="docs/assets/SOURCES.md">Visual sources</a>.</sub></p>
