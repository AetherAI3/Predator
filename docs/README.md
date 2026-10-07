# Predator docs and public evidence

Start with the [Predator overview](../README.md), browse the [HTB demo collection](htb/README.md), or inspect a published research result below.

The [redacted P-BOX replay](pbox-vercel-ai-sdk-showcase.md) shows the actual terminal during a local Vercel AI SDK security test while blurring private commands and finding details.

This is the public documentation and evidence repository for Aether's AI security research and software repair program. The CLI and operator engines have a separate reviewed access path.

## Research results

| Record | What it covers | Public data |
| :--- | :--- | :--- |
| [CharLS Q3 repair](research/charls-q3.md) | Dependent repair: 16/24 → 24/24 protected passes, with all earlier passes retained | [Result JSON](research/charls-q3.json) |
| [QPACK feedback study](research/gen3-qpack-experiment1.md) | 5/8 controlled faults found with feedback, versus 2/8 without it; incomplete adaptive classical comparison | [Episode JSON](research/gen3-qpack-experiment1.json) |
| [joint5 IBM Fez pilot](research/ibm-fez-pilot.md) | Fewer native two-qubit gates and closer output agreement; worse expected energy | [Measurement JSON](research/ibm-pilot.json) |
| [Research roadmap](research/generations.md) | Quantum depth, matched comparisons, and the requirements for qualifying later profiles | — |

The studies use controlled fixtures or deliberately introduced faults. Quantum advantage remains an active research objective. Each result page explains its evidence and reproduction limits.

[View the public research site →](https://aetherai3.github.io/Predator/)

## Hack The Box training

| Guide | Recorded result |
| :--- | :--- |
| [All HTB modules and replays](htb/README.md) | Collection guide and complete replay index |
| [Satellite Exploitation](htb/satellite-exploitation/README.md) | 9/9 labs completed; certificate and saved Predator work for four labs |
| [AI and ML Exploitation](htb/ai-ml-exploitation/README.md) | 1/17 labs HTB-accepted; track in progress |
| [HTB Academy](htb/academy/README.md) | Nmap module: 12/12 sections; autonomous GLM-5.3 VM commands and owner answer entry |
| [HTB machines](htb/machines/README.md) | BlockSynergy and Ghostlink: saved work, observed results, and execution roles |
| [Academy completion record](research/htb-academy-nmap.md) | Detailed attribution, provenance, and replay limits |

The collection includes assembled evidence replays and a recorded pwnbox capture. Each guide explains the media provenance, HTB acceptance, and model/operator roles.

## Safety and participation

- [Predator safety model](../SAFETY.md): required boundaries and implementation status.
- [When shared state becomes authority](papers/when-shared-state-becomes-authority.md): the research note behind the long-running agent threat model.
- [Contributing guide](../CONTRIBUTING.md): documentation corrections, evidence updates, and research feedback.
- [Security reporting](../SECURITY.md): private reporting for sensitive concerns.
- [Community guidelines](../CODE_OF_CONDUCT.md): expectations for public participation.

<details>
<summary><strong>Media and publication notes</strong></summary>

[Visual sources and attribution](assets/SOURCES.md) · [HTB media manifest](htb/media-manifest.json)

The [Q3 publication review](readme-consistency-review.md) and [its checks](readme-consistency-checks.json) describe their dated publication snapshot. Use the current result pages for current public claims.

</details>

[Back to Predator →](../README.md)
