"""Refresh SHA-256 and frame counts for the public HTB media index."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image


HERE = Path(__file__).resolve().parent
ITEMS = [
    ("satellite-exploitation/certificate.png", "owner-supplied HTB track certificate"),
    ("satellite-exploitation/combined-replay.gif", "replay of four saved Predator lab records and certificate"),
    ("satellite-exploitation/baby-frame-replay.gif", "original saved Baby Frame replay"),
    ("satellite-exploitation/no-errors-replay.gif", "original saved No Errors replay"),
    ("ai-ml-exploitation/prometheon-replay.gif", "saved Prometheon Predator replay"),
    ("ai-ml-exploitation/lost-in-hyperspace-replay.gif", "saved Lost in Hyperspace Predator replay"),
    ("ai-ml-exploitation/spin-glass-brain-replay.gif", "corrected Spin Glass Brain Predator replay"),
    ("machines/blocksynergy/predator-replay.gif", "sanitized BlockSynergy machine evidence replay"),
    ("machines/ghostlink/predator-pwnbox-replay.gif", "cleaned full-screen Ghostlink VPS3 pwnbox recording"),
    ("../media/predator-vpn-scan-preview.gif", "existing sanitized Academy Nmap replay"),
    ("../media/predator-pwnbox-ttl-preview.gif", "existing sanitized Pwnbox workflow preview"),
]


def main() -> None:
    assets = []
    for name, description in ITEMS:
        path = (HERE / name).resolve()
        with path.open("rb") as source:
            digest = hashlib.file_digest(source, "sha256").hexdigest()
        with Image.open(path) as media:
            item = {
                "path": name,
                "description": description,
                "sha256": digest,
                "bytes": path.stat().st_size,
                "kind": "replay" if path.suffix.lower() == ".gif" else "certificate",
            }
            if item["kind"] == "replay":
                item["frames"] = media.n_frames
                item["replay_not_continuous_recording"] = True
        assets.append(item)
    payload = {
        "version": 1,
        "updated": "2026-10-06",
        "satellite_certificate_reference": "https://labs.hackthebox.com/achievement/track/4038252/99",
        "assets": assets,
    }
    (HERE / "media-manifest.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Indexed {len(assets)} public HTB media assets")


if __name__ == "__main__":
    main()
