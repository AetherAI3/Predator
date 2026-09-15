"""Build public result SVGs from approved summary JSONs; no experiment calls."""
import json
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE.parent / "research/ibm-pilot.json").read_text())
Q3 = json.loads((HERE.parent / "research/charls-q3.json").read_text())
BG, FG, MUTED = "#070d17", "#f2f6ff", "#adbbce"
BLUE, PURPLE, GREEN, AMBER = "#32c7eb", "#b48aff", "#67dcb4", "#efc479"


def text(x, y, value, size=20, color=FG, weight=400, extra=""):
    return f'<text x="{x}" y="{y}" font-family="Helvetica,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{escape(str(value))}</text>'


def start(width, height, title, description):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
            f'<title id="title">{escape(title)}</title><desc id="description">{escape(description)}</desc>',
            f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="18" fill="{BG}" stroke="#2a3b51"/>']


def hero():
    a = start(1280, 350, "Predator by Aether AI", "Brand graphic: reason deeply, prove the result. AI reasoning, adaptive compilation and software verification. This is not a research measurement.")
    a += [f'<path d="M48 42H650" stroke="{BLUE}" stroke-width="3"/>',
          f'<path d="M650 42H1232" stroke="{PURPLE}" stroke-width="3"/>',
          text(49, 86, "AETHER AI / SECURITY RESEARCH", 17, MUTED, 700, 'letter-spacing="2"'),
          text(42, 201, "PREDATOR", 128, FG, 900, 'letter-spacing="-6"'),
          text(50, 261, "Reason deeply. Prove the result.", 34, BLUE, 700),
          text(50, 308, "AI reasoning · Adaptive compilation · Software verification", 20, MUTED)]
    for y, number, title, color in [(99, "01", "REASON", BLUE), (173, "02", "COMPILE", PURPLE), (247, "03", "VERIFY", GREEN)]:
        a += [f'<rect x="945" y="{y}" width="287" height="57" rx="9" fill="#101b2b" stroke="#283b53"/>',
              text(962, y+37, number, 21, color, 700), text(1011, y+36, title, 19, FG, 700, 'letter-spacing="2"')]
    return "\n".join(a + ["</svg>"])


def badge(label, value, color, width=254):
    a = start(width, 32, label+": "+value, "Static editorial label, not a live CI, deployment or scientific-validation status.")
    a += [f'<circle cx="14" cy="16" r="3" fill="{color}"/>', text(25, 20, label, 10, MUTED, 700), text(96, 20, value, 10, color, 700)]
    return "\n".join(a + ["</svg>"])


def hardware():
    gates = DATA["two_qubit_gates"]
    reduction = 100 * (gates["ordinary"] - gates["joint5"]) / gates["ordinary"]
    a = start(1280, 800, "IBM Fez: published compiler measurements", "Author-reported pilot, September 6, 2026. Ordinary compilation in blue, joint5 in purple. Native two-qubit gates decreased 144 to 103 per circuit. Total-variation distance decreased in both related cases. Expected energy increased, which is worse for the minimization objective. One fixture, four circuits, one job; no independent confirmation or quantum advantage established.")
    a += [text(48, 48, "IBM FEZ / PUBLISHED HARDWARE PILOT", 17, GREEN, 700),
          text(1232, 48, "06 SEP 2026", 17, MUTED, 700, 'text-anchor="end"'),
          text(48, 117, "Fewer gates. Closer output.", 46, FG, 700),
          text(48, 158, "Two related cases from one six-variable fixture.", 23, MUTED),
          text(48, 244, gates["ordinary"], 76, BLUE, 700), text(215, 241, "→", 53, MUTED),
          text(301, 244, gates["joint5"], 76, PURPLE, 700),
          text(510, 240, f"−{reduction:.1f}%", 54, PURPLE, 700),
          text(50, 285, "Native two-qubit gates per circuit", 22, MUTED),
          text(930, 207, f'{DATA["circuits"]} circuits', 28, FG, 700),
          text(930, 244, f'{DATA["shots_per_circuit"]:,} shots each', 22, MUTED),
          text(930, 279, f'{DATA["billed_qpu_seconds"]} s billed QPU time', 20, MUTED),
          '<path d="M48 313H1232" stroke="#293b53"/>',
          text(48, 358, "Output agreement", 27, FG, 700),
          text(1232, 356, "TV distance ↓ Lower is closer to ideal", 18, MUTED, 400, 'text-anchor="end"')]
    for tick in range(6):
        x = 350 + tick * 138
        a += [f'<path d="M{x} 400V610" stroke="#28364b"/>', text(x, 389, f"{tick/10:.1f}", 16, MUTED, 400, 'text-anchor="middle"')]
    for top, label, key in [(410, "Vulnerable case", "vuln"), (533, "Fixed case", "fix")]:
        a += [text(48, top+29, label, 24, FG, 700)]
        for dy, method, display, color in [(0, "ordinary", "Ordinary", BLUE), (39, "joint5", "joint5", PURPLE)]:
            y, value = top+dy, DATA["poles"][key][method+"_tv"]
            a += [text(245, y+21, display, 18, color, 700),
                  f'<rect x="350" y="{y}" width="{value / .5 * 690:.6f}" height="28" rx="4" fill="{color}"/>',
                  text(365+value/.5*690, y+22, f"{value:.6f}", 20, FG, 700)]
    a += ['<path d="M48 638H1232" stroke="#293b53"/>',
          text(48, 678, "Important tradeoff: expected energy increased in both cases.", 25, AMBER, 700),
          text(48, 714, "Fewer gates and closer output did not improve minimization.", 22, FG),
          text(48, 763, "Author-reported public extract · One hardware job · No independent confirmation · No quantum advantage established", 17, MUTED)]
    return "\n".join(a + ["</svg>"])


def panel(x, y, width, height, fill="#101b2b", stroke="#293e57", radius=12):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'


def win():
    m = Q3["metrics"]
    a = start(1280, 740, "First Gen3 win · CharLS Q3", "Completed case, ongoing program. Q2 banked C2 with 16 of 24 protected cases passing. Q3 banked C3 with 24 of 24 passing: 16 preserved in blue, eight gained in purple, zero prior passes lost. Tiles show aggregate counts, not case identities. Producer-verified closeout; no quantum advantage established.")
    a += [f'<path d="M48 35H638" stroke="{BLUE}" stroke-width="4"/>',
          f'<path d="M646 35H1232" stroke="{PURPLE}" stroke-width="4"/>',
          text(48, 78, "AETHER AI / PREDATOR RESEARCH", 18, MUTED, 700, 'letter-spacing="2"'),
          text(1232, 78, "14 SEP 2026 · CASE COMPLETE", 17, GREEN, 700, 'text-anchor="end"'),
          text(48, 151, "FIRST GEN3 WIN", 61, FG, 800, 'letter-spacing="-2"'),
          text(48, 193, "The next repair used the last failure — and closed the residual.", 24, MUTED),
          text(52, 264, f'C2  {m["c2_pass"]}/{m["protected_total"]}  →  C3', 30, BLUE, 700),
          text(42, 403, f'{m["c3_pass"]}/{m["protected_total"]}', 151, FG, 800, 'letter-spacing="-7"'),
          text(52, 453, "Q3 NATIVE PASS · C3 BANKED", 24, PURPLE, 700),
          text(690, 251, "THE 24 EVALUATED CASES", 19, MUTED, 700, 'letter-spacing="1"')]
    for i in range(m["protected_total"]):
        x, y = 690 + (i % 8) * 65, 274 + (i // 8) * 60
        color = BLUE if i < m["preserved"] else PURPLE
        a += [panel(x, y, 49, 45, color, color, 6),
              f'<path d="M{x+14} {y+23}l7 7 14-15" fill="none" stroke="#071322" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>']
    a += [f'<circle cx="696" cy="463" r="5" fill="{BLUE}"/>', text(709, 469, "16 preserved", 21, BLUE, 700),
          f'<circle cx="962" cy="463" r="5" fill="{PURPLE}"/>', text(976, 469, "8 new passes", 21, PURPLE, 700)]
    for x, value, label, color in [(48, "+8", "NEW PROTECTED PASSES", PURPLE), (449, "16/16", "PRIOR PASSES RETAINED", BLUE), (850, "0", "PRIOR PASSES LOST", GREEN)]:
        a += [panel(x, 510, 382, 117), text(x+24, 564, value, 43, color, 700), text(x+24, 601, label, 17, MUTED, 700)]
    a += [text(48, 666, "Completed dependent repair. Next objective: demonstrate quantum advantage.", 25, FG, 700),
          text(48, 708, "Controlled CharLS test cases, not vulnerabilities · Aggregate tiles · Producer-verified closeout", 18, MUTED)]
    return "\n".join(a + ["</svg>"])


def chain():
    a = start(1280, 970, "The completed Gen3 chain, followed by the next objective", "C0 frozen problem, Q1, C1 continuation reached, Q2 native failure, C2 16 of 24, Q3 residual-directed repair, C3 24 of 24. C0 and C1 have no comparable protected count here. The Q2 failure is retained. Q3 is a new C2-directed singleton repair, with unchanged compiler and decoder semantics. The case is complete; the program continues toward quantum advantage.")
    a += [text(48, 52, "THE LOOP HAS A COMPLETED RESULT", 19, GREEN, 700, 'letter-spacing="1"'),
          text(48, 108, "Evidence → intervention → new evidence", 40, FG, 700),
          text(48, 145, "C = banked checkpoint carried into reasoning     Q = dependent intervention", 21, MUTED)]
    rows = [
        ("C0", 184, "Frozen problem", "Controlled source + committed evaluation contract", "—", "No comparable count", MUTED),
        ("C1", 356, "Continuation reached", "Q1 exposes the next obligation; stage-two options released", "—", "No comparable count", BLUE),
        ("C2", 528, "Residual isolated", "Q2: gates A/B pass; gate C fails FRAGMENTDATA", "16/24", "Native FAIL retained", BLUE),
        ("C3", 700, "Residual closed", "Q3: new C2-H1 repair; 16 preserved + 8 newly passing", "24/24", "Native PASS · banked", PURPLE),
    ]
    a += [f'<path d="M150 242V758" stroke="#496481" stroke-width="3"/>']
    for stage, y, title, detail, score, score_label, color in rows:
        a += [f'<path d="M150 {y+58}H270" stroke="{color}" stroke-width="2"/>',
              f'<circle cx="150" cy="{y+58}" r="7" fill="{color}"/>',
              panel(270, y, 962, 116, "#101627" if stage == "C3" else "#0f1928", color if stage == "C3" else "#293e57"),
              text(294, y+56, stage, 36, color, 800),
              text(390, y+44, title, 29, FG, 700),
              text(390, y+85, detail, 18, MUTED),
              text(1199, y+49, score, 37, color, 700, 'text-anchor="end"'),
              text(1199, y+87, score_label, 17, MUTED, 400, 'text-anchor="end"')]
    for y, q, action, color in [(306, "Q1", "Reach continuation", BLUE), (478, "Q2", "Select + test", BLUE), (650, "Q3", "Repair from C2", PURPLE)]:
        a += [panel(48, y, 204, 44, "#151f32", color, 8), text(66, y+29, q, 25, color, 700),
              text(281, y+28, action, 19, color, 700),
              f'<path d="M145 {y+43}l5 5 5-5" fill="none" stroke="{color}" stroke-width="2"/>']
    a += [f'<path d="M48 854H1232" stroke="#2c405d"/>',
          text(48, 891, "FOLLOW-UP / GEN3 CONTINUES", 18, PURPLE, 700, 'letter-spacing="1"'),
          text(48, 930, "Demonstrate quantum advantage through matched comparisons and replication.", 24, FG, 700)]
    return "\n".join(a + ["</svg>"])


def selection():
    q = Q3["quantum"]
    a = start(1280, 620, "Recorded Q2 quantum-selection data · Aer simulation", "2048 samples: 00 635 rejected; 01 291 feasible and selected at energy one quarter; 10 324 feasible at energy two; 11 798 rejected. Lowest feasible sampled energy selected, not most frequent state. 615 feasible, 1433 rejected, regret zero. Exact classical selection agreed. This is Q2 simulation data, not a Q3 hardware result.")
    a += [text(48, 52, "QUANTUM SELECTION / Q2 · AER SIMULATION", 18, BLUE, 700),
          text(48, 112, "The frozen optimum was selected.", 43, FG, 700),
          text(48, 150, "2,048 recorded samples · bit order [t17, t42] · lower feasible energy wins", 22, MUTED),
          text(1123, 201, "DECISION / ENERGY", 16, MUTED, 700, 'text-anchor="middle"')]
    for i, row in enumerate(q["samples"]):
        y = 218 + i * 63
        color = PURPLE if row.get("selected") else BLUE if row["feasible"] else "#586c87"
        a += [text(49, y+29, row["bits"], 29, color if row["feasible"] else MUTED, 700),
              panel(155, y, 720, 36, "#142035", "#142035", 5),
              panel(155, y, row["count"] / 900 * 720, 36, color, color, 5),
              text(915, y+28, row["count"], 27, FG, 700),
              text(1020, y+28, "Selected · 1/4" if row.get("selected") else "Feasible · 2" if row["feasible"] else "Rejected", 23, color if row["feasible"] else MUTED, 700)]
    a += ['<path d="M48 486H1232" stroke="#293e57"/>',
          text(48, 530, "615 feasible", 29, BLUE, 700), text(384, 530, "1,433 rejected", 29, MUTED, 700),
          text(803, 530, "Regret 0", 29, PURPLE, 700),
          text(48, 584, "Exact classical selection agreed · Q2 native FAIL preserved · Q3 repaired the remaining obligation", 21, MUTED)]
    return "\n".join(a + ["</svg>"])


def entry_card(research=False):
    color = PURPLE if research else BLUE
    title = "Explore the Q3 result" if research else "Explore Aether Actions"
    a = start(620, 365, title, "First Gen3 result: 24 of 24 cases passing, eight new passes, zero prior passes lost." if research else "Supported Actions: connect a repository, review scope and approve an action.")
    a += [f'<path d="M30 23H590" stroke="{color}" stroke-width="2"/>',
          text(30, 63, "FIRST GEN3 REPAIR WIN" if research else "SUPPORTED CHECKS", 14, color, 700, 'letter-spacing="1"'),
          text(30, 118, title, 32, FG, 700),
          text(30, 156, "The completed chain. The next research objective." if research else "Connect a repo. Review scope. Approve usage.", 18, MUTED)]
    stats = [("24/24", "CASES PASSING"), ("+8", "NEW PASSES"), ("0", "PRIOR LOST")] if research else [("Repo", "CONNECT"), ("Scope", "REVIEW"), ("Action", "APPROVE")]
    for i, (value, label) in enumerate(stats):
        x = 30 + i * 190
        a += [panel(x, 190, 177, 87), text(x+14, 228, value, 31, [BLUE,PURPLE,GREEN][i], 700), text(x+14, 256, label, 12, MUTED, 700)]
    a += [panel(30, 304, 560, 39, "#18223a", "#425478", 18), text(50, 330, "Read the Q3 evidence →" if research else "Explore supported Actions →", 18, FG, 700)]
    return "\n".join(a + ["</svg>"])


if __name__ == "__main__":
    assert DATA["schema"] == "predator.public-compiler-pilot.v1" and DATA["independent_confirmation"] is False
    assert (DATA["hardware_jobs"], DATA["circuits"], DATA["shots_per_circuit"], DATA["billed_qpu_seconds"]) == (1, 4, 1024, 3)
    assert (DATA["two_qubit_gates"]["ordinary"], DATA["two_qubit_gates"]["joint5"]) == (144, 103)
    assert all(p["joint5_tv"] < p["ordinary_tv"] and p["joint5_expected_energy"] > p["ordinary_expected_energy"] for p in DATA["poles"].values())
    assert Q3["schema"] == "predator.public-gen3-charls-q3.v1"
    m = Q3["metrics"]
    assert (m["c2_pass"], m["c3_pass"], m["preserved"], m["gained"], m["lost"]) == (16, 24, 16, 8, 0)
    assert sum(s["count"] for s in Q3["quantum"]["samples"]) == 2048
    outputs = {"readme-hero.svg": hero(), "readme-hardware-data.svg": hardware(),
               "readme-gen3-win.svg": win(), "flow-gen3-research.svg": chain(), "readme-q2-selection.svg": selection(),
               "readme-start-actions.svg": entry_card(), "readme-start-q3.svg": entry_card(research=True),
               "tag-actions-profiles.svg": badge("ACTIONS", "LOCKED PROFILES", GREEN),
               "tag-gen3-private.svg": badge("GEN 3", "RESEARCH CONTINUES", PURPLE),
               "tag-gen3-win.svg": badge("MILESTONE", "Q3 NATIVE PASS", GREEN),
               "tag-q3-utility.svg": badge("PROTECTED", "24 / 24 PASSING", PURPLE),
               "tag-hardware-pilot.svg": badge("HARDWARE", "PUBLISHED PILOT", BLUE)}
    for name, svg in outputs.items():
        (HERE/name).write_text(svg, encoding="utf-8")
    print(f"Built {len(outputs)} SVGs from approved public Q3 and IBM records; no experiments run.")
