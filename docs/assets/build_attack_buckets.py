"""Build the public ATT&CK and Aether research-bucket card.

This editorial figure contains catalog labels only. It intentionally omits
private chain transitions, prerequisites, payloads, and report details.
"""

from html import escape
from pathlib import Path


OUT = Path(__file__).with_name("attack-buckets-v15.svg")

# MITRE ATT&CK Enterprise tactic names and IDs, checked October 10, 2026.
TACTICS = [
    ("TA0043", "Reconnaissance"),
    ("TA0042", "Resource Development"),
    ("TA0001", "Initial Access"),
    ("TA0002", "Execution"),
    ("TA0003", "Persistence"),
    ("TA0004", "Privilege Escalation"),
    ("TA0005", "Stealth"),
    ("TA0112", "Defense Impairment"),
    ("TA0006", "Credential Access"),
    ("TA0007", "Discovery"),
    ("TA0008", "Lateral Movement"),
    ("TA0009", "Collection"),
    ("TA0011", "Command and Control"),
    ("TA0010", "Exfiltration"),
    ("TA0040", "Impact"),
]

CUSTOM = [
    ("01", "AI Injection", "Prompts / context / retrieved content", "#70b9ff"),
    ("02", "MCP Top 10", "Tools / permissions / connectors", "#a78bfa"),
    ("03", "Memory-Safety Primitives", "Native-code weakness building blocks", "#6ee7c2"),
]

parts = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1050" viewBox="0 0 1600 1050" role="img" aria-labelledby="title desc">',
    '<title id="title">Predator ATT&amp;CK and Aether research buckets</title>',
    '<desc id="desc">A public catalog overview: 421 modeled chains in 18 Predator routing buckets; all 15 current MITRE ATT&amp;CK Enterprise tactics; three Aether research areas for AI injection, MCP Top 10, and memory-safety primitives. GX Gemini CLI and GLX GitLab Duo are named as private case families only. No exploit details are shown.</desc>',
    '<defs>',
    '<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#07111f"/><stop offset=".56" stop-color="#0b1830"/><stop offset="1" stop-color="#100c22"/></linearGradient>',
    '<linearGradient id="topLine"><stop stop-color="#2dd4ef"/><stop offset=".52" stop-color="#8877f8"/><stop offset="1" stop-color="#58e6ba"/></linearGradient>',
    '<radialGradient id="glow"><stop stop-color="#20bde0" stop-opacity=".16"/><stop offset="1" stop-color="#20bde0" stop-opacity="0"/></radialGradient>',
    '<filter id="shadow" x="-.2" y="-.3" width="1.4" height="1.6"><feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#010611" flood-opacity=".36"/></filter>',
    '</defs>',
    '<rect width="1600" height="1050" fill="url(#bg)"/>',
    '<circle cx="1200" cy="120" r="470" fill="url(#glow)"/>',
    '<path d="M0 2H1600" stroke="url(#topLine)" stroke-width="4"/>',
    '<g opacity=".10" stroke="#75a4ca"><path d="M0 278H1600M0 909H1600"/><path d="M968 285V908"/></g>',
    '<rect x="54" y="40" width="54" height="54" rx="14" fill="#102f45" stroke="#3ad6eb" stroke-opacity=".55"/>',
    '<text x="81" y="77" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="32" font-weight="800" fill="#81e9fa">Æ</text>',
    '<text x="126" y="62" font-family="Arial,Helvetica,sans-serif" font-size="15" font-weight="800" letter-spacing="3" fill="#8de8f6">AETHER AI  /  PREDATOR</text>',
    '<text x="54" y="139" font-family="Arial,Helvetica,sans-serif" font-size="43" font-weight="800" fill="#f5f8ff">Attack-chain research map</text>',
    '<text x="56" y="177" font-family="Arial,Helvetica,sans-serif" font-size="19" fill="#a9bbd0">MITRE Enterprise tactics and Aether research buckets, shown as separate catalog lenses.</text>',
]

for x, value, label, color in [
    (54, "421", "MODELED CHAINS", "#80e7f5"),
    (550, "15", "MITRE ENTERPRISE TACTICS", "#b7a2ff"),
    (1046, "18", "PREDATOR ROUTING BUCKETS", "#8cf0c9"),
]:
    parts.extend([
        f'<rect x="{x}" y="205" width="476" height="93" rx="16" fill="#102038" fill-opacity=".90" stroke="{color}" stroke-opacity=".30"/>',
        f'<text x="{x + 22}" y="262" font-family="Arial,Helvetica,sans-serif" font-size="47" font-weight="800" fill="{color}">{value}</text>',
        f'<text x="{x + 125}" y="258" font-family="Arial,Helvetica,sans-serif" font-size="15" font-weight="700" letter-spacing="1.5" fill="#c7d4e7">{label}</text>',
    ])

parts.extend([
    '<text x="54" y="351" font-family="Arial,Helvetica,sans-serif" font-size="15" font-weight="800" letter-spacing="3" fill="#7ce4f4">MITRE ATT&amp;CK  /  ENTERPRISE</text>',
    '<text x="54" y="380" font-family="Arial,Helvetica,sans-serif" font-size="17" fill="#91a8c0">Current tactic names and IDs · matrix order, not an attack sequence</text>',
    '<text x="1004" y="351" font-family="Arial,Helvetica,sans-serif" font-size="15" font-weight="800" letter-spacing="3" fill="#b49eff">AETHER  /  CUSTOM AREAS</text>',
    '<text x="1004" y="380" font-family="Arial,Helvetica,sans-serif" font-size="17" fill="#91a8c0">Additional lenses for modern research surfaces</text>',
])

for idx, (tactic_id, name) in enumerate(TACTICS):
    col, row = idx % 3, idx // 3
    x, y = 54 + col * 306, 403 + row * 94
    color = ("#73dff0", "#a9a0f8", "#70dbc0")[col]
    parts.extend([
        f'<rect x="{x}" y="{y}" width="291" height="81" rx="13" fill="#111e34" stroke="#38516a" stroke-opacity=".75" filter="url(#shadow)"/>',
        f'<path d="M{x + 1} {y + 20}V{y + 61}" stroke="{color}" stroke-width="3" stroke-linecap="round"/>',
        f'<text x="{x + 19}" y="{y + 28}" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="700" letter-spacing="1.4" fill="{color}">{tactic_id}</text>',
        f'<text x="{x + 19}" y="{y + 59}" font-family="Arial,Helvetica,sans-serif" font-size="21" font-weight="700" fill="#f0f5fc">{escape(name)}</text>',
    ])

for idx, (num, name, sub, color) in enumerate(CUSTOM):
    y = 403 + idx * 157
    parts.extend([
        f'<rect x="1004" y="{y}" width="542" height="141" rx="17" fill="#161c38" stroke="{color}" stroke-opacity=".40" filter="url(#shadow)"/>',
        f'<rect x="1023" y="{y + 19}" width="44" height="44" rx="11" fill="{color}" fill-opacity=".15" stroke="{color}" stroke-opacity=".55"/>',
        f'<text x="1045" y="{y + 48}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="17" font-weight="800" fill="{color}">{num}</text>',
        f'<text x="1083" y="{y + 51}" font-family="Arial,Helvetica,sans-serif" font-size="26" font-weight="800" fill="#f3f5ff">{escape(name)}</text>',
        f'<text x="1024" y="{y + 105}" font-family="Arial,Helvetica,sans-serif" font-size="19" fill="#acbdd3">{escape(sub)}</text>',
    ])

parts.extend([
    '<rect x="54" y="885" width="1492" height="104" rx="17" fill="#0d2633" stroke="#55b6ce" stroke-opacity=".43"/>',
    '<text x="77" y="916" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="800" letter-spacing="2.4" fill="#85ddec">PRIVATE CASE FAMILIES  /  PUBLIC LABELS ONLY</text>',
    '<rect x="77" y="934" width="430" height="37" rx="9" fill="#173c4a"/>',
    '<text x="94" y="960" font-family="Arial,Helvetica,sans-serif" font-size="19" font-weight="800" fill="#d6faff">GX  ·  GEMINI CLI</text>',
    '<rect x="521" y="934" width="430" height="37" rx="9" fill="#30294d"/>',
    '<text x="538" y="960" font-family="Arial,Helvetica,sans-serif" font-size="19" font-weight="800" fill="#e6ddff">GLX  ·  GITLAB DUO</text>',
    '<text x="966" y="960" font-family="Arial,Helvetica,sans-serif" font-size="16" fill="#a6bdd0">No chain transitions, payloads, or report details shown.</text>',
    '<text x="56" y="1022" font-family="Arial,Helvetica,sans-serif" font-size="15" fill="#91a8c0">Registry snapshot: V15 · 10 Oct 2026. Predator selector labels are not a one-to-one copy of the MITRE matrix.</text>',
    '</svg>',
])

OUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
print(OUT)
