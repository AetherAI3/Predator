"""Validate the public export and rebuild GEN3 figures. No experiment calls.

Python 3.11+; matplotlib 3.10.8. --check validates without writing figures.
--preview-dir PATH also writes PNGs for visual review (outside the repository).
"""
import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "research/gen3-qpack-experiment1.json"
ORDER = ["AI_Q_d1", "AI_Q_d2", "AI_C_d1", "AI_C_d2", "FIXED_Q_d1", "FIXED_Q_d2"]
LABELS = ["AI + Q / d1", "PREDATOR / d2", "AI + C / d1", "AI + C / d2", "Fixed Q / d1", "Fixed Q / d2"]
BG, FG, MUTED = "#070d17", "#f2f6ff", "#adbbce"
GREEN, BLUE, PURPLE, AMBER, ZERO = "#67dcb4", "#32c7eb", "#b48aff", "#efc479", "#25374e"


def require(value, message):
    if not value:
        raise ValueError(message)


def validate(d):
    require(d["schema"] == "predator.public-gen3-qpack-experiment1.v1", "schema")
    es, rows = d["episodes"], {r["variant"]: r for r in d["rows"]}
    require(len(es) == 96 and len({e["id"] for e in es}) == 96, "96 unique episodes")
    require(set(rows) == set(ORDER), "six variants")
    require(len({(e["pair"], e["condition"], e["variant"]) for e in es}) == 96, "unique cells")
    require(Counter(e["condition"] for e in es) == {"controlled_fault": 48, "pristine_control": 48}, "conditions")
    for variant, r in rows.items():
        group = [e for e in es if e["variant"] == variant]
        faults = [e for e in group if e["condition"] == "controlled_fault"]
        require(len(group) == r["scheduled_episodes"] == 16 and len(faults) == 8, variant + " schedule")
        for field, outcome in [("positive_findings", "verified_finding"), ("stage_1_findings", "stage_1_finding"), ("new_at_stage_2", "new_at_stage_2")]:
            require(sum(e["outcome"][outcome] for e in faults) == r[field], variant + " " + field)
        missing = sum(e["outcome"]["missing"] for e in group)
        require(missing == r["operational_missing"], variant + " missing")
        require(r["complete_coverage"] == (missing == 0), variant + " completeness")
        require(r["complete_fault_rate"] == (r["positive_findings"] / 8 if missing == 0 else None), variant + " rate")
        require(sum(e["failure_category"] == "observed_method_failure" for e in group) == r["observed_method_failures"], variant + " failures")
        require(sum(len(e["stages"]) for e in group) == r["recorded_selection_stages"], variant + " stages")
        controls = Counter(e["control_status"] for e in group if e["condition"] == "pristine_control")
        for status in ("confirmed", "refuted", "unsupported", "inconsistent"):
            require(controls[status] == r["pristine_claims"][status], variant + " control " + status)
    for e in es:
        o = e["outcome"]
        require(o["observed"] != o["missing"], "observed/missing")
        checks = {c["stage"]: c for c in e["checks"]}
        stages = {s["stage"]: s for s in e["stages"]}
        require(len(checks) == len(e["checks"]) and len(stages) == len(e["stages"]), "duplicate stage")
        # Partial operational records can retain a selection without its native check.
        for stage, c in checks.items():
            require(stage in stages, "check references absent selection")
            require(c["selected_semantic_trace_digest"] == stages[stage]["selected_semantic_trace_digest"], "trace binding")
        require(o["verified_finding"] == any(c["status"] == "VERIFIED_FINDING" for c in checks.values()), "native finding binding")
        require(o["stage_1_finding"] == (checks.get(1, {}).get("status") == "VERIFIED_FINDING"), "stage-one binding")
        require(o["new_at_stage_2"] == (not o["stage_1_finding"] and checks.get(2, {}).get("status") == "VERIFIED_FINDING"), "stage-two binding")
    pairs = d["paired_fault_outcomes"]
    require([p["pair"] for p in pairs] == [f"P{i:02}" for i in range(1, 9)], "pair inventory")
    for p in pairs:
        for variant in ORDER:
            e = next(e for e in es if (e["pair"], e["condition"], e["variant"]) == (p["pair"], "controlled_fault", variant))
            expected = None if e["outcome"]["missing"] else int(e["outcome"]["verified_finding"])
            require(p["outcomes"][variant] == expected and p["stratum"] == e["stratum"], "paired outcome")
    paired = Counter((p["outcomes"]["AI_Q_d1"], p["outcomes"]["AI_Q_d2"]) for p in pairs)
    require(d["paired_ai_q_d2_vs_d1"] == dict(gained=paired[0, 1], lost=paired[1, 0], both_find=paired[1, 1], neither_finds=paired[0, 0]), "paired contrast")
    contrasts = d["contrasts_percentage_points"]
    require(contrasts["R_Q"] == 100 * (rows["AI_Q_d2"]["complete_fault_rate"] - rows["AI_Q_d1"]["complete_fault_rate"]) == 37.5, "R_Q")
    require(contrasts["A_DEV"] == 100 * (rows["AI_Q_d2"]["complete_fault_rate"] - rows["FIXED_Q_d2"]["complete_fault_rate"]) == 62.5, "A_DEV")
    require(all(contrasts[k] is None for k in ("R_C", "D_DEV", "I_DEV")), "unavailable contrasts")
    require(d["descriptive_ai_q_rate_ratio"] == 5 / 2, "descriptive ratio")
    require(sum(e["outcome"]["missing"] for e in es) == 3 and sum(e["outcome"]["observed"] for e in es) == 93, "coverage")
    require(sum(r["observed_method_failures"] for r in rows.values()) == 2, "method failures")
    require(sum(c["status"] == "INCONSISTENT" for e in es for c in e["checks"]) == 4, "preserved inconsistent checks")
    require(sum(r["pristine_claims"]["unsupported"] for r in rows.values()) == 1, "unsupported control")
    require(sum(r["pristine_claims"]["confirmed"] for r in rows.values()) == 0, "confirmed controls")
    a = d["accounting"]
    require(a["aggregate_known_actual_charge_usd"] <= a["aggregate_fail_closed_charge_exposure_usd"] <= a["aggregate_charge_ceiling_usd"], "cost scope")
    require(a["client_native_commits"] + a["client_native_uncommitted"] == a["client_native_reservations_consumed"], "native ledger")

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if (k.endswith("digest") or k.endswith("sha256")) and v is not None:
                    require(isinstance(v, str) and re.fullmatch(r"[0-9a-f]{64}", v), "digest format: " + k)
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
        elif isinstance(x, float):
            require(math.isfinite(x), "non-finite value")
    walk(d)
    return rows


def figures(d, preview_dir=None):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch, Rectangle
    matplotlib.rcParams.update({"font.family": "DejaVu Sans", "text.color": FG, "axes.facecolor": BG,
        "figure.facecolor": BG, "svg.fonttype": "none", "svg.hashsalt": "predator-gen3-qpack-v1", "font.size": 12})
    rows = {r["variant"]: r for r in d["rows"]}

    def canvas(title, subtitle, height=7.7):
        fig = plt.figure(figsize=(13.2, height))
        ax = fig.add_axes([0, 0, 1, 1]); ax.set(xlim=(0, 1), ylim=(0, 1)); ax.axis("off")
        ax.text(.045, .94, "AETHER AI  /  PREDATOR GEN3  /  EXPERIMENT #1", color=BLUE, fontsize=11, weight="bold")
        ax.text(.045, .875, title, fontsize=25, weight="bold")
        ax.text(.045, .827, subtitle, fontsize=12, color=MUTED)
        return fig, ax

    def save(fig, name, desc):
        fig.savefig(HERE / (name + ".svg"), metadata={"Date": None, "Creator": "Predator public figure builder", "Title": name, "Description": desc})
        if preview_dir:
            preview_dir.mkdir(parents=True, exist_ok=True)
            fig.savefig(preview_dir / (name + ".png"), dpi=110)
        plt.close(fig)

    fig, ax = canvas("Feedback: 2/8 → 5/8 controlled faults found", "+37.5 percentage points vs AI_Q d1 · One exploratory DEV campaign · Aer MPS simulation")
    for i, variant in enumerate(ORDER):
        r, y = rows[variant], .72 - i * .093
        missing = sum(p["outcomes"][variant] is None for p in d["paired_fault_outcomes"])
        color = PURPLE if variant == "AI_Q_d2" else GREEN
        ax.text(.045, y + .016, LABELS[i], weight="bold", color=color if variant == "AI_Q_d2" else FG)
        # These tiles are counts, not individual pair identities; the paired figure supplies identities.
        for j in range(8):
            fill = color if j < r["positive_findings"] else AMBER if j >= 8 - missing else ZERO
            ax.add_patch(Rectangle((.27 + j * .043, y), .034, .042, color=fill))
            if j >= 8 - missing:
                ax.text(.287 + j * .043, y + .021, "?", color=BG, ha="center", va="center", weight="bold")
        rate = f'{r["complete_fault_rate"]:.1%}' if r["complete_coverage"] else "INCOMPLETE"
        ax.text(.645, y + .016, f'{r["positive_findings"]}/8', weight="bold", fontsize=16)
        ax.text(.73, y + .016, rate, color=AMBER if missing else MUTED, fontsize=12)
        if missing:
            ax.text(.89, y + .016, f"{missing} missing", color=AMBER, fontsize=10)
    ax.text(.045, .17, "Filled = found   ·   Dark = observed, no finding   ·   ? = missing   ·   Tiles show aggregate counts", color=MUTED, fontsize=11)
    ax.text(.045, .115, "Classical feedback comparison remains unset. No established quantum advantage or new CVE.", color=AMBER, fontsize=11)
    ax.text(.045, .062, "Controls: 47 refuted, 1 unsupported, 0 confirmed findings. Counts are fault instances, not vulnerabilities.", color=MUTED, fontsize=10)
    save(fig, "gen3-qpack-findings", "Six rows over eight controlled faults. AI_Q d1 2, Predator d2 5, AI_C d1 2, AI_C d2 3 with one missing, fixed Q d1 zero with two missing, fixed Q d2 zero. Two rows incomplete; no cross-arm superiority established.")

    fig, ax = canvas("The paired outcomes include a regression", "AI_Q d2 vs d1: 4 gained · 1 lost · 1 found by both · 2 found by neither", 8.2)
    xs = [.24 + i * .115 for i in range(6)]
    for x, label in zip(xs, LABELS):
        ax.text(x + .04, .763, label.replace(" / ", "\n"), ha="center", va="center", fontsize=10, weight="bold")
    for i, p in enumerate(d["paired_fault_outcomes"]):
        y = .68 - i * .063
        ax.text(.045, y + .023, f'{p["pair"]}  /  {p["stratum"]}', va="center", fontsize=12)
        for x, variant in zip(xs, ORDER):
            v = p["outcomes"][variant]
            color = AMBER if v is None else PURPLE if v and variant == "AI_Q_d2" else GREEN if v else ZERO
            ax.add_patch(Rectangle((x, y), .08, .044, color=color))
            ax.text(x + .04, y + .022, "?" if v is None else str(v), ha="center", va="center", color=BG if v or v is None else MUTED, weight="bold")
    ax.text(.045, .178, "1 = native-verified finding   ·   0 = observed, no finding   ·   ? = operationally missing", color=MUTED, fontsize=11)
    ax.text(.045, .115, "Eight matched controlled-fault instances, not eight CVEs. Same pair identity is used in every column.", color=MUTED, fontsize=10)
    ax.text(.045, .066, "Previously exposed DEV mechanisms · Seed 1103 · Incomplete cells remain missing", color=AMBER, fontsize=11)
    save(fig, "gen3-qpack-paired-outcomes", "Eight by six paired outcome matrix. Predator feedback gains four cases but loses P04 versus no feedback. Missing cells are P04 fixed Q d1 and P08 classical d2 and fixed Q d1.")

    fig, ax = canvas("The ratchet, as recorded", "Predator AI_Q d2 · Two real trajectories · Fingerprints link to the public episode export", 8.8)
    def box(x, y, w, h, title, detail, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012", facecolor="#101b2b", edgecolor=color, linewidth=1.2))
        ax.text(x + .014, y + h - .038, title, fontsize=12, weight="bold", color=color)
        ax.text(x + .014, y + h - .075, detail, fontsize=10, linespacing=1.65, va="top")
    for eid, y, caption in [("E002", .48, "P01 / S1 · A new verified finding at stage two"), ("E095", .19, "P08 / S4 · Stage-one evidence survives a refuted second candidate")]:
        e = next(e for e in d["episodes"] if e["id"] == eid)
        ax.text(.045, y + .25, eid + "  /  " + caption, fontsize=12, weight="bold")
        for j, s in enumerate(e["stages"]):
            c = next(c for c in e["checks"] if c["stage"] == s["stage"])
            x = .045 if j == 0 else .58
            status = "VERIFIED FINDING" if c["status"] == "VERIFIED_FINDING" else c["status"]
            box(x, y, .37, .21, f'STAGE {j + 1} / {status}', f'AI formulation → QAOA/MPS → native check\nFormulation {s["compilation_digest"][:12]}…\nNative receipt {c["native_receipt_sha256"][:12]}…\nLocal objective energy: {s["selected_energy"]}', GREEN if c["status"] == "VERIFIED_FINDING" else MUTED)
        ax.annotate("", xy=(.56, y + .1), xytext=(.44, y + .1), arrowprops={"arrowstyle": "->", "color": PURPLE, "lw": 2})
        ax.text(.50, y + .15, "Native feedback\nAI reformulates", ha="center", va="center", fontsize=10, color=PURPLE)
    ax.text(.045, .095, "Each stage has its own objective: these energies do not measure convergence on a shared landscape.", color=AMBER, fontsize=10)
    ax.text(.045, .045, "Evidence graph, not a superposition image. MPS simulation; selector contribution is not isolated by this study.", color=MUTED, fontsize=10)
    save(fig, "gen3-qpack-ratchet", "Two actual trajectories: E002 refuted then verified, E095 verified then refuted with first-stage finding retained. AI reformulation uses native feedback. Stage energies belong to distinct formulations.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--preview-dir", type=Path)
    args = parser.parse_args()
    data = json.loads(DATA.read_text(encoding="utf-8"), parse_constant=lambda v: (_ for _ in ()).throw(ValueError(v)))
    validate(data)
    if not args.check:
        figures(data, args.preview_dir)
    print("Validated 96 episodes, six rows, eight paired outcomes, native bindings, missingness and accounting." + (" Built three SVGs." if not args.check else ""))
