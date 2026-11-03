"""Build the Quantum Comm Ops agent-lane SVGs (compounding chart, one-cycle loop) from the approved public JSON; no experiment calls.

Run from the repository root: python docs/assets/build_quantum_comm_ops_k_assets.py [--check]
--check rebuilds in memory and exits non-zero if either published SVG differs from the rebuild.
"""
import json
import sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE.parent / "research/quantum-comm-ops.json").read_text(encoding="utf-8"))
LANES = DATA["agent_lanes"]
HW = DATA["hardware_missions"]
BG, FG, MUTED = "#070d17", "#f2f6ff", "#adbbce"
BLUE, PURPLE, GREEN, AMBER = "#32c7eb", "#b48aff", "#67dcb4", "#efc479"
DIM, DIM_TEXT, ARROW = "#3b4f68", "#8696ad", "#5f7a99"
CHAR_W = 0.55  # approximate advance per character as a fraction of font size for the sans stack
WIDTH, MARGIN = 960, 48
CONTENT_W = WIDTH - 2 * MARGIN
KICKER_W = CONTENT_W - 180  # bold capitals run wider than CHAR_W; leave room for the right-aligned date
EVIDENCE_NO_QPU = "measured_no_qpu"
EVIDENCE_HARDWARE = "measured_hardware"
DATE_K = "2026-11-01"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def text(x, y, value, size=20, color=FG, weight=400, extra="", max_w=None):
    value = str(value)
    if max_w is not None and len(value) * size * CHAR_W > max_w:
        raise ValueError(f"text overflows {max_w}px at {size}px ({len(value) * size * CHAR_W:.0f}px): {value!r}")
    return (f'<text x="{x}" y="{y}" font-family="Helvetica,Arial,sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" {extra}>{escape(value)}</text>')


def start(width, height, title, description):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
            f'role="img" aria-labelledby="title description">',
            f'<title id="title">{escape(title)}</title><desc id="description">{escape(description)}</desc>',
            f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="18" fill="{BG}" stroke="#2a3b51"/>']


def panel(x, y, width, height, fill="#101b2b", stroke="#293e57", radius=12, extra=""):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}" stroke="{stroke}"{extra}/>'


def pct(value):
    return f"{value * 100:.1f}%"


def short_date(iso):
    year, month, day = iso.split("-")
    return f"{int(day)} {MONTHS[int(month) - 1].upper()} {year}"


def require(condition, message):
    if not condition:
        raise ValueError(message)


# ---------------------------------------------------------------- compounding chart (K4)

def compounding_data():
    k4 = LANES["compounding_K4"]
    run = k4["run_3b"]
    first, esc, cost = run["first_try_verified_of_40"], run["escalations"], run["cost_per_verified_uvt"]
    require(len(first) == len(esc) == len(cost) == 3, "run 3b must hold three cycles")
    require(LANES["evidence_label"] == EVIDENCE_NO_QPU, "agent_lanes evidence label changed; review the figure wording")
    return k4, run, first, esc, cost, k4.get("runs_1_2")


def compounding_description(run, first, esc, cost, free):
    free_part = ""
    if free:
        f12 = free["first_try_verified_of_40_cycles_1_2"]
        free_part = (f" Earlier free-tier runs one and two (a free first-tier worker) reached {f12[0]} then {f12[1]} of forty "
                     f"in cycles one and two, with cycle-two cost per verified record {free['cost_ratio_cycle2_over_cycle1']} of cycle one; "
                     f"their cycle three was {free['cycle_3']}.")
    return (f"Measured compounding rehearsal on fixture tasks with known answers: forty agents, one shared evidence bank, three cycles, "
            f"run 3b with a paid first-tier worker paced at 40 seconds, escalating to a mid-cost worker; a frontier captain was available and not called. "
            f"Agents verified on the first try per cycle: {first[0]}, then {first[1]}, then {first[2]} of forty. "
            f"Escalations per cycle: {esc[0]}, then {esc[1]}, then {esc[2]}. "
            f"Cost per verified record in UVT per cycle: {cost[0]:,}, then {cost[1]:,}, then {cost[2]:,}; cycle three cost "
            f"{run['cycle3_over_cycle1']} times cycle one. Gates K-4a {run['gates']['K-4a']}, K-4b {run['gates']['K-4b']}; "
            f"{run['errors']} errors; run 3b model spend {run['cost_usd']} dollars.{free_part} A scripted warm-up cycle on other chains "
            "seeded the bank. No quantum-computer time was used; these are measured model calls, not a projection; "
            "no quantum advantage is claimed.")


def legend(x, y, entries):
    """entries: (swatch colour, label, text colour); laid out left to right on one line at 11px."""
    a, cursor = [], x
    for color, label, text_color in entries:
        a += [f'<rect x="{cursor}" y="{y - 10}" width="12" height="12" rx="2" fill="{color}"/>',
              text(cursor + 18, y, label, 11, text_color, 400)]
        cursor += 18 + round(len(label) * 11 * CHAR_W) + 16
    return a, cursor - x


def agents_panel(x, y, w, h, first, esc, free):
    baseline, scale = y + 190, 110 / 40
    a = [panel(x, y, w, h), text(x + 22, y + 30, "Agents verified first try, of 40", 17, GREEN, 700, max_w=w - 44),
         f'<path d="M{x + 22} {baseline}H{x + w - 22}" stroke="#293b53"/>']
    entries = [(BLUE, "run 3b · paid tier-0, paced", MUTED)]
    if free:
        entries.append((DIM, "runs 1–2 · free tier", DIM_TEXT))
    legend_marks, legend_w = legend(x + 22, y + 50, entries)
    require(legend_w <= w - 44, f"legend overflows the agents panel ({legend_w}px)")
    a += legend_marks
    f12 = free["first_try_verified_of_40_cycles_1_2"] if free else []
    for i, (n, e) in enumerate(zip(first, esc)):
        cx, bar_h = x + 80 + i * 130, n * scale
        a += [f'<rect x="{cx - 52}" y="{baseline - bar_h:.1f}" width="56" height="{bar_h:.1f}" rx="4" fill="{BLUE}"/>',
              text(cx - 24, f"{baseline - bar_h - 8:.1f}", n, 20, FG, 700, 'text-anchor="middle"'),
              text(cx, baseline + 20, f"Cycle {i + 1}", 14, FG, 400, 'text-anchor="middle"'),
              text(cx, baseline + 38, f"{e} escalated", 12, MUTED, 400, 'text-anchor="middle"')]
        if not free:
            continue
        if i < len(f12):
            fh = f12[i] * scale
            a += [f'<rect x="{cx + 12}" y="{baseline - fh:.1f}" width="32" height="{fh:.1f}" rx="4" fill="{DIM}"/>',
                  text(cx + 28, f"{baseline - fh - 6:.1f}", f12[i], 12, DIM_TEXT, 400, 'text-anchor="middle"')]
        else:
            a += [f'<rect x="{cx + 12}" y="{baseline - 22}" width="32" height="22" rx="4" fill="none" stroke="{DIM}" stroke-dasharray="3 3"/>',
                  text(cx + 28, baseline - 28, "quota", 11, DIM_TEXT, 400, 'text-anchor="middle"')]
    return a


def cost_panel(x, y, w, h, run):
    cost, ratio = run["cost_per_verified_uvt"], run["cycle3_over_cycle1"]
    baseline, scale = y + 190, 110 / max(cost)
    a = [panel(x, y, w, h), text(x + 22, y + 30, "Cost per verified record, UVT", 17, GREEN, 700, max_w=w - 44),
         text(x + 22, y + 50, "UVT = internal unit of model spend · lower is better", 12, MUTED, max_w=w - 44),
         f'<path d="M{x + 22} {baseline}H{x + w - 22}" stroke="#293b53"/>']
    under = [("baseline", MUTED, 400), ("", MUTED, 400), (f"{ratio}× cycle 1", GREEN, 700)]
    for i, c in enumerate(cost):
        cx, bar_h = x + 80 + i * 130, c * scale
        a += [f'<rect x="{cx - 36}" y="{baseline - bar_h:.1f}" width="72" height="{bar_h:.1f}" rx="4" fill="{PURPLE}"/>',
              text(cx, f"{baseline - bar_h - 8:.1f}", f"{c:,}", 20, FG, 700, 'text-anchor="middle"'),
              text(cx, baseline + 20, f"Cycle {i + 1}", 14, FG, 400, 'text-anchor="middle"')]
        label, color, weight = under[i]
        if label:
            a.append(text(cx, baseline + 38, label, 12, color, weight, 'text-anchor="middle"'))
    return a


def compounding():
    k4, run, first, esc, cost, free = compounding_data()
    title = "Compounding on fixture tasks: 40 agents, one shared evidence bank, three cycles"
    a = start(WIDTH, 516, title, compounding_description(run, first, esc, cost, free))
    a += [text(MARGIN, 40, "AGENT LANES / EXPERIMENT K · COMPOUNDING (K4) · MEASURED, NO QUANTUM-COMPUTER TIME",
               15, GREEN, 700, max_w=KICKER_W),
          text(WIDTH - MARGIN, 40, short_date(DATE_K), 15, MUTED, 700, 'text-anchor="end"'),
          text(MARGIN, 84, "Compounding on fixture tasks:", 30, FG, 700, max_w=CONTENT_W),
          text(MARGIN, 118, "40 agents, one shared evidence bank, three cycles", 30, FG, 700, max_w=CONTENT_W),
          text(MARGIN, 144, "Run 3b · paid first-tier worker, paced 40 s → mid-cost worker; captain not called · same 40 chains each cycle",
               14, MUTED, max_w=CONTENT_W)]
    a += agents_panel(MARGIN, 160, 420, 240, first, esc, free)
    a += cost_panel(MARGIN + 444, 160, 420, 240, run)
    if free:
        f12 = free["first_try_verified_of_40_cycles_1_2"]
        a += [text(MARGIN, 424, f"Grey bars: free-tier runs 1–2: {f12[0]} → {f12[1]} first try in cycles 1–2; cycle-2 cost per verified "
                   f"vs cycle 1: {free['cost_ratio_cycle2_over_cycle1']}.", 12, MUTED, max_w=CONTENT_W),
              text(MARGIN, 442, "Free first-tier worker · cycle 3 stopped by the model gateway's hourly call quota · "
                   "run 3b is the run of record", 12, MUTED, max_w=CONTENT_W)]
    gates = run["gates"]
    a += [f'<path d="M{MARGIN} 458H{WIDTH - MARGIN}" stroke="#293b53"/>',
          text(MARGIN, 480, "Fixture tasks with known answers · a scripted warm-up cycle on other chains seeded the bank · no quantum-computer time",
               12, MUTED, max_w=CONTENT_W),
          text(MARGIN, 498, f"Measured model calls, not a projection · K-4a {gates['K-4a']}, K-4b {gates['K-4b']}, {run['errors']} errors · "
               f"run 3b ${run['cost_usd']}, lane ${k4['lane_cost_usd']} · no quantum advantage claimed", 12, MUTED, max_w=CONTENT_W)]
    return "\n".join(a + ["</svg>"])


# ---------------------------------------------------------------- one-cycle agent loop

def hardware_delivery_row():
    rows = [r for r in HW["ladder"] if r["mission"] == "J11-R"]
    require(len(rows) == 1, "expected exactly one J11-R ladder row")
    row = rows[0]
    require(row["evidence_label"] == EVIDENCE_HARDWARE, "J11-R evidence label changed; review the figure wording")
    require(row["provider_jobs"] == 1, "J11-R should be a one-job mission")
    return row


def loop_numbers():
    k1, k2, k4 = LANES["encoder_K1"], LANES["think_longer_worker_K2"], LANES["compounding_K4"]
    k5, k6, hw = LANES["selection_vote_K5"], LANES["narrow_then_deepen_K6"], hardware_delivery_row()
    recall, k1c = k1["recall_at_8"], k1["selection_to_agent_K1c"]
    verified_k2 = {k2["verified_out_of_12"][str(d)] for d in k2["depths"]}
    require(len(verified_k2) == 1, "K2 verified counts differ by depth; show them separately")
    return {
        "chains": k1["dataset_chains"], "recall_pool": pct(recall["code_4_pool"]), "bm25_pool": pct(recall["bm25_pool"]),
        "unfiltered": k1c["scripted_agent_verified_unfiltered"], "filtered": k1c["scripted_agent_verified_with_chain_and_status_filter"],
        "k2_verified": verified_k2.pop(), "k2_depths": ", ".join(str(d) for d in k2["depths"]),
        "recipients": hw["recipients"], "jobs": hw["provider_jobs"], "seconds": hw["billed_qpu_seconds"], "shots": hw["shots_per_circuit"],
        "first_pass": hw["first_pass_verified"], "device": hw["device"], "hw_date": HW["scope"]["dates"][-1],
        "first_try": k4["run_3b"]["first_try_verified_of_40"], "plain": k5["plain_majority"],
        "weighted": k5["reliability_weighted_vote"], "tasks": k5["tasks"],
        "deepen": k6["deepen"].split(" (")[0], "a_only": k6["a_only"]["status"],
        "spend": LANES["budget"]["model_spend_used_usd_experiment_k"], "cap": LANES["budget"]["model_spend_cap_usd"],
        "ibm_seconds": LANES["budget"]["ibm_seconds"], "gpu_hours": LANES["budget"]["gpu_hours"],
    }


def loop_description(n):
    day = short_date(n["hw_date"]).title()
    return (f"Schematic of one cycle of the agent loop. A shared evidence bank holds verified records with receipts. The encoder picks the top "
            f"eight records per agent: recall at eight was {n['recall_pool']} for the code-4 encoder against {n['bm25_pool']} for BM25 on the "
            f"pool of {n['chains']} fixture chains, measured on fixture tasks. The briefing compiler keeps only records from the same chain and "
            f"drops contradicted ones, lifting scripted-agent verification from {n['unfiltered']} to {n['filtered']} chains, measured on fixtures. "
            f"Delivery to {n['recipients']} agents ran as {n['jobs']} IBM job on {n['device']} billed {n['seconds']:.1f} seconds, "
            f"{n['first_pass']} of {n['recipients']} verified on the first try, measured on IBM hardware on {day}. Agents report HIT, MISS or "
            f"REJECT and verified records are banked with a receipt: in the compounding rehearsal {n['first_try'][0]}, then {n['first_try'][1]}, "
            f"then {n['first_try'][2]} of forty agents verified first try across three cycles, measured on fixtures. Disagreements go to a "
            f"reliability-weighted vote, which matched the answer on {n['weighted']} tasks where a plain majority managed {n['plain']}, "
            f"measured offline on fixtures. A greyed side box shows the deep cell: the think-longer worker verified {n['k2_verified']} of 12 "
            f"tasks at depths {n['k2_depths']} and stays advisory; narrow-then-deepen was {n['deepen'].lower()} under a five-dollar lane cap. "
            "A return arrow labelled next cycle leads back to the bank. Numbers come from preregistered runs on fixture tasks with known "
            "answers except the delivery stage, which ran on IBM hardware; no quantum advantage is claimed.")


def stage(x, y, w, h, name, lines, number, number_color, evidence, evidence_color):
    inner = w - 32
    a = [panel(x, y, w, h), text(x + 16, y + 24, name, 14, FG, 700, max_w=inner)]
    a += [text(x + 16, y + 43 + i * 16, line, 12, MUTED, max_w=inner) for i, line in enumerate(lines)]
    a += [text(x + 16, y + 78, number, 13, number_color, 700, max_w=inner),
          text(x + 16, y + 93, evidence, 11, evidence_color, 400, max_w=inner)]
    return a


def arrow(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{ARROW}" stroke-width="2" marker-end="url(#arrow)"/>'


def loop_stages(n):
    day = short_date(n["hw_date"]).title()
    fixtures, hardware = "measured (fixtures)", f"measured (IBM hardware, {day})"
    box_w, box_h, gap, top, bottom = 250, 100, 57, 112, 290
    xs = [MARGIN, MARGIN + box_w + gap, MARGIN + 2 * (box_w + gap)]
    a = stage(xs[0], top, box_w, box_h, "Shared evidence bank", ["verified records with receipts,", "read by every agent"],
              "seeded by a scripted warm-up", BLUE, f"{fixtures} · known answers", MUTED)
    a += stage(xs[1], top, box_w, box_h, "Encoder picks top-8 records", ["per agent, from the bank's pool", "code-4 encoder vs BM25"],
               f"recall@8: {n['recall_pool']} vs BM25 {n['bm25_pool']}", BLUE, f"{fixtures} · {n['chains']} chains", MUTED)
    a += stage(xs[2], top, box_w, box_h, "Briefing compiler filters", ["same chain only;", "drop contradicted records"],
               f"verified {n['unfiltered']} → {n['filtered']}", BLUE, f"{fixtures} · scripted agent", MUTED)
    a += stage(xs[2], bottom, box_w, box_h, f"{n['recipients']} agents, {n['jobs']} IBM job",
               [f"{n['seconds']:.1f} s billed on {n['device']}, {n['shots']} shots", "known frames, majority-vote bits"],
               f"{n['first_pass']} / {n['recipients']} first try · {n['seconds']:.1f} s", GREEN, hardware, GREEN)
    a += stage(xs[1], bottom, box_w, box_h, "Agents report verdicts", ["HIT / MISS / REJECT; verified", "records banked with a receipt"],
               f"{' → '.join(str(v) for v in n['first_try'])} of 40 first try", BLUE, f"{fixtures} · 3 cycles × 40", MUTED)
    a += stage(xs[0], bottom, box_w, box_h, "Disagreements: weighted vote", ["reliability-weighted vote", "over worker replies"],
               f"{n['weighted']} vs plain majority {n['plain']}", BLUE, f"{fixtures} · offline", MUTED)
    mid_top, mid_bottom = top + box_h // 2, bottom + box_h // 2
    a += [arrow(xs[0] + box_w, mid_top, xs[1] - 4, mid_top), arrow(xs[1] + box_w, mid_top, xs[2] - 4, mid_top),
          arrow(xs[2] + box_w // 2, top + box_h, xs[2] + box_w // 2, bottom - 4),
          arrow(xs[1], mid_bottom, xs[0] + box_w + 4, mid_bottom), arrow(xs[2], mid_bottom, xs[1] + box_w + 4, mid_bottom),
          arrow(xs[0] + box_w // 2, bottom, xs[0] + box_w // 2, top + box_h + 4),
          text(xs[0] + box_w // 2 - 10, top + box_h + 43, "next cycle", 12, GREEN, 700, 'text-anchor="end"')]
    return a


def deep_cell_box(n):
    x, y, w, h = 250, 224, 460, 54
    return [panel(x, y, w, h, fill="#0c1420", stroke="#2a3b51", extra=' stroke-dasharray="5 4"'),
            text(x + 14, y + 18, "Deep cell · side box, not in the loop", 12, DIM_TEXT, 700, max_w=w - 28),
            text(x + 14, y + 34, f"think-longer worker: {n['k2_verified']}/12 verified at depths {n['k2_depths']} · stays advisory",
                 11, DIM_TEXT, max_w=w - 28),
            text(x + 14, y + 48, f"narrow-then-deepen: {n['deepen']} · a-only {n['a_only']}", 11, AMBER, max_w=w - 28)]


def agent_loop():
    n = loop_numbers()
    title = "Quantum Comm Ops agent loop: one cycle from the shared evidence bank to the reliability-weighted vote"
    a = start(WIDTH, 452, title, loop_description(n))
    a += ['<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
          f'<path d="M0 0L10 5L0 10z" fill="{ARROW}"/></marker></defs>',
          text(MARGIN, 36, "EXPERIMENT K · ONE CYCLE · AGENT LANES: NO NEW QPU TIME · DELIVERY: 1 NOV HARDWARE",
               15, GREEN, 700, max_w=KICKER_W),
          text(WIDTH - MARGIN, 36, short_date(DATE_K), 15, MUTED, 700, 'text-anchor="end"'),
          text(MARGIN, 72, "One cycle of the agent loop", 28, FG, 700, max_w=CONTENT_W),
          text(MARGIN, 98, "Bank → encoder → compiler → 400 agents on one IBM job → verdicts → weighted vote → bank",
               15, MUTED, max_w=CONTENT_W)]
    a += loop_stages(n)
    a += deep_cell_box(n)
    a += [f'<path d="M{MARGIN} 404H{WIDTH - MARGIN}" stroke="#293b53"/>',
          text(MARGIN, 424, "Schematic · stages measured separately (fixtures; delivery on IBM hardware) · no full cycle has run with the hardware step inside",
               12, MUTED, max_w=CONTENT_W),
          text(MARGIN, 442, f"Scripted or API model workers · model spend ${n['spend']} of a ${n['cap']} cap · {n['ibm_seconds']} IBM seconds · "
               f"{n['gpu_hours']} GPU hours · no quantum advantage claimed", 12, MUTED, max_w=CONTENT_W)]
    return "\n".join(a + ["</svg>"])


OUTPUTS = {"quantum-comm-ops-compounding.svg": compounding, "quantum-comm-ops-agent-loop.svg": agent_loop}


def main(argv):
    check = "--check" in argv
    require("November 1, 2026" in LANES["scope"], "agent_lanes scope no longer names the expected date")
    failures = 0
    for name, build in OUTPUTS.items():
        out = HERE / name
        content = (build() + "\n").encode("utf-8")
        if check:
            same = out.exists() and out.read_bytes() == content
            print(name, "ok" if same else "DIFFERS")
            failures += 0 if same else 1
        else:
            out.write_bytes(content)
            print(name, len(content), "bytes")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
