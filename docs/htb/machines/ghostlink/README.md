# Ghostlink

**HTB machine · Hard · Windows.** The user and root challenge files were read from the live, authorized lab machine on October 5, 2026.

**Predator model: GLM-5.3.** The GIF below is the P-BOX guest recording from that mission.

![P-BOX guest recording from Predator's GLM-5.3 Ghostlink mission, with blank white frames removed](Ghostlink-VM-Predator-final-replay.gif)

The [670-frame GIF](Ghostlink-VM-Predator-final-replay.gif) is the actual full-screen recording of Predator's disposable VPS3 pwnbox at 1600 × 920. It is the cleaned version of 783 saved frames: 113 near-white browser-loading frames were omitted to stop flashing. The terminal is visible. **It includes temporary lab addresses, command history, and challenge spoilers.** The [frame provenance](replay-provenance.json) records every included source-frame hash, the omitted blank frames, and the GIF hash.

## Execution roles and evidence

| Role | Recorded contribution |
| :--- | :--- |
| **Predator / GLM-5.3** | Produced early reconnaissance and hypotheses in its saved trace. Later planning calls returned HTTP 400; the model did not complete the final escalation. |
| **Operator** | Reviewed guest actions, used the live pwnbox to reach a target shell, changed to the local user, and read the user challenge file. The operator then validated an Administrator credential lead from a [published Ghostlink analysis](https://0xdf.gitlab.io/2026/09/15/htb-ghostlink.html) against this instance and read the root challenge file over SMB. |

The live user observation reported `uid=1001(nvirelli)` before reading `user.txt`. The root observation authenticated to the Windows host as Administrator and read `root.txt` from its administrative share. The flag values and credentials remain in the private task receipt. The certificate-relay escalation described by the published lead was **not independently replayed** here.

The recorder stopped before those final flag reads, so the GIF does not depict the flags or Administrator verification. The live flag observations are described from the separate private receipt. Challenge files, credentials, and the complete tool trace remain outside this public repository.

[All machines →](../README.md) · [All HTB work →](../../README.md)
