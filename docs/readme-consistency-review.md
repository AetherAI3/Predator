# Public README consistency review

Date: 2026-09-15. Repository: `AetherAI3/predator-cli`. Reviewed base: `6ec943838e0a5254c88e9dc8e8975c89f1b1e782`.

Scope: the public README, its new or updated vector assets, the linked public research notes and the product/access descriptions they support. This is a documentation review. It is not an independent scientific replication, a runtime qualification or a production deployment.

## Findings and resolutions

| Area | Resolution |
| --- | --- |
| Repository purpose | States that this repository holds the showcase and selected public notes. It does not provide an installable research CLI. |
| Product coverage | Ties Predator Security to approved assurance profiles. The public Actions page lists AetherCloud backend coverage and customer-specific profiles in private preview; Hosted Build & Test is identified separately. |
| Product versus research | Distinguishes approved Actions, private Gen3 research and conditional Gen4 transfer. Roadmap arrows do not represent completed experiments or achieved advantage. |
| Published quantum evidence | Brings the existing September 6 IBM Fez pilot into the main reading flow. It is explicitly hardware evidence, author-reported and separate from Gen3 depth trials. |
| Measurement arithmetic | Uses the existing public JSON for 144→103 gates, 28.5% rounded reduction, four TV distances and four expected energies. The numerical record and original measurement note are unchanged. |
| Unfavorable result | States prominently that expected energy increased in both cases, so minimization worsened despite the gate and output-agreement improvements. |
| Sample and time denominators | Four circuits at 1,024 shots each; one job and one fixture. Three seconds refers to recorded billed QPU time, not total wall-clock time. Related cases are not independent confirmations. |
| Quantum and transfer claims | No independent confirmation, improved optimization, Gen3 advantage or completed Gen4 upgrade is inferred from the pilot. |
| Graphical semantics | Cyan is ordinary compilation and purple is joint5. All TV-distance bars use the same 0–0.5 scale. Scope and negative result remain visible in the standalone chart. |
| Badges | Local editorial labels describe product/research scope. They do not impersonate CI, live deployment or scientific verification badges. |
| Illustration versus evidence | The unchanged console image is in an expandable section with an explicit illustrative-session caption. Its counters are not used as measurements. |
| Public disclosure | Uses the numerical data and research boundaries already present in this public repository. No private campaign record or implementation is imported. |
| Access | Repository connection and evidence inspection do not grant access to private research controls or hardware. Customer actions require supported coverage and usage approval. |
| Navigation | New navigation uses section anchors; older named section destinations are retained. Local README links are checked against the complete repository tree and new assets. |
| GitHub HTML | Uses paragraphs, links, images, tables and details/summary. No inline styles, scripts, classes, embedded SVG markup or external-font dependencies are needed in the README. |
| Branding and provenance | Preserves the existing Aether mark and console bytes. Documents the updated hero, new badges and public-data chart in the visual source record. |

## Verification status

Final consistency and structural validation: **PASS — 26 checks**. [Machine-readable check record](readme-consistency-checks.json).

Checks cover section destinations, older anchors, local links and images, GitHub-compatible HTML, descriptive image alternatives, disclosure boundaries, generation/access wording, all eight published numeric measurements, acquisition denominators, the gate-reduction calculation, the negative expected-energy result, shared chart scale, SVG accessibility metadata and deterministic rebuilding. The original numerical record, measurement note, generation guide, Aether mark and showcase source match their original Git blob hashes.

The hero, hardware chart and three new badges were rendered with a non-browser SVG renderer and visually inspected. The common-scale chart and the negative expected-energy result are legible in that rendering.

The README is parsed as GitHub-flavored Markdown with Pandoc for structural checks. That is not GitHub's production renderer or a browser-layout certification. GitHub's actual responsive rendering remains unverified in this session.

The Actions, defense-stack and contact pages were retrieved through public web access. The linked Nano, Unlimited-Context-LLM and PROTOCOL-C repository identities were verified through GitHub. The showcase URL is retained, but its live availability remains **UNVERIFIED**: the web fetch returned an internal error and the connector does not expose the Pages metadata endpoint. This is not treated as proof that the showcase is down. No endpoint or credential workaround was attempted.

## Sources and rebuilding

- [Full-precision public pilot record](research/ibm-pilot.json)
- [Pilot measurement note and uncertainty](research/ibm-fez-pilot.md)
- [Generation and public-disclosure guidance](research/generations.md)
- [Current Actions product description](https://aethersystems.net/actions)
- [GitHub markup and sanitization](https://github.com/github/markup)
- [Visual sources](assets/SOURCES.md)

Run `python3 docs/assets/build_readme_assets.py` from the repository root to regenerate the five SVGs. The script reads the public pilot JSON and contains no network, circuit or native-test execution. No experimental result was generated or changed by this README revision.
