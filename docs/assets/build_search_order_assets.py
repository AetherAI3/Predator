"""Build the search-order figure from the public JSON; no experiment calls.

Figure:
  search-order.svg   search by mechanism, not by position (P1 to P17; scripted test targets,
                     recorded Gen3 outcomes, one IBM hardware run)

Run from the repository root: python docs/assets/build_search_order_assets.py [--check]
--check rebuilds in memory and exits non-zero if the published SVG differs from the rebuild.
"""
import json
import sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE.parent / "research/search-order.json").read_text(encoding="utf-8"))
BG, FG, MUTED = "#070d17", "#f2f6ff", "#adbbce"
BLUE, PURPLE, GREEN, AMBER = "#32c7eb", "#b48aff", "#67dcb4", "#efc479"
DIM, DIM_TEXT, LINE = "#3b4f68", "#8696ad", "#293b53"
CHAR_W = 0.55
WIDTH, HEIGHT, MARGIN = 960, 748, 48
CONTENT_W = WIDTH - 2 * MARGIN


def require(condition, message):
    if not condition:
        raise ValueError(message)


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
            raise ValueError(f"text overflows {max_w}px at {size}px: {value!r}")
    return (f'<text x="{x}" y="{y}" font-family="Helvetica,Arial,sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" {extra}>{escape(value)}</text>')


def panel(x, y, w, h, fill="#101b2b", stroke="#293e57"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}"/>'


def numbers():
    rec, scan, ratio, hw = DATA["recorded_outcomes"], DATA["technique_scan_p15"], DATA["explore_ratio_p16_p17"], DATA["hardware_p7"]
    require(DATA["quantum_advantage_established"] is False, "wording assumes no quantum advantage")
    require(sum(m["checks"] for m in rec["by_mechanism"]) == rec["checks"], "mechanism checks must sum to the total")
    require(sum(m["hits"] for m in rec["by_mechanism"]) == rec["hits"], "mechanism hits must sum to the total")
    arms = scan["dev_round_targets_reached"]
    require(arms[0]["share"] == max(a["share"] for a in arms), "wording assumes the scan reaches the most targets")
    curve = ratio["dev_curve"]
    best = max(curve, key=lambda p: p["mechanisms_found"])
    require(best["explore"] == 90, "wording assumes the curve peaks at 90 percent exploring")
    return rec, scan, ratio, hw, best


def description():
    rec, scan, ratio, hw, best = numbers()
    mech = "; ".join(f"{m['mechanism']} {m['hits']} hits of {m['checks']}" for m in rec["by_mechanism"])
    arms = "; ".join(f"{a['arm']} {round(a['share'] * 200)} of 200" for a in scan["dev_round_targets_reached"])
    curve = "; ".join(f"{p['explore']} percent exploring {p['mechanisms_found']}" for p in ratio["dev_curve"])
    final = scan["final_gate"]
    p18 = rec["replay_p18"]["counted_mission"]
    return (f"{DATA['title']}. Lesson: {DATA['lesson']} Panel 1, recorded Gen3 outcomes, not blind: {rec['checks']} checks over "
            f"{rec['mechanisms']} anonymised mechanisms; the mechanism alone predicts {rec['predicted_by_mechanism']} of {rec['checks']}; "
            f"{mech}. Panel 2, scripted test targets, development round: targets reached, {arms}. On 200 fresh targets the scan reached "
            f"{round(final['scan'] * 200)} of 200 against {round(final['no_sweep'] * 200)} with no sweep, with {final['hits_ratio']:.1f} "
            f"times the hits. Panel 3, scripted: mechanisms found per target by share of turns spent exploring, {curve}; best at "
            f"{best['explore']} percent, and it held when the share of working variants changed. One IBM hardware run on "
            f"{hw['backend']}, where the hardware only carried the probes: narrowing found "
            f"{hw['good_candidates_per_billed_second_vs_random']['drive_length_7']:.1f} and "
            f"{hw['good_candidates_per_billed_second_vs_random']['drive_length_8']:.1f} times as many good candidates per billed "
            f"second as random order, {hw['billed_qpu_seconds']} billed seconds. A replay of recorded Gen3 missions (P18) then "
            f"favoured the rule: {p18['mechanism_first_found']} of {p18['mechanisms_with_a_hit']} mechanisms against "
            f"{p18['current_rule_found']} for Gen3's current next-test rule on the one counted mission; the win rests on one "
            f"mechanism. {DATA['claims_boundary']}")


def mechanism_panel(x, y, w, h):
    rec = DATA["recorded_outcomes"]
    a = [panel(x, y, w, h),
         text(x + 18, y + 28, "1 · What decides success", 15, GREEN, 700, max_w=w - 36),
         text(x + 18, y + 45, f"{rec['checks']} recorded Gen3 checks · {rec['mechanisms']} mechanisms", 10.5, MUTED, max_w=w - 36),
         text(x + 18, y + 84, f"{rec['predicted_by_mechanism']} of {rec['checks']}", 28, FG, 700, max_w=w - 36),
         text(x + 18, y + 102, "outcomes predicted by the mechanism alone", 10.5, MUTED, max_w=w - 36)]
    lx, bx = x + 18, x + 82
    scale = (w - 82 - 70) / max(m["checks"] for m in rec["by_mechanism"])
    ty = y + 132
    for m in rec["by_mechanism"]:
        name = m["mechanism"] if " to " not in m["mechanism"] else "11 others"
        a += [text(lx, ty + 9, name, 10.5, FG, 700, max_w=60),
              f'<rect x="{bx}" y="{ty}" width="{m["checks"] * scale:.1f}" height="11" rx="2" fill="#1d2b3e" stroke="{DIM}"/>']
        if m["hits"]:
            a.append(f'<rect x="{bx}" y="{ty}" width="{m["hits"] * scale:.1f}" height="11" rx="2" fill="{GREEN}"/>')
        a.append(text(f"{bx + m['checks'] * scale + 6:.1f}", ty + 9.5, f"{m['hits']} of {m['checks']}", 10, MUTED, max_w=64))
        ty += 22
    a += [f'<rect x="{lx}" y="{ty + 4}" width="10" height="9" rx="2" fill="{GREEN}"/>',
          text(lx + 15, ty + 12, "hits", 9.5, MUTED),
          f'<rect x="{lx + 46}" y="{ty + 4}" width="10" height="9" rx="2" fill="#1d2b3e" stroke="{DIM}"/>',
          text(lx + 61, ty + 12, "checks", 9.5, MUTED)]
    a += [text(x + 18, y + h - 50, f"Best 3 mechanisms: {round(rec['best_three_share_of_hits'] * 100)} % of the hits",
               11, FG, 700, max_w=w - 36),
          text(x + 18, y + h - 34, f"on {round(rec['best_three_share_of_checks'] * 100)} % of the checks", 11, FG, 700, max_w=w - 36),
          text(x + 18, y + h - 18, "recorded data, not blind · anonymised", 9.5, DIM_TEXT, max_w=w - 36)]
    require(ty + 14 <= y + h - 62, "mechanism panel overflows")
    return a


def scan_panel(x, y, w, h):
    scan = DATA["technique_scan_p15"]
    final = scan["final_gate"]
    a = [panel(x, y, w, h),
         text(x + 18, y + 28, "2 · Try every technique once", 15, BLUE, 700, max_w=w - 36),
         text(x + 18, y + 45, "targets reached of 200, development round", 10.5, MUTED, max_w=w - 36)]
    colors = [GREEN, MUTED, AMBER, AMBER, AMBER]
    labels = ["every technique once, then focus", "no sweep", "narrowing by position, 1 level",
              "narrowing by position, 2 levels", "narrowing by position, 3 levels"]
    bw = w - 36 - 44
    ty = y + 74
    for arm, color, label in zip(scan["dev_round_targets_reached"], colors, labels):
        n = round(arm["share"] * 200)
        a += [text(x + 18, ty, label, 10.5, FG, 700, max_w=w - 36),
              f'<rect x="{x + 18}" y="{ty + 6}" width="{bw * arm["share"]:.1f}" height="14" rx="3" fill="{color}"/>',
              text(f"{x + 18 + bw * arm['share'] + 6:.1f}", ty + 18, n, 12, color, 700)]
        ty += 46
    a += [text(x + 18, y + h - 50, f"Fresh targets: {round(final['scan'] * 200)} of 200, against", 11, FG, 700, max_w=w - 36),
          text(x + 18, y + h - 34, f"{round(final['no_sweep'] * 200)} with no sweep; {final['hits_ratio']:.1f} times the hits",
               11, FG, 700, max_w=w - 36),
          text(x + 18, y + h - 18, "scripted targets, at the old 15 % explore rate", 9.5, DIM_TEXT, max_w=w - 36)]
    require(ty <= y + h - 60, "scan panel overflows")
    return a


def ratio_panel(x, y, w, h):
    ratio = DATA["explore_ratio_p16_p17"]
    curve = sorted(ratio["dev_curve"], key=lambda p: p["explore"])
    final, robust = ratio["final_gate"], ratio["robustness_p17"]
    a = [panel(x, y, w, h),
         text(x + 18, y + 28, "3 · Explore 90 %, dig 10 %", 15, PURPLE, 700, max_w=w - 36),
         text(x + 18, y + 45, "mechanisms found per target", 10.5, MUTED, max_w=w - 36)]
    px, py, pw, ph = x + 46, y + 72, w - 46 - 20, 186
    lo, hi = 0.3, 0.7
    for v in (0.3, 0.4, 0.5, 0.6, 0.7):
        gy = py + ph - (v - lo) / (hi - lo) * ph
        a += [f'<path d="M{px} {gy:.1f}H{px + pw}" stroke="#1b2a3d"/>',
              text(px - 6, f"{gy + 3.5:.1f}", f"{v:.1f}", 9.5, DIM_TEXT, 400, 'text-anchor="end"')]
    pts = [(px + p["explore"] / 100 * pw, py + ph - (p["mechanisms_found"] - lo) / (hi - lo) * ph, p) for p in curve]
    a.append('<path d="' + " ".join(f"{'M' if i == 0 else 'L'}{cx:.1f} {cy:.1f}" for i, (cx, cy, _) in enumerate(pts)) +
             f'" stroke="{PURPLE}" stroke-width="2" fill="none"/>')
    for cx, cy, p in pts:
        best = p["explore"] == 90
        a.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{6 if best else 4}" fill="{GREEN if best else PURPLE}"/>')
        a.append(text(f"{cx:.1f}", py + ph + 16, p["explore"], 9.5, GREEN if best else DIM_TEXT, 700 if best else 400,
                      'text-anchor="middle"'))
        if best:
            a.append(text(f"{cx - 8:.1f}", f"{cy - 12:.1f}", f"{p['mechanisms_found']:.3f}", 11, GREEN, 700, 'text-anchor="end"'))
    a += [text(px + pw / 2, py + ph + 30, "percent of turns spent exploring", 9.5, DIM_TEXT, 400, 'text-anchor="middle"'),
          text(x + 18, y + h - 50, f"Fresh targets: {final['pick_mechanisms_found']:.3f} against {final['pure_explore']:.3f}",
               11, FG, 700, max_w=w - 36),
          text(x + 18, y + h - 34, f"(all explore) and {final['pure_dig']:.3f} (all dig)", 11, FG, 700, max_w=w - 36),
          text(x + 18, y + h - 18, f"worst loss {robust['worst_regret_of_0_90']} as the working share moved", 9.5,
               DIM_TEXT, max_w=w - 36)]
    return a


def takeaways(x, y, w, h):
    hw = DATA["hardware_p7"]
    ratio = hw["good_candidates_per_billed_second_vs_random"]
    p18 = DATA["recorded_outcomes"]["replay_p18"]["counted_mission"]
    lines = [(GREEN, "Lesson: organise search by mechanism, not by position. Recorded outcomes point this way; the scripted tests "
                     "measure its value.", 400),
             (BLUE, "Now the Gen2 swarm's default, on a draft (not main): every technique once (P15), then explore 90 % (P16); "
                    "settings revert.", 400),
             (AMBER, f"IBM hardware only carried the probes ({hw['backend']}, one run): narrowing got {ratio['drive_length_7']:.1f} "
                     f"to {ratio['drive_length_8']:.1f} times random's finds per billed second.", 400),
             (PURPLE, f"P18, replaying recorded Gen3 missions: {p18['mechanism_first_found']} of {p18['mechanisms_with_a_hit']} "
                      f"mechanisms against {p18['current_rule_found']} for Gen3's current rule; the win rests on one.", 400),
             (FG, "Gen2 work: scripted targets, no real target, nothing replayed or trained into Model 1.", 700)]
    a = [panel(x, y, w, h, fill="#0d1420", stroke=DIM)]
    for i, (color, line, weight) in enumerate(lines):
        require(len(line) * 11.5 * CHAR_W <= w - 60, f"takeaway line would shrink below 11.5px: {line!r}")
        a += [f'<circle cx="{x + 24}" cy="{y + 24 + i * 25}" r="4" fill="{color}"/>',
              text(x + 38, y + 28 + i * 25, line, 11.5, FG, weight, max_w=w - 60)]
    require(y + 28 + (len(lines) - 1) * 25 + 12 <= y + h, "takeaway panel overflows")
    return a


def figure():
    numbers()
    title = "Search order: organise search by mechanism, not by position"
    a = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" '
         'role="img" aria-labelledby="title description">',
         f'<title id="title">{escape(title)}</title><desc id="description">{escape(description())}</desc>',
         f'<rect x="1" y="1" width="{WIDTH - 2}" height="{HEIGHT - 2}" rx="18" fill="{BG}" stroke="#2a3b51"/>',
         text(MARGIN, 40, "SEARCH ORDER · STEPS P1 TO P18 · SCRIPTED TARGETS UNLESS MARKED", 15, BLUE, 700,
              max_w=CONTENT_W - 150),
         text(WIDTH - MARGIN, 40, "9–17 NOV 2026", 15, MUTED, 700, 'text-anchor="end"'),
         text(MARGIN, 82, "Search by mechanism, not by position", 30, FG, 700, max_w=CONTENT_W),
         text(MARGIN, 108, "What decides success · how to reach every target · how much to dig", 14, MUTED, max_w=CONTENT_W)]
    pw, gap, py, ph = 276, 18, 128, 404
    a += mechanism_panel(MARGIN, py, pw, ph)
    a += scan_panel(MARGIN + pw + gap, py, pw, ph)
    a += ratio_panel(MARGIN + 2 * (pw + gap), py, pw, ph)
    a += takeaways(MARGIN, 548, CONTENT_W, 141)
    a += [f'<path d="M{MARGIN} 706H{WIDTH - MARGIN}" stroke="{LINE}"/>',
          text(MARGIN, 728,"Preregistered steps · recorded outcomes anonymised · the original sweep method stays private · "
                            "no quantum advantage claimed", 11, MUTED, max_w=CONTENT_W)]
    return "\n".join(a + ["</svg>"])


OUTPUTS = {"search-order.svg": figure}


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
