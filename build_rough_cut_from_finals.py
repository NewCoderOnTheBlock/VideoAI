from __future__ import annotations

from pathlib import Path

from render_support import find_ffmpeg, run


ROOT = Path(__file__).resolve().parent
SELECTED_DIR = ROOT / "pika" / "finals" / "selected"
OUTPUT_DIR = ROOT / "pilot" / "output"
TEMP_DIR = OUTPUT_DIR / "rough_cut_clips"
WIDTH = 1280
HEIGHT = 720
FPS = 24


CLIPS = [
    "intro_ocean.mp4",
    "shot01_trade_network_fleet.mp4",
    "shot02_hero_gaulos_ship.mp4",
    "shot03_harbor_approach.mp4",
    "shot04_quay_loading.mp4",
    "shot05_marketplace_exchange.mp4",
    "shot06_ship_construction.mp4",
    "shot07_trade_route_map.mp4",
    "shot08_bormla_repair.mp4",
]
def normalize_clip(ffmpeg: str, source: Path, output: Path) -> None:
    cmd = [
        ffmpeg,
        "-y",
        "-i",
        str(source),
        "-vf",
        f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,crop={WIDTH}:{HEIGHT},fps={FPS},format=yuv420p",
        "-an",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        str(output),
    ]
    run(cmd)


def main() -> None:
    ffmpeg = find_ffmpeg()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    normalized: list[Path] = []
    for index, clip_name in enumerate(CLIPS, start=1):
        source = SELECTED_DIR / clip_name
        if not source.exists():
            raise FileNotFoundError(f"Missing selected clip: {source}")
        output = TEMP_DIR / f"{index:02d}_{clip_name}"
        normalize_clip(ffmpeg, source, output)
        normalized.append(output)

    concat_file = OUTPUT_DIR / "rough_cut_concat.txt"
    concat_file.write_text(
        "\n".join(f"file '{clip.resolve().as_posix()}'" for clip in normalized) + "\n",
        encoding="utf-8",
    )

    final_output = OUTPUT_DIR / "phoenician_pilot_rough_cut.mp4"
    cmd = [
        ffmpeg,
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat_file),
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        str(final_output),
    ]
    run(cmd)
    print(final_output)


if __name__ == "__main__":
    main()
