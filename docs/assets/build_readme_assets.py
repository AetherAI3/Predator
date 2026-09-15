"""Build public README SVGs from the published pilot JSON; no experiment calls."""
import json
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE.parent / "research/ibm-pilot.json").read_text())
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


if __name__ == "__main__":
    assert DATA["schema"] == "predator.public-compiler-pilot.v1" and DATA["independent_confirmation"] is False
    assert (DATA["hardware_jobs"], DATA["circuits"], DATA["shots_per_circuit"], DATA["billed_qpu_seconds"]) == (1, 4, 1024, 3)
    assert (DATA["two_qubit_gates"]["ordinary"], DATA["two_qubit_gates"]["joint5"]) == (144, 103)
    assert all(p["joint5_tv"] < p["ordinary_tv"] and p["joint5_expected_energy"] > p["ordinary_expected_energy"] for p in DATA["poles"].values())
    outputs = {"readme-hero.svg": hero(), "readme-hardware-data.svg": hardware(),
               "tag-actions-profiles.svg": badge("ACTIONS", "LOCKED PROFILES", GREEN),
               "tag-gen3-private.svg": badge("GEN 3", "PRIVATE RESEARCH", PURPLE),
               "tag-hardware-pilot.svg": badge("HARDWARE", "PUBLISHED PILOT", BLUE)}
    for name, svg in outputs.items():
        (HERE/name).write_text(svg, encoding="utf-8")
    print(f"Built {len(outputs)} public README SVGs from the existing public record.")
