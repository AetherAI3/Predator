# BlockSynergy

**HTB machine · Insane · Linux · completed October 5, 2026.** The user and root challenge files were read from the live, authorized lab machine, and the owner confirmed the result. A separate HTB account submission was not observed.

![Sanitized Predator BlockSynergy replay](predator-replay.gif)

The [six-frame GIF](predator-replay.gif) is a **sanitized replay assembled from saved model output and terminal evidence**. Every frame identifies it as a replay. The public version omits the target address, credentials, flag values, precise timing, file paths, and exploit commands. Its SHA-256 hash and frame count are in the [HTB media manifest](../../media-manifest.json).

## Execution roles and evidence

| Role | Recorded contribution |
| --- | --- |
| **Predator / GLM 5.3** | Reviewed the pinned attack-chain catalog and identified a generic SUID privilege-escalation chain and a TOCTOU primitive as research context. The model explicitly treated these as hypotheses before live validation. |
| **Operator** | Ran the authorized lab checks, observed the privilege-escalation result, read both challenge files, and removed temporary access and test artifacts. |
| **Owner** | Confirmed the reported flags in the chat. |

The live root verification showed effective UID 0. The development service was restored and returned HTTP 200 after cleanup. The custom application and restore behavior were **not assigned a CVE**; a generic MITRE chain is research context, not a verified product vulnerability.

## BlockSynergy attack-chain Crucible replay

After completion, the saved machine evidence was replayed **offline** through the existing seven-role Crucible lane: DSV4 Flash proposed chain claims, and GLM 5.3 reviewed the unresolved set. An independent source check then separated supported matches from false leads. This replay neither contacted the machine nor contributed to the original solve or GIF.

The concrete retrieval failure was a vocabulary mismatch. The saved query `authorized_keys` returned no catalog results, although the frozen bank contained **P14, SSH Authorized Key Injection**, retrievable by its exact MITRE code `T1098.004`. The broad `SUID` query also returned **PX10**, whose PATH-hijack prerequisite was absent from the case. **MS02** describes the observed check/use race at the primitive level, while **E01** is only a broad SUID detection chain. Neither supplies a product CVE or a complete machine-specific route.

**Repair:** Predator's existing read-only chain search now folds separators and simple plurals when matching a query to chain-title words. This makes `authorized_keys` find P14 without changing the frozen chain bank or widening exact MITRE-code matching. The case regression and negative controls pass **13 scoped catalog tests**. The replay rejected the suggestion to launch a deeper search solely because the first query missed: the relevant P14 entry was already present. This establishes retrieval correctness for the saved case; no latency or cost improvement has been measured.

The full trace and challenge answers remain in the private Predator task record. This page records the outcome and attribution without publishing an active-machine solution.

[All machines →](../README.md) · [All HTB work →](../../README.md)
