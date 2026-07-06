from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


def find_ffmpeg() -> str:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise FileNotFoundError("ffmpeg is required but was not found in PATH")
    return ffmpeg


def find_font() -> Path:
    override = os.environ.get("VIDEOAI_FONT")
    if override:
        candidate = Path(override)
        if candidate.exists():
            return candidate

    candidates = [
        Path("C:/Windows/Fonts/georgia.ttf"),
        Path("C:/Windows/Fonts/times.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf"),
        Path("/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"),
        Path("/Library/Fonts/Georgia.ttf"),
        Path("/System/Library/Fonts/Supplemental/Times New Roman.ttf"),
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        "No suitable font file found. Set VIDEOAI_FONT to an installed .ttf path."
    )


def escape_drawtext(value: str) -> str:
    return value.replace("\\", "\\\\").replace(":", r"\:").replace("'", r"\'")


def font_arg(font_path: Path) -> str:
    return font_path.as_posix().replace(":", r"\:")


def run(cmd: list[str]) -> None:
    completed = subprocess.run(cmd, text=True, capture_output=True)
    if completed.returncode != 0:
        raise RuntimeError(
            "Command failed with exit code "
            f"{completed.returncode}:\n{' '.join(cmd)}\n{completed.stderr.strip()}"
        )

