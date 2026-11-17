"""Build the Model-1 SVGs from the public JSON; no experiment calls.

Figures:
  model1-training-mission.svg  lane run R1 (measured on fixtures)
  model1-rsi-loop.svg          the self-improvement loop (design, with what each step has measured)
  model1-replay.svg            replay at ~0 inference (design, with its first measurements)
  model1-pl1.svg               the first test of the loop, PL1 (measured on fixtures)
  model1-replay-path.svg       Model 1's replay path, the depth ladder T3 stage A (measured on fixtures)

Run from the repository root: python docs/assets/build_model1_assets.py [--check]
--check rebuilds in memory and exits non-zero if any published SVG differs from the rebuild.
"""
import json
import sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE.parent / "research/quantum-comm-ops.json").read_text(encoding="utf-8"))
R1 = DATA["model1_lane_run_r1_2026_11_12"]
PL1 = DATA["model1_pl1_2026_11_16"]
LOOP = DATA["model1_rsi_loop_2026_11_17"]
RP = DATA["model1_replay_path_2026_11_15"]
TRACE = DATA["model1_trace_runs_2026_11_14_15"]
BG, FG, MUTED = "#070d17", "#f2f6ff", "#adbbce"
BLUE, PURPLE, GREEN, AMBER = "#32c7eb", "#b48aff", "#67dcb4", "#efc479"
DIM, DIM_TEXT, ARROW, LINE = "#3b4f68", "#8696ad", "#5f7a99", "#293b53"
CHAR_W = 0.55
WIDTH, MARGIN = 960, 48
CONTENT_W = WIDTH - 2 * MARGIN
STATUS_COLOR = {"measured": GREEN, "partly measured": BLUE, "built": BLUE, "preregistered": PURPLE,
                "design": AMBER, "not measured": DIM_TEXT, "people today": MUTED}


def fit(value, size, max_w):
    """Shrink the font size until the value fits; never below 9px."""
    while len(str(value)) * size * CHAR_W > max_w and size > 9:
        size = max(size - 1, 9)
    return size


def text(x, y, value, size=20, color=FG, weight=400, extra="", max_w=None):
    value = str(value)
    if max_w is not None:
        size = fit(value, size, max_w)
        if len(value) * size * CHAR_W > max_w:
            raise ValueError(f"text overflows {max_w}px at {size}px ({len(value) * size * CHAR_W:.0f}px): {value!r}")
    return (f'<text x="{x}" y="{y}" font-family="Helvetica,Arial,sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" {extra}>{escape(value)}</text>')


def wrap(value, size, max_w):
    """Greedy word wrap at the estimated width."""
    lines, cur = [], []
    for wd in str(value).split():
        if cur and len(" ".join(cur + [wd])) * size * CHAR_W > max_w:
            lines.append(" ".join(cur))
            cur = [wd]
        else:
            cur.append(wd)
    if cur:
        lines.append(" ".join(cur))
    return lines


def start(width, height, title, description):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
            f'role="img" aria-labelledby="title description">',
            f'<title id="title">{escape(title)}</title><desc id="description">{escape(description)}</desc>',
            '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10z" fill="{ARROW}"/></marker></defs>',
            f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="18" fill="{BG}" stroke="#2a3b51"/>']


def panel(x, y, width, height, fill="#101b2b", stroke="#293e57", radius=12, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}" stroke="{stroke}"{d}/>'


def arrow(x1, y1, x2, y2, color=ARROW):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="2" fill="none" marker-end="url(#arr)"/>'


def path_arrow(d, color=ARROW, dash=""):
    dd = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" stroke="{color}" stroke-width="2" fill="none"{dd} marker-end="url(#arr)"/>'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def header(kicker, kicker_color, date, title_lines, subtitle):
    """Kicker + date, one or two title lines, one subtitle; returns the elements and the subtitle's baseline."""
    a = [text(MARGIN, 40, kicker, 15, kicker_color, 700, max_w=CONTENT_W - 150),
         text(WIDTH - MARGIN, 40, date, 15, MUTED, 700, 'text-anchor="end"')]
    y = 82
    for line in title_lines:
        a.append(text(MARGIN, y, line, 30, FG, 700, max_w=CONTENT_W))
        y += 34
    a.append(text(MARGIN, y - 8, subtitle, 14, MUTED, max_w=CONTENT_W))
    return a, y - 8


def box(x, y, w, h, title, sub, color, fill="#101b2b"):
    a = [panel(x, y, w, h, fill=fill, stroke=color)]
    if sub:
        a += [text(x + w / 2, y + h / 2 - 3, title, 14, color, 700, 'text-anchor="middle"', w - 12),
              text(x + w / 2, y + h / 2 + 13, sub, 10.5, MUTED, 400, 'text-anchor="middle"', w - 12)]
    else:
        a.append(text(x + w / 2, y + h / 2 + 5, title, 14, color, 700, 'text-anchor="middle"', w - 12))
    return a


def box_wrapped(x, y, w, h, title, color, fill="#101b2b", size=12):
    lines = wrap(title, size, w - 14)
    require(len(lines) <= 2, f"box title needs more than two lines: {title!r}")
    a = [panel(x, y, w, h, fill=fill, stroke=color)]
    top = y + h / 2 + 4 - (len(lines) - 1) * 8
    for i, line in enumerate(lines):
        a.append(text(x + w / 2, top + i * 16, line, size, color, 700, 'text-anchor="middle"', w - 10))
    return a


# ---------------------------------------------------------------- figure 1: the training mission (R1)

def mission_numbers():
    ops = R1["operators_on_the_same_mission"]
    asked = R1["model_proposals"]["per_stage_asked"]
    require(R1["evidence_label"] == "measured_on_fixtures", "R1 evidence label changed; review the figure wording")
    require(R1["model_proposals"]["valid"] == R1["model_proposals"]["total"] == sum(asked.values()), "R1 proposal counts inconsistent")
    rows = [("Oracle, no selection (ceiling)", ops["oracle_no_selection_ceiling"], DIM),
            ("Oracle with selection", ops["oracle_with_selection"], DIM),
            ("Trained 9B model with selection", ops["trained_model_lane_bc_1_with_selection"], BLUE),
            ("Scripted rule with selection (floor)", ops["scripted_rule_with_selection_floor"], AMBER)]
    return ops, asked, rows


def mission_description(asked, rows):
    return (f"Lane run R1, November 12, 2026, measured on fixtures with no quantum-computer time. A 9-billion-parameter model with an "
            f"adapter trained on {R1['adapter']['train_rows']} teacher rows drove one whole {R1['mission']['pins']}-pin synthetic mission: "
            f"{asked['C1_PIN']} proposals at each of C1, C2 and C3, a selection step solved exactly on CPU that let {asked['Q1_OPTIMIZE']} "
            f"pins go on and parked {R1['mission']['pins'] - asked['Q1_OPTIMIZE']}, then {asked['Q1_OPTIMIZE']} proposals at each of Q1, Q2 "
            f"and Q3; {R1['model_proposals']['valid']} of {R1['model_proposals']['total']} proposals valid, none refused. Findings found of "
            f"{R1['mission']['planted_findings']}: " + "; ".join(f"{n} {r['found_of_178']} with {r['false_alarms_of_222']} false alarms"
                                                                 for n, r, _ in rows) +
            f". Preregistered verdict {R1['rules']['verdict'].split(' (')[0]}. Caveats on the figure: a fixture shortcut picks the true sink in all "
            f"{R1['mission']['two_sink_findings']} two-sink functions, the final decision is mostly a read-back of verifier evidence, "
            f"and the model had no part in selection. Cost about {R1['cost']['usd_from_node_time']} dollars of a {R1['cost']['line_usd']} "
            f"dollar line on CPU. No quantum advantage is claimed.")


def stage_row(y):
    asked = R1["model_proposals"]["per_stage_asked"]
    agreed = R1["model_proposals"]["energy_prediction_agreed"]
    stages = [("C1", "pin", "C1_PIN"), ("C2", "analyse", "C2_ANALYZE"), ("C3", "search", "C3_SEARCH"), None,
              ("Q1", "optimise", "Q1_OPTIMIZE"), ("Q2", "refine", "Q2_REFINE"), ("Q3", "decide", "Q3_DECIDE")]
    a, x, w, gap, sel_w = [], MARGIN, 98, 18, 138
    for s in stages:
        if s is None:
            parked = R1["mission"]["pins"] - asked["Q1_OPTIMIZE"]
            a += [panel(x, y, sel_w, 92, fill="#1a1630", stroke=PURPLE),
                  text(x + sel_w / 2, y + 24, "SELECT", 15, PURPLE, 700, 'text-anchor="middle"'),
                  text(x + sel_w / 2, y + 44, f"{asked['Q1_OPTIMIZE']} go on · {parked} parked", 12, FG, 400, 'text-anchor="middle"', sel_w - 8),
                  text(x + sel_w / 2, y + 61, "verifier scores, exact", 11, MUTED, 400, 'text-anchor="middle"', sel_w - 8),
                  text(x + sel_w / 2, y + 76, "CPU solve · not the model", 11, MUTED, 400, 'text-anchor="middle"', sel_w - 8),
                  arrow(x + sel_w + 2, y + 46, x + sel_w + gap - 2, y + 46)]
            x += sel_w + gap
            continue
        code, name, key = s
        color = BLUE if code.startswith("C") else GREEN
        a += [panel(x, y, w, 92, stroke=color),
              text(x + w / 2, y + 26, code, 20, color, 700, 'text-anchor="middle"'),
              text(x + w / 2, y + 44, name, 12, MUTED, 400, 'text-anchor="middle"'),
              text(x + w / 2, y + 64, f"{asked[key]}/{asked[key]} valid", 12, FG, 700, 'text-anchor="middle"', w - 6),
              text(x + w / 2, y + 80, f"{agreed[key]} agreed", 11, MUTED, 400, 'text-anchor="middle"')]
        if code != "Q3":
            a.append(arrow(x + w + 2, y + 46, x + w + gap - 2, y + 46))
        x += w + gap
    require(x - gap <= WIDTH - MARGIN + 1, f"stage row overflows ({x - gap}px)")
    return a


def findings_panel(x, y, w, h, rows):
    total = R1["mission"]["planted_findings"]
    a = [panel(x, y, w, h), text(x + 22, y + 30, f"Findings found, of {total} planted", 17, GREEN, 700, max_w=w - 44),
         text(x + 22, y + 50, f"same 400-pin mission · false alarms of {R1['mission']['safe_pins']} safe pins · two-sink of "
                              f"{R1['mission']['two_sink_findings']}", 11, MUTED, max_w=w - 44)]
    bar_x, bar_w_max, row_h = x + 22, w - 44 - 150, 44
    for i, (name, r, color) in enumerate(rows):
        by = y + 70 + i * row_h
        bw = bar_w_max * r["found_of_178"] / total
        strong = color == BLUE
        a += [text(bar_x, by + 12, name, 12, FG if strong else MUTED, 700 if strong else 400, max_w=w - 44),
              f'<rect x="{bar_x}" y="{by + 18}" width="{bar_w_max:.1f}" height="14" rx="4" fill="#0c1522"/>',
              f'<rect x="{bar_x}" y="{by + 18}" width="{bw:.1f}" height="14" rx="4" fill="{color}"/>',
              text(bar_x + bw + 8, by + 30, r["found_of_178"], 15, FG, 700),
              text(x + w - 22, by + 30, f"{r['false_alarms_of_222']} false · {r['two_sink_found_of_54']} two-sink", 11, MUTED, 400,
                   'text-anchor="end"')]
    return a


def reading_panel(x, y, w, h):
    m, rule = R1["model_proposals"], R1["rules"]
    a = [panel(x, y, w, h), text(x + 22, y + 30, "What it shows, and what it does not", 17, AMBER, 700, max_w=w - 44)]
    lines = [
        (GREEN, f"{m['valid']:,} of {m['total']:,} proposals valid, {m['refused']} refused: the model drives every stage."),
        (GREEN, f"Rule: at least 160 found, at most 3 false alarms. Got 172 and 3. {rule['verdict'].split(' (')[0]}, at its edge."),
        (GREEN, f"{R1['adapter']['train_rows']} teacher rows, one pass; about ${R1['cost']['usd_from_node_time']} of ${R1['cost']['line_usd']} on CPU."),
        (AMBER, "A fixture shortcut also picks the true sink 54 of 54 times: the gain over the rule is not yet tracing skill."),
        (AMBER, "From C3 on the verifier hands over the evidence; the final decision is mostly a read-back."),
        (AMBER, "Selection was the verifier's, not the model's. One seed, synthetic code, no real code."),
    ]
    ty = y + 58
    for color, line in lines:
        a.append(f'<circle cx="{x + 28}" cy="{ty - 4}" r="4" fill="{color}"/>')
        for p in wrap(line, 11, w - 62):
            a.append(text(x + 40, ty, p, 11, FG, 400, max_w=w - 62))
            ty += 14
        ty += 10
    require(ty <= y + h, f"reading panel overflows ({ty - y} > {h})")
    return a


def mission_figure():
    _, asked, rows = mission_numbers()
    title = "Model-1 lane run R1: one 9B model drives a 400-pin mission end to end"
    a = start(WIDTH, 604, title, mission_description(asked, rows))
    a += [text(MARGIN, 40, "MODEL-1 · LANE RUN R1 · MEASURED ON FIXTURES, NO QUANTUM-COMPUTER TIME", 15, GREEN, 700, max_w=CONTENT_W - 150),
          text(WIDTH - MARGIN, 40, "12 NOV 2026", 15, MUTED, 700, 'text-anchor="end"'),
          text(MARGIN, 82, "One 9B model drives a 400-pin mission end to end", 30, FG, 700, max_w=CONTENT_W),
          text(MARGIN, 108, f"400 synthetic pins · {R1['mission']['planted_findings']} planted findings · six stages · "
                            "every proposal verified before the next stage", 14, MUTED, max_w=CONTENT_W)]
    a += stage_row(130)
    a += findings_panel(MARGIN, 246, 430, 300, rows)
    a += reading_panel(MARGIN + 454, 246, 410, 300)
    a += [f'<path d="M{MARGIN} 562H{WIDTH - MARGIN}" stroke="{LINE}"/>',
          text(MARGIN, 584, "Preregistered before the job existed · verdict BEATS THE RULE · oracle = the scripted teacher with planted truth · "
                            "no quantum advantage claimed", 12, MUTED, max_w=CONTENT_W)]
    return "\n".join(a + ["</svg>"])


# ---------------------------------------------------------------- figure 2: the self-improvement loop (design)

def loop_description():
    steps = "; ".join(f"{s['step']}: {s['status']}, {s['today']}" for s in LOOP["steps_for_the_figure"])
    signal = "; ".join(LOOP["rsi_signal_not_measured"]["all_four_at_once"])
    return (f"Design figure with what each step has measured, November 17, 2026. {LOOP['one_line']} The loop: {LOOP['loop_line']} "
            f"When Model 1 is stuck there are two doors. Door 1, search: {LOOP['two_doors']['evidence_missing']}. Door 2, absorb: "
            f"{LOOP['two_doors']['evidence_on_screen']}. Both lead to an independent verifier, then the Atlas bank, then replay at about zero "
            f"model inference (procedural learning) and training into Model 1 (neural learning). Where each step stands: {steps}. "
            f"What would count as self-improvement, not measured yet: {signal}. {LOOP['claims_boundary']}")


def loop_panel(x, y, w, h):
    a = [panel(x, y, w, h), text(x + 22, y + 30, "The loop (design)", 17, PURPLE, 700, max_w=w - 44),
         text(x + 22, y + 50, "what each part does first; its name in small print", 11, MUTED, max_w=w - 44)]
    bw, bh, step = 220, 46, 75
    cx = x + w / 2
    lx, rx = x + 24, x + w - 24 - bw
    lcx, rcx = lx + bw / 2, rx + bw / 2
    r = [y + 70 + i * step for i in range(8)]
    a += box(cx - bw / 2, r[0], bw, bh, "Model 1 works the pin", "reasons and acts · the student", BLUE, fill="#0f1e2c")
    a.append(arrow(cx, r[0] + bh, cx, r[1] - 2))
    a += box(cx - bw / 2, r[1], bw, bh, "Stuck: what is missing?", "the exact stuck point is saved (a halt)", FG)
    a += [arrow(cx - 40, r[1] + bh, lcx, r[2] - 2), arrow(cx + 40, r[1] + bh, rcx, r[2] - 2),
          text(lcx - 14, r[2] - 10, "evidence missing", 10.5, GREEN, 700, 'text-anchor="end"'),
          text(rcx + 14, r[2] - 10, "evidence on screen", 10.5, PURPLE, 700)]
    a += box(lx, r[2], bw, bh, "Door 1 · SEARCH", "find the missing piece", GREEN, fill="#0f2320")
    a += box(rx, r[2], bw, bh, "Door 2 · ABSORB", "use what is already there", PURPLE, fill="#1a1630")
    a += [arrow(lcx, r[2] + bh, lcx, r[3] - 2), arrow(rcx, r[2] + bh, rcx, r[3] - 2)]
    a += box(lx, r[3], bw, bh, "Make a small search", "adaptive energy tokenizer (Nano)", GREEN)
    a += box(rx, r[3], bw, bh, "Train the decision", "first run: D1", PURPLE)
    a.append(arrow(lcx, r[3] + bh, lcx, r[4] - 2))
    a += box(lx, r[4], bw, bh, "Try candidates fast", "miss · colder · warmer · hit", GREEN)
    a += [text(lx, r[4] + bh + 14, "brute force · quantum oracle optional", 9.5, DIM_TEXT, 400, max_w=bw),
          text(lx, r[4] + bh + 26, "level 3 · discovery", 9.5, GREEN, 700, max_w=bw)]
    a += [arrow(lcx + 60, r[4] + bh, cx - 30, r[5] - 2), arrow(rcx, r[3] + bh, cx + 30, r[5] - 2)]
    a += box(cx - bw / 2, r[5], bw, bh, "Prove it is right", "independent verifier", AMBER)
    a.append(arrow(cx, r[5] + bh, cx, r[6] - 2))
    a += box(cx - bw / 2, r[6], bw, bh, "Remember it", "Atlas bank · the notebook", GREEN, fill="#0f2320")
    a += [arrow(cx - 40, r[6] + bh, lcx, r[7] - 2), arrow(cx + 40, r[6] + bh, rcx, r[7] - 2)]
    a += box(lx, r[7], bw, bh, "Replay it · ~0 inference", "AQRC: a step the system runs", BLUE, fill="#0f1e2c")
    a += box(rx, r[7], bw, bh, "Train it in", "the next Model 1 learns it", PURPLE, fill="#1a1630")
    a += [text(lx, r[7] + bh + 14, "level 2 · procedural", 9.5, BLUE, 700, max_w=bw),
          text(rx + bw, r[7] + bh + 14, "level 1 · neural", 9.5, PURPLE, 700, 'text-anchor="end"', bw)]
    mid1 = r[0] + bh / 2
    a += [path_arrow(f"M{lx} {r[7] + bh / 2}H{x + 10}V{mid1}H{cx - bw / 2 - 4}", dash="5 4"),
          path_arrow(f"M{rx + bw} {r[7] + bh / 2}H{x + w - 10}V{mid1}H{cx + bw / 2 + 4}", dash="5 4"),
          text(x + 16, r[0] - 8, "goes farther now", 9.5, DIM_TEXT, 400, max_w=150),
          text(x + w - 16, r[0] - 8, "goes farther next generation", 9.5, DIM_TEXT, 400, 'text-anchor="end"', 170)]
    require(r[7] + bh + 26 <= y + h, f"loop panel overflows ({r[7] + bh + 26 - y} > {h})")
    return a


def status_panel(x, y, w, h):
    a = [panel(x, y, w, h), text(x + 20, y + 30, "Where each step stands", 17, GREEN, 700, max_w=w - 40),
         text(x + 20, y + 50, "measured on fixtures unless marked", 10.5, MUTED, max_w=w - 40)]
    ty = y + 80
    for s in LOOP["steps_for_the_figure"]:
        color = STATUS_COLOR[s["status"]]
        a += [f'<circle cx="{x + 26}" cy="{ty - 5}" r="5" fill="{color}"/>',
              text(x + 38, ty, s["step"], 12.5, FG, 700, max_w=w - 58),
              text(x + 38, ty + 14, s["status"].upper(), 9.5, color, 700, max_w=w - 58)]
        lines = wrap(s["today"], 10, w - 58)
        require(len(lines) <= 3, f"status line too long: {s['today']!r}")
        for i, line in enumerate(lines):
            a.append(text(x + 38, ty + 28 + i * 12, line, 10, MUTED, max_w=w - 58))
        ty += 28 + 12 * len(lines) + 12
    require(ty <= y + h, f"status panel overflows ({ty - y} > {h})")
    return a


def signal_strip(x, y, w, h):
    sig = LOOP["rsi_signal_not_measured"]
    a = [panel(x, y, w, h, fill="#0d1420", stroke=DIM),
         text(x + 20, y + 24, "What would count as self-improvement · not measured yet", 13, AMBER, 700, max_w=w - 40)]
    items = sig["all_four_at_once"]
    col = (w - 40) / len(items)
    for i, item in enumerate(items):
        head, tail = item.split(": ", 1)
        cx = x + 20 + i * col
        a += [text(cx, y + 46, head[0].upper() + head[1:], 12, FG, 700, max_w=col - 12),
              text(cx, y + 62, tail, 10.5, MUTED, max_w=col - 12)]
    a.append(text(x + 20, y + h - 10, f"All four at once, across trained generations; {sig['not_the_signal']} is not the signal.", 10, DIM_TEXT,
                  max_w=w - 40))
    return a


def loop_figure():
    title = "Gen3 to Gen4: the self-improvement loop, by what each part does"
    a = start(WIDTH, 1000, title, loop_description())
    hdr, _ = header("GEN3 → GEN4 · THE SELF-IMPROVEMENT LOOP · DESIGN, WITH WHAT EACH STEP HAS MEASURED", AMBER, "17 NOV 2026",
                    ["Turn failure into verified capability,", "and verified capability into a stronger model"],
                    "Stuck → find what was missing → prove it → remember it → replay it → train it in → go farther alone")
    a += hdr
    a += loop_panel(MARGIN, 166, 528, 670)
    a += status_panel(MARGIN + 552, 166, 312, 670)
    a += signal_strip(MARGIN, 852, CONTENT_W, 92)
    a += [f'<path d="M{MARGIN} 958H{WIDTH - MARGIN}" stroke="{LINE}"/>',
          text(MARGIN, 980, "Design and hypothesis · no generation trained on its own rescues yet · classical loop, quantum oracle optional · "
                            "no frontier-level capability claimed · no quantum advantage", 11, MUTED, max_w=CONTENT_W)]
    return "\n".join(a + ["</svg>"])


# ---------------------------------------------------------------- figure 3: replay at ~0 inference

def replay_description():
    rp = LOOP["replay"]
    return (f"Design figure with first measurements, November 17, 2026. Solve it once, run it again without the model. First time: "
            f"{'; '.join(rp['first_time'])}. Next time: {'; '.join(rp['next_time'])}. {rp['not_rag']} Why it matters for a small model: "
            f"{rp['why_small_model']}. Measured on fixtures: {'; '.join(rp['measured'])}. Status: {rp['status']}. Synthetic code; "
            "no quantum-computer time.")


def lane(y, label, label_color, items, colors, x0=170, bw=134, gap=18, bh=64):
    a = [text(MARGIN, y + bh / 2 + 5, label, 13, label_color, 700, max_w=x0 - MARGIN - 10)]
    for i, (item, color) in enumerate(zip(items, colors)):
        x = x0 + i * (bw + gap)
        a += box_wrapped(x, y, bw, bh, item[0].upper() + item[1:], color)
        if i < len(items) - 1:
            a.append(arrow(x + bw + 2, y + bh / 2, x + bw + gap - 2, y + bh / 2))
    return a


def replay_figure():
    rp = LOOP["replay"]
    require(len(rp["first_time"]) == 5 and len(rp["next_time"]) == 4, "replay lanes changed shape; review the figure")
    title = "Replay at about zero model inference: solve it once, run it again without the model"
    a = start(WIDTH, 642, title, replay_description())
    hdr, _ = header("REPLAY AT ~0 INFERENCE · DESIGN, WITH ITS FIRST MEASUREMENTS", BLUE, "17 NOV 2026",
                    ["Solve it once. Run it again without the model."], rp["not_rag"])
    a += hdr
    x0, bw, gap, bh = 170, 134, 18, 64
    ya, yb = 150, 290
    a += lane(ya, "FIRST TIME", PURPLE, rp["first_time"], [BLUE, GREEN, AMBER, BLUE, GREEN], x0, bw, gap, bh)
    a += lane(yb, "NEXT TIME", GREEN, rp["next_time"], [FG, GREEN, BLUE, FG], x0, bw, gap, bh)
    bx = x0 + 4 * (bw + gap)
    a += [panel(bx, yb, bw, bh, fill="#0f2320", stroke=GREEN),
          text(bx + bw / 2, yb + 28, "model inference", 12, GREEN, 700, 'text-anchor="middle"', bw - 10),
          text(bx + bw / 2, yb + 50, "≈ 0", 20, GREEN, 700, 'text-anchor="middle"', bw - 10),
          arrow(bx - gap + 2, yb + bh / 2, bx - 2, yb + bh / 2)]
    atlas_cx = x0 + 4 * (bw + gap) + bw / 2
    match_cx = x0 + (bw + gap) + bw / 2
    mid = (ya + bh + yb) / 2
    a += [path_arrow(f"M{atlas_cx} {ya + bh}V{mid}H{match_cx}V{yb - 2}", color=GREEN, dash="5 4"),
          text(match_cx + 12, mid - 7, "the stored step is found again", 10, DIM_TEXT, max_w=300)]
    py, ph = 386, 194
    a += [panel(MARGIN, py, CONTENT_W, ph),
          text(MARGIN + 22, py + 30, "Where it stands · measured on fixtures", 16, GREEN, 700, max_w=CONTENT_W - 44),
          text(MARGIN + 22, py + 48, rp["why_small_model"][0].upper() + rp["why_small_model"][1:] + ".", 10.5, MUTED, max_w=CONTENT_W - 44)]
    ty = py + 76
    for color, line in zip([BLUE, AMBER, BLUE], rp["measured"]):
        a.append(f'<circle cx="{MARGIN + 28}" cy="{ty - 4}" r="4" fill="{color}"/>')
        for p in wrap(line[0].upper() + line[1:] + ".", 11.5, CONTENT_W - 66):
            a.append(text(MARGIN + 42, ty, p, 11.5, FG, 400, max_w=CONTENT_W - 66))
            ty += 15
        ty += 12
    require(ty <= py + ph, f"replay panel overflows ({ty - py} > {ph})")
    a += [f'<path d="M{MARGIN} 598H{WIDTH - MARGIN}" stroke="{LINE}"/>',
          text(MARGIN, 620, f"Design · {rp['status']} · synthetic code · no quantum-computer time", 11, MUTED, max_w=CONTENT_W)]
    return "\n".join(a + ["</svg>"])


# ---------------------------------------------------------------- figure 4: the first test of the loop (PL1)

def pl1_numbers():
    s2 = PL1["stage_2"]
    require(PL1["evidence_label"] == "measured_on_fixtures", "PL1 evidence label changed; review the figure wording")
    miss = s2["verified_of_50_evidence_missing"]
    floor = s2["noise_floor_states"]
    p, b, t, c = miss["P"], miss["B"], miss["T"], miss["C_seeds"]
    require(max(c) - min(c) == floor, "the noise floor is the spread of the random-search seeds")
    require(t - p > floor and b - p <= floor, "figure wording assumes T clears the floor over P and B does not")
    return s2, p, b, t, c, floor


def pl1_description():
    s2, p, b, t, c, floor = pl1_numbers()
    on = s2["verified_of_50_evidence_on_screen"]
    fa = s2["false_alarms_of_50_evidence_on_screen"]
    return (f"First test of the self-improvement loop, PL1, November 16, 2026, measured on fixtures with no quantum-computer time. "
            f"100 of Model 1's own stuck points, each read once from a hint and counted only when the verifier's tight rule confirms. "
            f"Evidence missing, 50 stuck points, verified: placebo {p}, Nano lockpick {b}, random hint {', '.join(map(str, c))} across five seeds, "
            f"teacher's hint {t}. The noise floor is {floor}: two random seeds differ by up to {floor}. Teacher's hint against placebo, net "
            f"{t - p}, is above the floor: IMPROVED. Lockpick against placebo, net {b - p}, is not: no difference; lockpick against the random "
            f"hint: no difference at any seed. Evidence on screen, 50 stuck points, verified: placebo {on['P']}, lockpick {on['B']}, random "
            f"{on['C']}, teacher {on['T']}; false alarms {fa['P']}, {fa['B']}, {fa['C']}, {fa['T']}. No hint helped there. Verdict: "
            f"{s2['verdict']}. Next: train the decision, run D1, sealed and not yet run. No quantum advantage claimed.")


def missing_panel(x, y, w, h):
    s2, p, b, t, c, floor = pl1_numbers()
    a = [panel(x, y, w, h), text(x + 22, y + 30, "Evidence missing · 50 stuck points", 16, GREEN, 700, max_w=w - 44),
         text(x + 22, y + 48, f"verified, of 50 · noise floor: two random seeds differ by up to {floor}", 10.5, MUTED, max_w=w - 44)]
    base, scale = y + h - 58, 10
    for v in (5, 10, 15, 20):
        gy = base - v * scale
        a += [f'<path d="M{x + 44} {gy}H{x + w - 18}" stroke="#1b2a3d"/>', text(x + 36, gy + 4, v, 9.5, DIM_TEXT, 400, 'text-anchor="end"')]
    a.append(f'<path d="M{x + 44} {base}H{x + w - 18}" stroke="#2e4560"/>')
    centers = [x + 100 + i * 118 for i in range(4)]
    groups = [("Placebo", "its own halt again", p, DIM_TEXT), ("Nano lockpick", "the search door", b, BLUE),
              ("Random hint", "five seeds", None, MUTED), ("Teacher's hint", "shortest continuation", t, GREEN)]
    for cx, (name, sub, val, color) in zip(centers, groups):
        if val is not None:
            a += [f'<rect x="{cx - 30}" y="{base - val * scale}" width="60" height="{val * scale}" rx="4" fill="{color}"/>',
                  text(cx, base - val * scale - 8, val, 16, FG, 700, 'text-anchor="middle"')]
        else:
            lo, hi = min(c), max(c)
            a += [f'<rect x="{cx - 30}" y="{base - hi * scale}" width="60" height="{(hi - lo) * scale}" rx="4" fill="#1d2b3e" stroke="{DIM}"/>',
                  text(cx, base - hi * scale - 8, f"{lo}–{hi}", 16, FG, 700, 'text-anchor="middle"')]
            for i, v in enumerate(c):
                a.append(f'<circle cx="{cx - 20 + i * 10}" cy="{base - v * scale}" r="4" fill="{MUTED}"/>')
        a += [text(cx, base + 18, name, 12, FG, 700, 'text-anchor="middle"', 112),
              text(cx, base + 33, sub, 9.5, MUTED, 400, 'text-anchor="middle"', 112)]
    return a


def onscreen_panel(x, y, w, h):
    s2 = PL1["stage_2"]
    on, fa = s2["verified_of_50_evidence_on_screen"], s2["false_alarms_of_50_evidence_on_screen"]
    a = [panel(x, y, w, h), text(x + 20, y + 30, "Evidence on screen · 50 stuck points", 16, AMBER, 700, max_w=w - 40),
         text(x + 20, y + 48, "verified (green) and false alarms (amber), of 50", 10.5, MUTED, max_w=w - 40)]
    names = [("P", "Placebo"), ("B", "Lockpick"), ("C", "Random"), ("T", "Teacher")]
    bx, scale, ty = x + 96, (w - 96 - 40) / 50, y + 78
    for key, name in names:
        vw = max(on[key] * scale, 2)
        a += [text(x + 20, ty + 13, name, 12, FG, 700, max_w=70),
              f'<rect x="{bx}" y="{ty}" width="{vw:.1f}" height="9" rx="2" fill="{GREEN}"/>',
              text(bx + vw + 6, ty + 8.5, on[key], 10, GREEN, 700),
              f'<rect x="{bx}" y="{ty + 13}" width="{fa[key] * scale:.1f}" height="9" rx="2" fill="{AMBER}"/>',
              text(bx + fa[key] * scale + 6, ty + 21.5, fa[key], 10, AMBER, 700)]
        ty += 44
    for i, line in enumerate(wrap("No hint helped. The model saw what it needed and still decided wrong.", 11, w - 40)):
        a.append(text(x + 20, y + h - 30 + i * 14, line, 11, FG, 700, max_w=w - 40))
    require(ty <= y + h - 40, f"on-screen panel overflows ({ty - y} > {h - 40})")
    return a


def pl1_figure():
    s2, p, b, t, c, floor = pl1_numbers()
    title = "First test of the self-improvement loop (PL1): where Model 1 got stuck, did a hint help?"
    a = start(WIDTH, 668, title, pl1_description())
    hdr, _ = header("FIRST TEST OF THE LOOP (PL1) · MEASURED ON FIXTURES, NO QUANTUM-COMPUTER TIME", GREEN, "16 NOV 2026",
                    ["Where Model 1 got stuck, did a hint help?"],
                    "100 of Model 1's own stuck points · each read once from a hint · counted only when the verifier's tight rule confirms")
    a += hdr
    a += missing_panel(MARGIN, 130, 528, 350)
    a += onscreen_panel(MARGIN + 552, 130, 312, 350)
    vy = 498
    lines = [(GREEN, f"Teacher's hint vs placebo: net +{t - p}, above the noise floor of {floor} → IMPROVED", 400),
             (AMBER, f"Nano lockpick vs placebo: net +{b - p}, inside the noise floor → no difference; vs the random hint: no difference at any seed", 400),
             (FG, "Verdict: ONLY THE TEACHER'S SEAT ADVANCES MODEL 1 · NOT ABOVE GUESSING ON BOTH KINDS OF PIN", 700)]
    a.append(panel(MARGIN, vy, CONTENT_W, 100, fill="#0d1420", stroke=DIM))
    for i, (color, line, weight) in enumerate(lines):
        a += [f'<circle cx="{MARGIN + 24}" cy="{vy + 26 + i * 26}" r="4" fill="{color}"/>',
              text(MARGIN + 38, vy + 30 + i * 26, line, 12.5, FG, weight, max_w=CONTENT_W - 60)]
    a += [f'<path d="M{MARGIN} 618H{WIDTH - MARGIN}" stroke="{LINE}"/>',
          text(MARGIN, 640, "Preregistered · reproduced byte for byte · synthetic code · no training in this test · "
                            "next: train the decision (D1, sealed, not yet run) · no quantum advantage claimed", 11, MUTED, max_w=CONTENT_W)]
    return "\n".join(a + ["</svg>"])


# ---------------------------------------------------------------- figure 5: Model 1's replay path (T3 stage A, measured)

STARTS = ("zero", "p25", "half", "p75", "last")


def cap(value):
    return value[0].upper() + value[1:]


def replay_path_numbers():
    require(RP["evidence_label"] == "measured_on_fixtures", "replay-path evidence label changed; review the figure wording")
    ladder, same, pin = RP["ladder"], RP["same_answer_fewer_replies"], RP["example_pin"]
    require(tuple(r["start"] for r in ladder) == STARTS, "ladder starts changed; review the figure")
    published = TRACE["T3_stage_A_depth_ladder"]["findings_verified_of_32"]
    require({r["start"]: r["verified_of_32"] for r in ladder} == published, "ladder disagrees with the published T3 stage A block")
    replayed = [r["replayed_calls"] for r in ladder]
    require(replayed[0] == 0 and replayed == sorted(replayed), "replayed calls must start at zero and grow")
    require(max(r["verified_of_32"] for r in ladder[:-1]) < ladder[-1]["verified_of_32"], "wording assumes only the end steps up")
    require(same["model_replies_from_the_end"] < same["model_replies_from_scratch"], "wording assumes fewer replies from the end")
    strips = pin["strips"]
    require(tuple(s["start"] for s in strips) == STARTS, "example strips changed; review the figure")
    require([s["replayed"] for s in strips] == list(range(len(strips))) and strips[-1]["replayed"] == pin["proven_path_calls"],
            "example strips assume one more replayed call per start, ending at the whole path")
    require(all(s["verifier"] == "NOT_CONFIRMED" for s in strips[:-1]) and strips[-1]["verifier"] == "CONFIRMED"
            and not strips[-1]["model_calls"], "example wording assumes only the end is confirmed, with no model call")
    return ladder, same, pin


def replay_path_description():
    ladder, same, pin = replay_path_numbers()
    labels = {r["start"]: r["label"] for r in ladder}
    rows = "; ".join(f"{r['label']}: {r['replayed_calls']} calls replayed, {r['model_replies']} model replies, "
                     f"{r['verified_of_32']} of 32 findings verified, {r['false_alarms_of_28']} false alarms of 28" for r in ladder)
    strips = "; ".join(f"{labels[s['start']]}: {s['replayed']} replayed, {len(s['model_calls'])} model calls, claims {s['claim']}, "
                       f"{'confirmed' if s['verifier'] == 'CONFIRMED' else 'not confirmed'}" for s in pin["strips"])
    return (f"Model 1's replay path, measured on fixtures with no quantum-computer time, November 15, 2026 (the depth ladder, T3 stage A). "
            f"{cap(RP['what_replayed_means'])}. The same trained 9B started at five points of the scripted teacher's proven path on "
            f"{RP['dev_pins']} synthetic pins with {RP['findings_planted']} planted findings. {rows}. On the {same['findings']} findings "
            f"verified from every start, model replies fell from {same['model_replies_from_scratch']} to "
            f"{same['model_replies_from_the_end']}. One pin, {pin['pin']}, synthetic: {strips}. {RP['reading']} {RP['claims_boundary']}")


def ladder_panel(x, y, w, h):
    ladder, _, _ = replay_path_numbers()
    a = [panel(x, y, w, h),
         text(x + 22, y + 30, "Five starts along the proven path", 16, GREEN, 700, max_w=w - 44),
         text(x + 22, y + 48, f"all {RP['dev_pins']} pins at each start · a bar is every step taken: replayed from the record, "
                              "or written by Model 1", 10.5, MUTED, max_w=w - 44)]
    lx, bx, bw = x + 22, x + 196, 392
    vx, fx = x + w - 252, x + w - 112
    top = y + 86
    a += [text(bx, top - 12, "replayed · no model reply", 10, BLUE, 700, max_w=180),
          text(bx + bw, top - 12, "written by Model 1", 10, PURPLE, 700, 'text-anchor="end"', 160),
          text(vx, top - 12, "verified, of 32", 10, GREEN, 700, max_w=126),
          text(fx, top - 12, "false alarms, of 28", 10, AMBER, 700, max_w=100)]
    scale = bw / max(r["replayed_calls"] + r["model_replies"] for r in ladder)
    for i, r in enumerate(ladder):
        ry = top + i * 32
        rw, mw = r["replayed_calls"] * scale, r["model_replies"] * scale
        end = r is ladder[-1]
        a.append(text(lx, ry + 14, cap(r["label"]), 12, FG, 700, max_w=bx - lx - 14))
        if rw:
            a += [f'<rect x="{bx}" y="{ry}" width="{rw:.1f}" height="20" rx="3" fill="#0e2733" stroke="{BLUE}"/>',
                  text(f"{bx + rw / 2:.1f}", ry + 14.5, r["replayed_calls"], 11, BLUE, 700, 'text-anchor="middle"')]
        a += [f'<rect x="{bx + rw:.1f}" y="{ry}" width="{mw:.1f}" height="20" rx="3" fill="{PURPLE}"/>',
              text(f"{bx + rw + mw / 2:.1f}", ry + 14.5, r["model_replies"], 11, BG, 700, 'text-anchor="middle"'),
              text(vx, ry + 15, r["verified_of_32"], 16 if end else 14, GREEN if end else FG, 700),
              f'<rect x="{vx + 30}" y="{ry + 5}" width="{88 * r["verified_of_32"] / 32:.1f}" height="10" rx="2" '
              f'fill="{GREEN if end else DIM}"/>',
              text(fx, ry + 15, r["false_alarms_of_28"], 14, AMBER, 700)]
    ty = top + len(ladder) * 32 + 8
    a.append(text(x + 22, ty, "Replies fall as more of the path is replayed; verified findings stay flat until the whole path, "
                              "deciding call included, is handed over.", 11, FG, 400, max_w=w - 44))
    require(ty + 10 <= y + h, f"ladder panel overflows ({ty + 10 - y} > {h})")
    return a


def claim_node(cx, cy, confirmed):
    color = GREEN if confirmed else AMBER
    mark = (f"M{cx - 4} {cy}L{cx - 1} {cy + 3.5}L{cx + 4.5} {cy - 3.5}" if confirmed
            else f"M{cx - 3.5} {cy - 3.5}L{cx + 3.5} {cy + 3.5}M{cx + 3.5} {cy - 3.5}L{cx - 3.5} {cy + 3.5}")
    return [f'<path d="M{cx} {cy - 12}L{cx + 12} {cy}L{cx} {cy + 12}L{cx - 12} {cy}Z" fill="{color}"/>',
            f'<path d="{mark}" stroke="{BG}" stroke-width="2.2" fill="none" stroke-linecap="round"/>']


def strip_row(nx, cy, step, strip):
    nodes = ["replayed"] * strip["replayed"] + list(strip["model_calls"]) + ["claim"]
    a = [f'<path d="M{nx} {cy}H{nx + (len(nodes) - 1) * step}" stroke="{DIM}" stroke-width="2"/>']
    for j, node in enumerate(nodes):
        cx = nx + j * step
        if node == "replayed":
            a.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{BG}" stroke="{BLUE}" stroke-width="2"/>')
        elif node == "claim":
            ok = strip["verifier"] == "CONFIRMED"
            a += claim_node(cx, cy, ok)
            a.append(text(cx + 22, cy + 4, f"claims {strip['claim']} · {'confirmed' if ok else 'not confirmed'}", 11.5,
                          GREEN if ok else AMBER, 700, max_w=230))
        else:
            a += [f'<circle cx="{cx}" cy="{cy}" r="9" fill="{PURPLE}"/>',
                  text(cx, cy + 3.5, node[0], 10, BG, 700, 'text-anchor="middle"')]
    return a


def pin_panel(x, y, w, h):
    ladder, _, pin = replay_path_numbers()
    labels = {r["start"]: r["label"] for r in ladder}
    a = [panel(x, y, w, h),
         text(x + 22, y + 30, f"One pin, five starts · {pin['pin']}, synthetic code", 16, BLUE, 700, max_w=w - 44),
         text(x + 22, y + 48, f"the planted answer is a finding · the proven path is {pin['proven_path_calls']} tool calls · "
                              "each mark is one step", 10.5, MUTED, max_w=w - 44)]
    lx, nx, step = x + 22, x + 196, 30
    top = y + 84
    for i, s in enumerate(pin["strips"]):
        cy = top + i * 34
        replies = len(s["model_calls"]) + 1
        a.append(text(lx, cy + 4, cap(labels[s["start"]]), 12, FG, 700, max_w=nx - lx - 14))
        a += strip_row(nx, cy, step, s)
        a.append(text(x + w - 22, cy + 4, f"{replies} model {'reply' if replies == 1 else 'replies'}", 11.5,
                      GREEN if replies == 1 else MUTED, 700 if replies == 1 else 400, 'text-anchor="end"'))
    ly = top + len(pin["strips"]) * 34 + 4
    lx2 = x + 30
    a += [f'<circle cx="{lx2}" cy="{ly - 4}" r="6" fill="{BG}" stroke="{BLUE}" stroke-width="2"/>',
          text(lx2 + 12, ly, "replayed: no model reply", 10, MUTED, max_w=140)]
    lx2 += 170
    a += [f'<circle cx="{lx2}" cy="{ly - 4}" r="6" fill="{PURPLE}"/>',
          text(lx2 + 12, ly, "Model 1's own call: r finds a function, c lists its callers", 10, MUTED, max_w=330)]
    lx2 += 360
    a += [f'<path d="M{lx2} {ly - 12}L{lx2 + 8} {ly - 4}L{lx2} {ly + 4}L{lx2 - 8} {ly - 4}Z" fill="{GREEN}"/>',
          text(lx2 + 14, ly, "Model 1's claim, judged by the verifier", 10, MUTED, max_w=240)]
    require(ly + 14 <= y + h, f"pin panel overflows ({ly + 14 - y} > {h})")
    return a


def replay_path_takeaways(x, y, w, h):
    ladder, same, _ = replay_path_numbers()
    partial = sorted({r["verified_of_32"] for r in ladder[:-1]})
    alarms = sorted(r["false_alarms_of_28"] for r in ladder)
    lines = [(GREEN, f"Free steps: replayed calls need no model reply. On {same['findings']} findings verified from every start, "
                     f"replies fell from {same['model_replies_from_scratch']} to {same['model_replies_from_the_end']}.", 400),
             (AMBER, f"Depth pays only at the decision: partial replays verified {partial[0]} to {partial[-1]} of 32; the whole path, "
                     f"deciding call included, {ladder[-1]['verified_of_32']}.", 400),
             (FG, f"Replay is exact, byte for byte at every start. It does not fix the decision: false alarms stayed at "
                  f"{alarms[0]} to {alarms[-1]} of 28.", 700)]
    a = [panel(x, y, w, h, fill="#0d1420", stroke=DIM)]
    for i, (color, line, weight) in enumerate(lines):
        require(len(line) * 12 * CHAR_W <= w - 60, f"takeaway line would shrink below 12px: {line!r}")
        a += [f'<circle cx="{x + 24}" cy="{y + 26 + i * 26}" r="4" fill="{color}"/>',
              text(x + 38, y + 30 + i * 26, line, 12, FG, weight, max_w=w - 60)]
    require(y + 30 + (len(lines) - 1) * 26 + 10 <= y + h, "takeaway panel overflows")
    return a


def replay_path_figure():
    replay_path_numbers()
    title = "Model 1's replay path: replay a proven path, then Model 1 takes over"
    a = start(WIDTH, 862, title, replay_path_description())
    hdr, _ = header("MODEL 1'S REPLAY PATH · MEASURED ON FIXTURES, NO QUANTUM-COMPUTER TIME", GREEN, "15 NOV 2026",
                    ["Replay a proven path, then Model 1 takes over"],
                    f"The depth ladder (T3 stage A) · one trained 9B · five starts on the teacher's proven path · {RP['dev_pins']} "
                    "synthetic pins")
    a += hdr
    a += ladder_panel(MARGIN, 128, CONTENT_W, 272)
    a += pin_panel(MARGIN, 416, CONTENT_W, 286)
    a += replay_path_takeaways(MARGIN, 718, CONTENT_W, 92)
    a += [f'<path d="M{MARGIN} 826H{WIDTH - MARGIN}" stroke="{LINE}"/>',
          text(MARGIN, 848, "Preregistered · the replayed path is the scripted teacher's, not Model 1's own · one model, one seed, "
                            "dev pins · synthetic code · no quantum advantage claimed", 11, MUTED, max_w=CONTENT_W)]
    return "\n".join(a + ["</svg>"])


OUTPUTS = {"model1-training-mission.svg": mission_figure, "model1-rsi-loop.svg": loop_figure,
           "model1-replay.svg": replay_figure, "model1-pl1.svg": pl1_figure, "model1-replay-path.svg": replay_path_figure}


def main(argv):
    check = "--check" in argv
    bad = 0
    for name, fn in OUTPUTS.items():
        svg = fn() + "\n"
        path = HERE / name
        if check:
            current = path.read_bytes().decode("utf-8").replace("\r\n", "\n") if path.exists() else None
            status = "OK" if current == svg else "DIFFERS"
            bad += status != "OK"
            print(f"{name}: {status}")
        else:
            path.write_bytes(svg.encode("utf-8"))
            print(f"wrote {name} ({len(svg)} bytes)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
