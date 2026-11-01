"""Build the Quantum Comm Ops hardware-ladder SVG from the approved public JSON; no experiment calls."""
import json
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE.parent / "research/quantum-comm-ops.json").read_text(encoding="utf-8"))
HW = DATA["hardware_missions"]
BG, FG, MUTED = "#070d17", "#f2f6ff", "#adbbce"
BLUE, PURPLE, GREEN, AMBER = "#32c7eb", "#b48aff", "#67dcb4", "#efc479"


def text(x, y, value, size=20, color=FG, weight=400, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="Helvetica,Arial,sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" {extra}>{escape(str(value))}</text>')


def start(width, height, title, description):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
            f'role="img" aria-labelledby="title description">',
            f'<title id="title">{escape(title)}</title><desc id="description">{escape(description)}</desc>',
            f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="18" fill="{BG}" stroke="#2a3b51"/>']


def panel(x, y, width, height, fill="#101b2b", stroke="#293e57", radius=12):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'


def ladder_rows():
    by = {}
    for row in HW["ladder"]:
        by.setdefault(row["mission"], []).append(row)
    j5, j6, j7 = by["J5"][0], by["J6-base"][0], by["J7-s5"][0]
    j8, j9, j11 = by["J8"], by["J9"][0], by["J11-R"][0]
    return [
        ("J5 · Oct 31", j5["device"], f'{j5["provider_jobs"]} jobs · {j5["shots_per_circuit"]} shots', j5["billed_qpu_seconds"],
         f'{j5["first_pass_verified"]}/400 first pass', BLUE),
        ("J6 · Oct 31", j6["device"], f'{j6["provider_jobs"]} jobs · {j6["shots_per_circuit"]} shots', j6["billed_qpu_seconds"],
         f'{j6["first_pass_verified"]}/400 first pass · gate not met', AMBER),
        ("J7 · Oct 31", j7["device"], f'{j7["provider_jobs"]} job · {j7["shots_per_circuit"]} shots', j7["billed_qpu_seconds"],
         f'{j7["first_pass_verified"]}/400 first pass', GREEN),
        ("J8 · Oct 31", j8[0]["device"], "1 job each · 2 more datasets", j8[0]["billed_qpu_seconds"],
         f'{j8[0]["first_pass_verified"]}/400 and {j8[1]["first_pass_verified"]}/400', GREEN),
        ("J9 · Oct 31", j9["device"], "1 job · secret tag key", j9["billed_qpu_seconds"],
         f'{j9["first_pass_verified"]}/400 · 0/400 under public key', GREEN),
        ("J11 · Nov 1", j11["device"], "1 job · 2nd device · new secret", j11["billed_qpu_seconds"],
         f'{j11["first_pass_verified"]}/400 first pass', GREEN),
    ]


def hardware_ladder():
    rows = ladder_rows()
    totals = HW["one_job_five_shot_totals"]
    control = HW["cost_comparison"]["matched_packing_control"]
    packed = control["packed_job_billed_seconds"][0]
    separate = sum(control["separate_jobs_billed_seconds"][0])
    description = (f"Billed IBM QPU seconds for the same 400-recipient delivery mission. {rows[0][0]} on {rows[0][1]}: "
                   f"{rows[0][3]:g} seconds in {rows[0][2]}, {rows[0][4]}. {rows[1][0]} on {rows[1][1]}: {rows[1][3]:g} seconds, {rows[1][4]}. "
                   f"{rows[2][0]} on {rows[2][1]}: {rows[2][3]:g} seconds in one job, {rows[2][4]}; repeated at {rows[3][3]:g} seconds "
                   f"on two more datasets, with a secret key, and on {rows[5][1]} on November 1, each 400 of 400. "
                   f"Across the five one-job missions: {totals['first_pass_verified']} of {totals['recipient_deliveries']} first pass, "
                   f"{totals['majority_bit_errors']} majority bit errors in {totals['raw_bit_shots']:,} raw bit-shots. Inset: three circuits "
                   f"compiled once bill {packed:g} seconds as one job and {separate:g} seconds as three jobs on ibm_fez. The saving is provider "
                   "accounting for batched circuits; no quantum advantage is established.")
    a = start(1280, 760, "Quantum Comm Ops on IBM hardware: the same mission, from 81 jobs to one", description)
    a += [text(48, 48, "IBM HARDWARE / 400-RECIPIENT DELIVERY MISSION", 17, GREEN, 700),
          text(1232, 48, "31 OCT – 1 NOV 2026", 17, MUTED, 700, 'text-anchor="end"'),
          text(48, 112, "Same mission. 162 s → 5 s of billed QPU.", 44, FG, 700),
          text(48, 152, "1,200 circuits per mission · billed seconds as reported by the provider · "
               "different devices, shot counts and days · linear scale", 19, MUTED)]
    top, row_h, bar_x, bar_w, max_s = 190, 62, 560, 560, 162.0
    for i, (label, device, config, seconds, result, color) in enumerate(rows):
        y = top + i * row_h
        width = max(seconds / max_s * bar_w, 8)
        a += [text(48, y + 26, label, 21, FG, 700), text(48, y + 48, f"{device} · {config} · {result}", 15, MUTED),
              f'<rect x="{bar_x}" y="{y + 8}" width="{width:.3f}" height="30" rx="5" fill="{color}"/>',
              text(bar_x + width + 14, y + 31, f"{seconds:g} s", 22, FG, 700)]
    a += ['<path d="M48 572H1232" stroke="#293b53"/>',
          panel(48, 590, 560, 130),
          text(70, 622, "Matched packing control · ibm_fez · 3 circuits compiled once", 17, GREEN, 700),
          text(70, 660, f"{packed:g} s", 36, GREEN, 700), text(150, 660, "as one packed job", 19, FG),
          text(360, 660, f"{separate:g} s", 36, BLUE, 700), text(440, 660, "as three jobs", 19, FG),
          text(70, 700, "Both orders (J11); fresh circuits (J0). Three circuits only.", 15, MUTED),
          panel(632, 590, 600, 130),
          text(654, 622, "Five one-job missions, five shots", 17, GREEN, 700),
          text(654, 660, f"{totals['first_pass_verified']:,} / {totals['recipient_deliveries']:,}", 36, FG, 700),
          text(910, 660, "recipients verified first pass", 19, FG),
          text(654, 692, f"{totals['majority_bit_errors']} majority bit errors in {totals['raw_bit_shots']:,} raw bit-shots", 15, MUTED),
          text(654, 712, "raw error 0.41–0.52% per bit before the five-shot majority", 15, MUTED),
          text(48, 745, "Saving = IBM accounting for batched circuits · known classical frames · scripted recipients · "
               "no quantum advantage established", 15, MUTED)]
    return "\n".join(a + ["</svg>"])


if __name__ == "__main__":
    out = HERE / "quantum-comm-ops-hardware-ladder.svg"
    out.write_text(hardware_ladder() + "\n", encoding="utf-8")
    print(out.name, out.stat().st_size, "bytes")
