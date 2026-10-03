# HTB Academy: Network Enumeration with Nmap

**Completed October 3, 2026 · All 12 module sections**

Predator, using GLM-5.3, autonomously performed the VM command work for Hack The Box Academy's **Network Enumeration with Nmap** module. The owner supplied plain-language prompts and the HTB exercise questions, then typed the resulting answers into Academy. An owner-provided Academy screenshot shows the module completion dialog, and an earlier screenshot shows the Hard Lab answer's success notification.

![Sanitized replay of Predator's autonomous Academy Nmap enumeration through GLM-5.3](../media/predator-vpn-scan-preview.gif)

## What was completed

| Part of the recorded work | Evidence described in the completion record |
| :--- | :--- |
| **Connection and scope** | An owned Ubuntu VM connected to the Academy VPN after the timed Pwnbox expired. The current lab target and route were checked before each exercise. |
| **Enumeration and reports** | Saved full TCP scan output, hostname and highest-port evidence, service-version results, and report review. |
| **NSE exercise** | A rejected candidate prompted a fresh web-server check. The owner confirmed acceptance of the resulting answer. |
| **Easy, Medium, and Hard IDS/IPS labs** | Each lab used its own Academy target. Bounded steps and saved outputs supported the owner's answer submissions. |
| **Completion** | Owner-confirmed accepted answers and an Academy module completion screenshot covering all 12 sections. |

## Model and owner roles

**GLM-5.3** planned and executed the VM commands autonomously, interpreted saved outputs, and revised candidates when Academy feedback required a fresh check.

**The owner** provided plain-language instructions such as “go” and the HTB exercise questions, then typed the resulting answers into Academy.

Execution attribution follows the owner's October 3 clarification of the run: Predator performed the VM enumeration autonomously, and the owner entered the Academy answers.

The earlier user-owned **Pwnbox** session separately validated console attachment, observation, reviewed input, human takeover, resume, and detachment. Its short preview shows a TTL lesson check:

![Sanitized Pwnbox console preview and reviewed TTL lesson check](../media/predator-pwnbox-ttl-preview.gif)

## Public replay and evidence limits

The Nmap animation is a **27-frame sanitized evidence replay**, assembled from saved scans, model responses, and owner-provided Academy screenshots. It is not a continuous desktop recording. Target addresses, VPN material, and exercise flags are withheld.

The complete scans and original Academy screenshots remain private. This public note summarizes the producer's completion record and the owner's clarified execution attribution; it does not independently authenticate the Academy account or reproduce the private run. It records one completed training module with autonomous Predator/GLM-5.3 VM execution and human Academy answer entry.

The public animations are byte-for-byte copies of the sanitized Predator M assets at revision `b02492146d7f7cf5eb1ee3c8b27362dfedbaba2a`:

| Asset | Git blob |
| :--- | :--- |
| `predator-vpn-scan-preview.gif` | `ae2937e7895a55895efd19bab0abaeff475e4b37` |
| `predator-pwnbox-ttl-preview.gif` | `c0ef63583404a2e36c6825c6cdb55715867b5fe3` |

[Back to the Predator overview →](../../README.md#network-enumeration-with-nmap)
