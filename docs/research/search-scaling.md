# Search quality and joint5 scaling, in plain English

**Reported synthetic tests: October 20, 2026 · Public summary: October 21, 2026**

[← Predator overview](../../README.md#how-predator-chooses-the-next-move) · [Aggregate data](search-scaling.json) · [Separate IBM Fez hardware pilot](ibm-fez-pilot.md)

Predator chooses from a menu of possible next moves. Some work well together; some need another move first; others conflict. A **QUBO** is the scorecard for those yes/no choices and their interactions. **Energy** is the score, and lower is better. The software's own checks establish whether a proposed result holds.

The design recommendation is to **keep ordinary computer search in charge, make quantum experiments cheaper, and require evidence before trusting them with decisions**. The tests below have not demonstrated a quantum advantage.

![Two selected-size charts separating experimental answer quality from joint5 circuit instruction counts.](../assets/search-scaling-2026-10-20.svg)

## Three different jobs

| Job | Plain-English meaning | What the summary supports |
| :--- | :--- | :--- |
| **Choose actions** | Find a useful combination under the scorecard's rules. | Ordinary search remains the proposed V1 selector. The tested quantum algorithm's untuned samples often miss the known minimum. |
| **Simulate a quantum circuit** | Use an ordinary computer to imitate the quantum algorithm. | The proposed automatic mode uses a detailed **statevector** simulation up to 20 candidates and a compressed **MPS** simulation above that. The cutoff comes from this test setup. |
| **Compile a circuit** | Translate the scorecard into device instructions. | Compare ordinary and joint5 compilations and keep the smaller routed circuit. A smaller circuit still needs a separate answer-quality comparison. |

MPS's **χ (chi)** setting controls how much detail the compressed simulation can retain. A higher setting costs memory and time. The proposed cap is 64; convergence checks should show whether increasing the setting changes the scores. Agreement between two settings is evidence of stability, not a guarantee of correctness.

## Why a larger candidate limit needs different search

Each candidate can be included or excluded. Each additional candidate doubles the possible combinations before rules filter them:

| Candidates in one decision | Possible on/off combinations |
| ---: | ---: |
| 16 | 65,536 |
| 24 | 16,777,216 |
| 32 | 4,294,967,296 |
| 40 | 1,099,511,627,776 |

These are combination counts, not predicted run times. **V1 retains the 16-candidate limit.** Expansion toward 32–40 candidates, simulated annealing, and quantum parameter training are separate V2 proposals. Simulated annealing is an ordinary-computer search method that explores promising combinations without enumerating every one. Parameter training tunes the circuit's settings; it does not guarantee a quantum advantage.

## Answer quality: best sampled score versus the exact minimum

The reported circuit used one QAOA layer, fixed angles `gamma = beta = 0.4`, no parameter training, and 4,096 samples per run. A **0% gap** means the best sampled answer reached the classical minimum. Positive values mean it missed a better answer under the same synthetic scorecard.

| Candidates | Seeds | Reported best-sample score gap |
| ---: | ---: | :--- |
| 4 | 3 | 0% |
| 6 | 3 | 0–11% |
| 8 | 3 | 6–15% |
| 10 | 3 | 0–34% |
| 12 | 3 | 10–47% |
| 14 | 3 | 37–55% |
| 16 | 3 | 28–41% |
| 20 | 3 | 46–72% |
| 24 | 3 | Not supplied |
| 32 | 2 | Not supplied |
| 40 | 1 | Not supplied |

The ranges summarize different seeded test problems; they are **not confidence intervals**. These percentages describe an internal test score, not mission success rates, exploit reliability, or bounty results. No scored gap was supplied above 20 candidates, so the larger-size answer quality is not established here. The conclusion applies to the tested untuned circuit, not every quantum optimization method.

## Compilation: when joint5 saves instructions

A native two-qubit gate is a hardware instruction involving two qubits. The counts below include routing work needed to fit the circuit onto a heavy-hex connection layout. A circuit with fewer such instructions may be easier to execute, but instruction count alone does not establish lower run time, cost, noise, or a better answer.

| Candidates | Seeds | Ordinary instructions | joint5 instructions | Derived change |
| ---: | ---: | ---: | ---: | ---: |
| 4 | 3 | 9 | 7 | −22.2% |
| 6 | 3 | 16 | 9 | −43.8% |
| 8 | 3 | 40 | 35 | −12.5% |
| 10 | 3 | 76 | 64 | −15.8% |
| 12 | 3 | 101 | 88 | −12.9% |
| 14 | 3 | 160 | 152 | −5.0% |
| 16 | 3 | 228 | 213 | −6.6% |
| 20 | 3 | 433 | 423 | −2.3% |
| 24 | 3 | 647 | 604 | −6.6% |
| 32 | 2 | 1,299 | 1,351 | +4.0% |
| 40 | 1 | 2,077 | 2,365 | +13.9% |

Negative means fewer instructions. The derived change is `100 × (joint5 − ordinary) / ordinary`, calculated from the supplied **rounded mean counts**. It can differ from a mean or range of per-seed percentage changes; those statistics should not be mixed. The source also reports individual regressions at some smaller sizes, including 14 and 20 candidates. An aggregate reduction therefore does not mean joint5 helped every fixture.

The README chart selects 12, 16, 32, and 40 candidates for readability. The full table retains all supplied sizes. There are only two seeds at 32 and one at 40. The result supports comparing both layouts for each job; it does not prove that joint5 always fails above a particular size.

## What to record before trusting the experimental search

- Best sampled score and average score, compared with a suitable classical baseline.
- The ordinary and joint5 routed instruction counts, and which compilation was selected.
- The simulator or device actually used, its settings, and whether circuit parameters were trained.
- For compressed simulation, whether average scores stabilize as retained detail increases.

The source reports that distribution-distance comparisons become dominated by sparse sampling at larger sizes. Average-score comparisons and convergence checks are therefore proposed alongside that metric. None of these bookkeeping changes substitutes for native software validation.

## Method and provenance

This is an **owner-reported public projection of an aggregate research summary**, not an independently rerun experiment. The supplied document is titled “Part C. Math and scaling laws”; its SHA-256 is `2fb87bd080b3ca273575843c87ce78c1315cd519b3c15660b9c3255b27d1437f`. The fingerprint identifies that summary; it does not independently verify the measurements. Raw per-seed records, executable circuits, and the experiment implementation are not included in this public extract.

The summary reports Python 3.12, Qiskit 2.3.1, Qiskit Aer 0.17.2, and a 12-core Windows host. Synthetic QUBOs had interaction density 0.35, `n/4` prerequisites and exclusions, and penalty `sum(abs(u)) + sum(abs(s)) + 1`. Ordinary and greedy edge-disjoint-triangle joint5 circuits were compiled at optimization level 3 with seed 11 to `cz`, `rz`, `sx`, and `x` on a heavy-hex coupling map. Aer statevector supplied an ideal reference through 20 candidates. MPS detail settings were swept up to 128; 32- and 40-candidate cases used 4, 16, and 64. Three MPS data points were reportedly lost after repeated Windows process failures.

**No new IBM acquisition was made for this sweep.** The [September 6 IBM Fez pilot](ibm-fez-pilot.md) remains a separate hardware experiment: 144 → 103 native gates per pole, closer output distributions, and worse expected energy on both poles. It does not establish better minimization or quantum advantage.

The summary's automatic backend routing, automatic compiler comparison, larger search limits, and trained-circuit work are **design recommendations**, not proof of deployed behavior. Its proposed future hard-problem regime is a research hypothesis; these small tests do not establish a universal hardware-advantage threshold.

## Rebuild the figure

From the repository root, with Python and matplotlib installed:

```bash
python3 docs/assets/build_search_scaling_assets.py
```

This rebuilds the static SVG from [search-scaling.json](search-scaling.json). Add `--preview-dir /path/to/previews` to render a PNG for layout review. Rebuilding the figure does not run the research experiment, call a model, or use quantum hardware.
