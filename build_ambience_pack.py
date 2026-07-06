from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from render_support import find_ffmpeg, run


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "audio" / "mixkit_sources"
OUTPUT_DIR = ROOT / "audio" / "ambience"
SELECTED_DIR = ROOT / "pika" / "finals" / "selected"


SOURCES = {
    "sea_waves_birds": SOURCE_DIR / "1185_sea_waves_with_birds_loop.wav",
    "harbor_rocks": SOURCE_DIR / "1208_small_waves_harbor_rocks.wav",
    "close_sea_waves": SOURCE_DIR / "1195_close_sea_waves_loop.wav",
    "windy_sea": SOURCE_DIR / "1200_windy_sea_loop.wav",
    "hammer_wood": SOURCE_DIR / "830_hammer_hit_on_wood.wav",
    "saw_wood": SOURCE_DIR / "827_hand_saw_tool_on_wood.wav",
    "underwater": SOURCE_DIR / "1209_underwater_white_noise.wav",
}


RECIPES: dict[str, dict[str, object]] = {
    "intro_ocean": {
        "inputs": [("close_sea_waves", 0.26)],
    },
    "shot01_trade_network_fleet": {
        "inputs": [("close_sea_waves", 0.22), ("windy_sea", 0.08)],
    },
    "shot02_hero_gaulos_ship": {
        "inputs": [("close_sea_waves", 0.18), ("windy_sea", 0.10)],
    },
    "shot03_harbor_approach": {
        "inputs": [("harbor_rocks", 0.18), ("sea_waves_birds", 0.06)],
    },
    "shot04_quay_loading": {
        "inputs": [("harbor_rocks", 0.14), ("hammer_wood", 0.05)],
    },
    "shot05_marketplace_exchange": {
        "inputs": [("harbor_rocks", 0.12), ("sea_waves_birds", 0.05)],
    },
    "shot06_ship_construction": {
        "inputs": [("hammer_wood", 0.10), ("saw_wood", 0.07)],
    },
    "shot08_bormla_repair": {
        "inputs": [("harbor_rocks", 0.10), ("hammer_wood", 0.07)],
    },
    "shot09_night_navigation": {
        "inputs": [("windy_sea", 0.10), ("close_sea_waves", 0.08)],
    },
    "shot10_underwater_shipwreck": {
        "inputs": [("underwater", 0.10)],
    },
}


def find_ffprobe() -> str:
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        raise FileNotFoundError("ffprobe is required but was not found in PATH")
    return ffprobe


def probe_duration(ffprobe: str, path: Path) -> float:
    completed = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        text=True,
        capture_output=True,
        check=True,
    )
    return float(completed.stdout.strip())


def clip_duration(ffprobe: str, shot_key: str) -> float:
    if shot_key == "intro_ocean":
        clip = SELECTED_DIR / "intro_ocean.mp4"
    else:
        clip = SELECTED_DIR / f"{shot_key}.mp4"
    if not clip.exists():
        raise FileNotFoundError(f"Missing clip for ambience timing: {clip}")
    return probe_duration(ffprobe, clip)


def build_recipe(ffmpeg: str, ffprobe: str, shot_key: str, recipe: dict[str, object]) -> Path:
    output = OUTPUT_DIR / f"{shot_key}.wav"
    duration = clip_duration(ffprobe, shot_key)
    inputs = recipe["inputs"]

    cmd: list[str] = [ffmpeg, "-y"]
    filter_parts: list[str] = []
    mix_labels: list[str] = []

    for index, (source_key, volume) in enumerate(inputs):
        source_path = SOURCES[str(source_key)]
        if not source_path.exists():
            raise FileNotFoundError(f"Missing source ambience file: {source_path}")
        cmd.extend(["-stream_loop", "-1", "-i", str(source_path)])
        fade_out = min(0.45, max(duration / 3, 0.15))
        fade_out_start = max(duration - fade_out, 0.0)
        label = f"a{index}"
        filter_parts.append(
            f"[{index}:a]volume={float(volume):.3f},"
            f"afade=t=in:st=0:d=0.25,"
            f"afade=t=out:st={fade_out_start:.2f}:d={fade_out:.2f},"
            f"atrim=0:{duration:.2f}[{label}]"
        )
        mix_labels.append(f"[{label}]")

    filter_parts.append(
        "".join(mix_labels)
        + f"amix=inputs={len(mix_labels)}:duration=longest:dropout_transition=0,"
        + "alimiter=limit=0.90[aout]"
    )

    cmd.extend(
        [
            "-filter_complex",
            ";".join(filter_parts),
            "-map",
            "[aout]",
            "-ar",
            "24000",
            "-ac",
            "1",
            str(output),
        ]
    )
    run(cmd)
    return output


def main() -> None:
    ffmpeg = find_ffmpeg()
    ffprobe = find_ffprobe()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    built: list[Path] = []
    for shot_key, recipe in RECIPES.items():
        built.append(build_recipe(ffmpeg, ffprobe, shot_key, recipe))

    for path in built:
        print(path)


if __name__ == "__main__":
    main()
