"""Render public aggregate charts; does not execute circuits or call services."""

import argparse
import json
import math
from html import escape
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


HERE = Path(__file__).resolve().parent
BG, FG, MUTED = "#070d17", "#f2f6ff", "#adbbce"
BLUE, PURPLE, GRID = "#32c7eb", "#b48aff", "#2a3b51"


def style_axis(axis):
    axis.set_facecolor(BG)
    axis.set_axisbelow(True)
    axis.grid(axis="x", color=GRID, linewidth=0.7)
    axis.tick_params(axis="both", colors=FG, labelsize=13, length=0, pad=8)
    for name, spine in axis.spines.items():
        spine.set_visible(name == "bottom")
        spine.set_color(GRID)
    axis.xaxis.label.set_color(FG)
    axis.yaxis.label.set_color(FG)


def build(preview_dir=None):
    data = json.loads((HERE.parent / "research/search-scaling.json").read_text(encoding="utf-8"))
    if data["schema"] != "predator.public-search-scaling.v1":
        raise ValueError("Unexpected aggregate schema")
    rows = {row["candidates"]: row for row in data["rows"]}
    if len(rows) != len(data["rows"]):
        raise ValueError("Duplicate candidate count")
    quality = [rows[n] for n in data["figure"]["quality_candidates"]]
    compilation = [rows[n] for n in data["figure"]["compilation_candidates"]]
    for row in quality:
        gap = row["best_sample_gap_percent"]
        if gap is None or not 0 <= gap[0] <= gap[1] or row["seeds"] != 3:
            raise ValueError("Quality chart needs reported three-seed score ranges")
    if any(row["ordinary_native_2q_mean"] <= 0 for row in compilation):
        raise ValueError("Instruction comparison needs positive baseline counts")

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 12,
        "svg.fonttype": "none",
        "svg.hashsalt": "predator-search-scaling-2026-10-20",
        "axes.unicode_minus": True,
    })
    fig = plt.figure(figsize=(10.8, 8.6), facecolor=BG)
    fig.text(0.06, 0.958, "AETHER AI / PREDATOR RESEARCH", color=BLUE, fontsize=10.5, weight="bold")
    fig.text(0.06, 0.908, "Answer quality and circuit size.", color=FG, fontsize=22, weight="bold")
    fig.text(0.06, 0.871, "October 20, 2026 · Synthetic simulation and compilation tests", color=MUTED, fontsize=11.5)

    quality_axis = fig.add_axes([0.15, 0.55, 0.70, 0.23])
    style_axis(quality_axis)
    quality_axis.set_title("1. How far did the sampled answers miss the best score?", loc="left", color=FG, fontsize=13.5, pad=17, weight="bold")
    quality_axis.axvline(0, color=MUTED, linewidth=0.8)
    for index, row in enumerate(quality):
        low, high = row["best_sample_gap_percent"]
        quality_axis.plot([low, high], [index, index], color=BLUE, linewidth=5, solid_capstyle="round")
        quality_axis.scatter([low, high], [index, index], color=BLUE, s=34, zorder=3)
        quality_axis.text(high + 2, index, f"{low}–{high}%", color=FG, fontsize=13.5, va="center")
    quality_max = math.ceil(max(row["best_sample_gap_percent"][1] for row in quality) * 1.18 / 10) * 10
    quality_axis.set_xlim(-4, quality_max)
    quality_axis.set_ylim(len(quality) - 0.5, -0.5)
    quality_axis.set_yticks(range(len(quality)), [str(row["candidates"]) for row in quality])
    quality_axis.set_xticks([0, 20, 40, 60, 80])
    quality_axis.set_ylabel("Candidate actions", fontsize=12, labelpad=13)
    quality_axis.set_xlabel("Gap from best score (%) · 0% is best", fontsize=12, labelpad=11)
    fig.text(0.15, 0.465, "Untuned one-layer circuit · 4,096 samples per run · Observed ranges across 3 seeds", color=MUTED, fontsize=9.5)

    compilation_axis = fig.add_axes([0.15, 0.15, 0.70, 0.23])
    style_axis(compilation_axis)
    compilation_axis.set_title("2. Does joint5 reduce hardware instructions?", loc="left", color=FG, fontsize=13.5, pad=17, weight="bold")
    changes = [100 * (row["joint5_native_2q_mean"] - row["ordinary_native_2q_mean"]) / row["ordinary_native_2q_mean"] for row in compilation]
    compilation_axis.axvline(0, color=MUTED, linewidth=0.8)
    compilation_axis.barh(range(len(compilation)), changes, height=0.20, color=PURPLE)
    for index, value in enumerate(changes):
        label = f"{abs(value):.0f}% {'fewer' if value < 0 else 'more'}"
        compilation_axis.text(value / 2, index - 0.25, label, color=FG, fontsize=13.5, ha="center", va="center")
    extent = math.ceil(max(abs(value) for value in changes) * 1.6 / 5) * 5
    compilation_axis.set_xlim(-extent, extent)
    compilation_axis.set_ylim(len(compilation) - 0.5, -0.8)
    compilation_axis.set_yticks(range(len(compilation)), [str(row["candidates"]) for row in compilation])
    compilation_axis.set_xticks([-20, -10, 0, 10, 20], ["−20", "−10", "0", "+10", "+20"])
    compilation_axis.set_ylabel("Candidate actions", fontsize=12, labelpad=13)
    compilation_axis.set_xlabel("Change in routed two-qubit instructions (%)", fontsize=12, labelpad=11)
    fig.text(0.15, 0.064, "Changes from rounded mean counts · 12/16 choices: 3 seeds · 32: 2 seeds · 40: 1 seed", color=MUTED, fontsize=9.5)
    fig.text(0.06, 0.021, "Reported synthetic tests · Selected sizes · No quantum advantage established", color=MUTED, fontsize=10.5)

    title = "Predator synthetic search quality and joint5 instruction counts"
    description = (
        "Reported October 20, 2026 synthetic simulator and compilation tests, separate from the IBM Fez hardware pilot. "
        "The untuned circuit used one layer and 4,096 samples per run. Reported best-sample score gaps across three "
        "seeds: 6 candidates 0 to 11 percent, 8 candidates 6 to 15 percent, 16 candidates 28 to 41 percent, and "
        "20 candidates 46 to 72 percent. Zero is best. joint5 routed instruction changes calculated from rounded "
        "mean counts: 12 candidates about 13 percent fewer, 16 about 7 percent fewer, 32 about 4 percent more, "
        "40 about 14 percent more. There were three seeds at 12 and 16, two at 32, and one at 40. "
        "Ranges are observations, not confidence intervals. Selected sizes shown; full aggregates are in "
        "docs/research/search-scaling.json. These are synthetic scores and instruction counts, not mission success "
        "rates or run-time measurements. No quantum advantage or independent confirmation is established."
    )
    svg_path = HERE / "search-scaling-2026-10-20.svg"
    fig.savefig(svg_path, format="svg", facecolor=BG, metadata={"Date": None, "Title": title, "Description": description, "Creator": "Aether AI Predator / matplotlib"})
    svg = svg_path.read_text(encoding="utf-8")
    svg = svg.replace('<svg ', '<svg role="img" aria-labelledby="search-title search-description" ', 1)
    root_end = svg.index(">", svg.index("<svg ")) + 1
    svg = svg[:root_end] + f'\n<title id="search-title">{escape(title)}</title>\n<desc id="search-description">{escape(description)}</desc>' + svg[root_end:]
    svg_path.write_text(svg, encoding="utf-8")
    if preview_dir:
        preview_dir.mkdir(parents=True, exist_ok=True)
        fig.savefig(preview_dir / "search-scaling-2026-10-20.png", dpi=150, facecolor=BG)
    plt.close(fig)
    print(f"Built {svg_path.name} from public aggregates; no experiments run.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview-dir", type=Path, help="Optional directory for a PNG layout preview")
    build(parser.parse_args().preview_dir)
