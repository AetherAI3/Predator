# Hack The Box with Predator

A guide to the public HTB training collection: completed modules, track progress, machines, certificates, and recorded Predator work.

Start with [Academy](academy/README.md) for an example of Predator working in an owned VM. Explore [Satellite Exploitation](satellite-exploitation/README.md) for a completed track and its certificate, [AI and ML Exploitation](ai-ml-exploitation/README.md) for work in progress, or [Machines](machines/README.md) for individual lab records.

## Modules and tracks

*Status snapshot: October 5, 2026.*

| Area | Recorded progress | What you will find |
| :--- | :--- | :--- |
| **[Satellite Exploitation](satellite-exploitation/README.md)** | **9/9 labs completed** · October 5, 2026 | Certificate, nine-lab list, a combined replay, and two individual replays |
| **[AI and ML Exploitation](ai-ml-exploitation/README.md)** | **1/17 labs HTB-accepted** · in progress | Status for all 17 labs and three recorded replays |
| **[HTB Academy](academy/README.md)** | **Nmap module completed: 12/12 sections** · October 3, 2026 | Completion record, model/owner roles, Nmap replay, and earlier Pwnbox preview |

## Machines

| Machine | Recorded result | What you will find |
| :--- | :--- | :--- |
| **[BlockSynergy](machines/blocksynergy/README.md)** | **User and root challenge files read** · October 5, 2026; owner confirmed | Execution roles and a sanitized six-frame replay |
| **[Ghostlink](machines/ghostlink/README.md)** | **User and root challenge files read** · October 5, 2026; HTB submission unobserved | Full-screen VPS3 pwnbox replay and execution-role notes |

## Choose a replay

The GIFs are **assembled evidence replays** made from saved records. Some contain challenge answers; each track page explains the available evidence and execution roles.

| Replay | What it covers |
| :--- | :--- |
| **[Satellite overview](satellite-exploitation/combined-replay.gif)** | Four saved lab records and the completion certificate |
| [Baby Frame](satellite-exploitation/baby-frame-replay.gif) · [No Errors](satellite-exploitation/no-errors-replay.gif) | The two individual Satellite source replays |
| [Prometheon](ai-ml-exploitation/prometheon-replay.gif) · [Lost in Hyperspace](ai-ml-exploitation/lost-in-hyperspace-replay.gif) · [Spin Glass Brain](ai-ml-exploitation/spin-glass-brain-replay.gif) | Three AI/ML examples; the track guide distinguishes recovered candidates from HTB acceptance |
| [BlockSynergy](machines/blocksynergy/predator-replay.gif) | Sanitized machine replay of GLM chain research and operator-verified user/root access |
| [Ghostlink](machines/ghostlink/predator-pwnbox-replay.gif) | Sanitized full-screen VPS3 pwnbox replay; the guide separates model work from operator verification |
| **[Academy Nmap](../media/predator-vpn-scan-preview.gif)** | Sanitized autonomous GLM-5.3 VM command work |
| [Earlier Pwnbox preview](../media/predator-pwnbox-ttl-preview.gif) | Console attachment and a reviewed guest-terminal exercise |

## How to read the results

**Completion** comes from the recorded HTB acceptance, owner-provided activity, or certificate described on each page. **Saved Predator work** shows the execution evidence retained for that lab. The model and operator roles vary by example.

The Satellite [achievement](https://labs.hackthebox.com/achievement/track/4038252/99) and [certificate](satellite-exploitation/certificate.png) support completion of nine labs; the saved Predator record covers four. In AI/ML, a recovered candidate counts toward completion only once HTB acceptance is recorded. The Academy record attributes VM command execution to Predator/GLM-5.3 and answer entry to the owner. The BlockSynergy and Ghostlink pages distinguish GLM research from operator execution. Ghostlink's live flag reads are recorded without claiming an observed HTB account submission.

<details>
<summary><strong>Updating this collection</strong></summary>

Add results to the relevant track or machine page with the date, execution roles, and acceptance evidence. Update the progress tables here and the [main README](../../README.md#hack-the-box-modules-and-demos). Link reviewed replays in the index above.

The [media manifest](media-manifest.json) records each asset's SHA-256 hash, byte size, and GIF frame count. Refresh it with `update_media_manifest.py` when media changes. Keep challenge archives, live endpoints, credentials, VPN material, and private task bundles outside the public collection.

</details>

[Back to Predator →](../../README.md#hack-the-box-modules-and-demos)
