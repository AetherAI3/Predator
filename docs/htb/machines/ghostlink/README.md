# Ghostlink

**HTB machine · Hard · Windows.** The user and root challenge files were read from the live, authorized lab machine on October 5, 2026. An HTB account submission was not observed.

![Sanitized full-screen Predator pwnbox replay](predator-pwnbox-replay.gif)

The [ten-frame replay](predator-pwnbox-replay.gif) uses actual 1600 × 920 captures of Predator's disposable VPS3 pwnbox. It retains the full interface while obscuring the terminal, target address, and guest identifier. No credentials, flag values, or exploit commands appear in the public version. The [frame provenance](replay-provenance.json) records the selected source hashes and the GIF hash.

## Execution roles and evidence

| Role | Recorded contribution |
| :--- | :--- |
| **Predator / GLM 5.3** | Produced early reconnaissance and hypotheses in its saved trace. Later planning calls returned HTTP 400; the model did not complete the final escalation. |
| **Operator** | Reviewed guest actions, used the live pwnbox to reach a target shell, changed to the local user, and read the user challenge file. The operator then validated an Administrator credential lead from a [published Ghostlink analysis](https://0xdf.gitlab.io/2026/09/15/htb-ghostlink.html) against this instance and read the root challenge file over SMB. |

The live user observation reported `uid=1001(nvirelli)` before reading `user.txt`. The root observation authenticated to the Windows host as Administrator and read `root.txt` from its administrative share. The flag values and credentials remain in the private task receipt. The certificate-relay escalation described by the published lead was **not independently replayed** here.

The recorder stopped before those final flag reads. The GIF's later captions describe separately saved live observations; they are not depicted as VM footage. Detailed terminal and tool traces, including operational details, stay private.

[All machines →](../README.md) · [All HTB work →](../../README.md)
