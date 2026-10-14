#!/usr/bin/env python3
"""Build crucible-lockpick.svg: the Crucible loop explained as a lockpick.

Standard library only. Draws the control structure of one Crucible depth
step: a master checkpoint (tension), a CFC fanout of small c/q chains (pins),
native checks (the click), JEV triage and master Q selection (choosing the
next pin), and the repair lane behind a HIT. It illustrates structure, not a
measurement. Run from the repository root:

    python3 docs/assets/build_crucible_lockpick.py
"""
from __future__ import annotations

from pathlib import Path

W, H = 1280, 1120
BG, EDGE, PANEL = "#070d17", "#2a3b51", "#0f1928"
INK, MUTED, QUIET = "#f2f6ff", "#adbbce", "#6f819a"
GREEN, PURPLE, CYAN, RED, AMBER = "#67dcb4", "#a78bfa", "#5fd1ff", "#ff7a7a", "#f5c26b"
FONT = "Helvetica,Arial,sans-serif"

out: list[str] = []


def t(x, y, s, size=16, fill=INK, weight=400, anchor="start", extra=""):
    out.append(
        f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'
    )


def box(x, y, w, h, stroke=EDGE, fill=PANEL, sw=1.5, rx=12, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def line(d, stroke=MUTED, sw=2, arrow=True, dash=""):
    m = ' marker-end="url(#arrow)"' if arrow else ""
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    out.append(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"{m}{ds}/>')


out.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
    'aria-labelledby="title description">'
)
out.append("<title id=\"title\">Crucible explained as a lockpick: hold tension, test pins, keep what sets</title>")
out.append(
    "<desc id=\"description\">One Crucible depth step. A master checkpoint holds the verified state like a tension "
    "wrench. It fans out into several small chains, each a candidate pin: an AI proposal, a native check on the "
    "software, and a quantum-method selection. Chains end in HIT or REJECT. JEV triage and the master Q selection "
    "choose the chain that advances. The winner's evidence and open obligations become the next checkpoint; a "
    "repair lane runs behind each HIT. Failed chains stay in the record. This figure shows control structure, "
    "not a measured result.</desc>")
out.append('<defs>'
           f'<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
           f'<path d="M0 0L10 5L0 10z" fill="{MUTED}"/></marker>'
           f'<marker id="arrow-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
           f'<path d="M0 0L10 5L0 10z" fill="{GREEN}"/></marker>'
           f'<marker id="arrow-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
           f'<path d="M0 0L10 5L0 10z" fill="{PURPLE}"/></marker>'
           '</defs>')
box(1, 1, W - 2, H - 2, stroke=EDGE, fill=BG, rx=18)

# ---- header -------------------------------------------------------------
t(48, 52, "CRUCIBLE, EXPLAINED AS A LOCKPICK", 19, GREEN, 700, extra='letter-spacing="1"')
t(48, 108, "Hold tension, test pins, keep what sets", 40, INK, 700)
t(48, 145, "One depth step of the C → Q → C loop. Every pin is tested by a native check; the loop, not a person, picks the pin that advances.", 20, MUTED)

# ---- left column: the analogy -------------------------------------------
LX, LY, LW = 48, 190, 352
box(LX, LY, LW, 640, rx=14)
t(LX + 24, LY + 40, "THE ANALOGY", 15, CYAN, 700, extra='letter-spacing="1"')
rows = [
    ("Tension wrench", "Master checkpoint C", "Holds everything already verified so it cannot slip while the next pin is tested."),
    ("Pins", "CFC chains", "Many small, cheap candidates fanned out from one checkpoint, each a c / check / q stack."),
    ("The click", "Native check", "The software itself says whether a pin set. No receipt, no click; the pin did not set."),
    ("A set pin", "HIT", "Banked with its evidence. A pin that drops is a REJECT and stays in the record."),
    ("Choosing the next pin", "JEV triage + master Q", "Which pin is binding now is chosen from verified chain energies and outcomes."),
    ("Working the set pin", "Repair lane", "Behind every HIT a fix is proposed and checked the same way as the loop deepens."),
]
y = LY + 76
for i, (lock, part, why) in enumerate(rows):
    accent = [CYAN, PURPLE, AMBER, GREEN, PURPLE, GREEN][i]
    out.append(f'<rect x="{LX + 24}" y="{y - 14}" width="4" height="78" rx="2" fill="{accent}"/>')
    t(LX + 42, y + 2, lock, 17, INK, 700)
    t(LX + 42, y + 24, part, 14, accent, 700)
    # wrap why text at ~44 chars
    words, lines_, cur = why.split(), [], ""
    for w_ in words:
        if len(cur) + len(w_) + 1 > 44:
            lines_.append(cur)
            cur = w_
        else:
            cur = (cur + " " + w_).strip()
    lines_.append(cur)
    for j, ln in enumerate(lines_[:2]):
        t(LX + 42, y + 44 + 17 * j, ln, 13, MUTED)
    y += 92

# ---- right column: the mechanism ----------------------------------------
RX, RW = 440, 792
CX = RX + RW // 2  # 836

# master checkpoint
box(CX - 230, 190, 460, 64, stroke=CYAN, sw=2)
t(CX, 219, "Master checkpoint  C", 20, INK, 700, "middle")
t(CX, 241, "signed evidence · verified passes · open obligations", 13, MUTED, 400, "middle")
line(f"M{CX} 254V294")

# fanout box
FX, FY, FW, FH = RX, 294, RW, 392
box(FX, FY, FW, FH, stroke=EDGE, fill="none", dash="8 6", rx=14)
t(FX + 20, FY + 30, "CFC FANOUT  ·  N chains per checkpoint, each a small c / q stack", 14, MUTED, 700)

chains = [
    ("pin 1", False), ("pin 2", False), ("pin 3", True), ("pin 4", False),
]
cw, gap = 168, 28
total = 4 * cw + 3 * gap
x0 = CX - total // 2
rowA, rowB, rowC, rowT = FY + 58, FY + 136, FY + 214, FY + 300
bh = 50
for i, (name, sel) in enumerate(chains):
    x = x0 + i * (cw + gap)
    cx = x + cw // 2
    stroke = PURPLE if sel else EDGE
    fill = "#1a1533" if sel else PANEL
    sw = 2.2 if sel else 1.5
    if sel:
        out.append(f'<rect x="{x - 10}" y="{rowA - 24}" width="{cw + 20}" height="{rowT - rowA + 24 + 62}" rx="14" fill="none" stroke="{PURPLE}" stroke-width="1.2" stroke-dasharray="4 4"/>')
        t(cx, rowA - 9, "selected chain", 12, PURPLE, 700, "middle")
    t(cx, rowA - 9 if not sel else rowA - 30, name, 12, QUIET if not sel else PURPLE, 700, "middle")
    box(x, rowA, cw, bh, stroke, fill, sw)
    t(cx, rowA + 22, "c · propose", 15, INK, 700, "middle")
    t(cx, rowA + 40, "AI candidate", 12, MUTED, 400, "middle")
    line(f"M{cx} {rowA + bh}V{rowB}", MUTED if not sel else PURPLE)
    box(x, rowB, cw, bh, AMBER if sel else stroke, fill, sw)
    t(cx, rowB + 22, "native check", 15, INK, 700, "middle")
    t(cx, rowB + 40, "the click: receipt or none", 12, MUTED, 400, "middle")
    line(f"M{cx} {rowB + bh}V{rowC}", MUTED if not sel else PURPLE)
    box(x, rowC, cw, bh, stroke, fill, sw)
    t(cx, rowC + 22, "q · set one pin", 15, INK, 700, "middle")
    t(cx, rowC + 40, "QUBO over receipted pins", 12, MUTED, 400, "middle")
    line(f"M{cx} {rowC + bh}V{rowT}", MUTED if not sel else PURPLE)
    hit = sel
    col = GREEN if hit else RED
    box(cx - 54, rowT, 108, 38, col, "#0f2a22" if hit else "#2a1216", 2, rx=10)
    t(cx, rowT + 25, "HIT" if hit else "REJECT", 16, col, 700, "middle")

t(FX + FW - 20, FY + FH - 14, "rejected pins stay in the record", 12, QUIET, 400, "end")

line(f"M{CX} {FY + FH}V{FY + FH + 36}", PURPLE)
line(f"M{CX} {FY + FH}V{FY + FH + 36}", PURPLE)  # emphasis

# JEV triage
JY = FY + FH + 36
box(RX, JY, RW, 56, stroke=EDGE, fill="#0c1522")
t(CX, JY + 24, "JEV triage  ·  advisory only", 16, INK, 700, "middle")
t(CX, JY + 43, "typed model called by the loop, receipt logged per run; may reorder chains, never terminate one", 12, MUTED, 400, "middle")
line(f"M{CX} {JY + 56}V{JY + 92}", PURPLE)

# master Q selection
QY = JY + 92
box(CX - 270, QY, 540, 68, stroke=PURPLE, fill="#1a1533", sw=2.2)
t(CX, QY + 28, "Master Q selection  ·  which pin is binding", 18, INK, 700, "middle")
t(CX, QY + 50, "lowest native-confirmed feasible energy wins; chosen from receipts, not from a reported outcome", 12, MUTED, 400, "middle")
line(f"M{CX} {QY + 68}V{QY + 104}", GREEN)

# next checkpoint + repair lane
NY = QY + 104
box(CX - 250, NY, 440, 64, stroke=CYAN, sw=2)
t(CX - 30, NY + 29, "Next checkpoint  C+1", 20, INK, 700, "middle")
t(CX - 30, NY + 51, "winner's evidence + open obligations · no verified pass is lost", 13, MUTED, 400, "middle")

RLX = CX + 222
box(RLX, NY - 2, 174, 68, stroke=GREEN, fill="#0f2a22", sw=2)
t(RLX + 87, NY + 26, "Repair lane", 17, INK, 700, "middle")
t(RLX + 87, NY + 46, "runs behind each HIT", 12, MUTED, 400, "middle")
out.append(f'<path d="M{CX + 190} {NY + 32}H{RLX}" fill="none" stroke="{GREEN}" stroke-width="2" marker-end="url(#arrow-green)"/>')

# loop arrow (left of mechanism)
loopx = RX - 16
out.append(
    f'<path d="M{CX - 250} {NY + 32}H{loopx}V222H{CX - 230}" fill="none" stroke="{GREEN}" stroke-width="2" '
    f'stroke-dasharray="6 5" marker-end="url(#arrow-green)"/>'
)
t(loopx - 9, (NY + 222) // 2, "next depth · loop until HIT + repair, or REJECT", 12, GREEN, 700, "middle",
  extra=f'transform="rotate(-90 {loopx - 9} {(NY + 222) // 2})"')

# ---- footer -------------------------------------------------------------
FOOT = H - 70
out.append(f'<path d="M48 {FOOT - 26}H{W - 48}" stroke="{EDGE}" stroke-width="1"/>')
t(48, FOOT, "Depth = how many dependent C → Q steps have run. Circuit depth is a different number inside one Q.", 13, MUTED)
t(48, FOOT + 22, "This figure shows the loop's control structure. It is not a measurement, a severity, or a claim of quantum advantage.", 13, QUIET)
t(W - 48, FOOT + 22, "Visual by Mythos 5.1 · Aether AI Predator · October 2026", 13, PURPLE, 700, "end")

out.append("</svg>")

Path("docs/assets/crucible-lockpick.svg").write_text("\n".join(out) + "\n", encoding="utf-8")
print("wrote docs/assets/crucible-lockpick.svg")
