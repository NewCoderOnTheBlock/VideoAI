from __future__ import annotations

import subprocess
from pathlib import Path

from render_support import find_ffmpeg, run


ROOT = Path(__file__).resolve().parent
KEYFRAME_DIR = ROOT / "runway" / "extended_cut_keyframes"
OUTPUT_DIR = ROOT / "pika" / "finals" / "selected"
WIDTH = 1280
HEIGHT = 720
FPS = 24


INSERTS = [
    {
        "image": "insert_trade_goods_detail.png",
        "output": "insert_trade_goods_detail_v2.mp4",
        "duration": 8.08,
        "zoom_start": 1.00,
        "zoom_end": 1.08,
        "x_expr": "iw*0.06",
        "y_expr": "ih*0.04",
    },
    {
        "image": "insert_gaulos_broadside_hull.png",
        "output": "insert_gaulos_broadside_hull_v2.mp4",
        "duration": 8.08,
        "zoom_start": 1.02,
        "zoom_end": 1.10,
        "x_expr": "iw*0.02",
        "y_expr": "ih*0.08",
    },
    {
        "image": "insert_cultural_influence_map.png",
        "output": "insert_cultural_influence_map_v2.mp4",
        "duration": 10.08,
        "zoom_start": 1.00,
        "zoom_end": 1.12,
        "x_expr": "iw*0.04",
        "y_expr": "ih*0.03",
    },
]


def probe_frames(duration: float) -> int:
    return int(round(duration * FPS))


def build_insert(ffmpeg: str, config: dict[str, object]) -> Path:
    image = KEYFRAME_DIR / str(config["image"])
    output = OUTPUT_DIR / str(config["output"])
    duration = float(config["duration"])
    frames = probe_frames(duration)
    zoom_start = float(config["zoom_start"])
    zoom_end = float(config["zoom_end"])
    zoom_step = (zoom_end - zoom_start) / max(frames - 1, 1)

    zoom_expr = f"min(on*{zoom_step:.7f}+{zoom_start:.4f},{zoom_end:.4f})"
    crop_expr = (
        "zoompan="
        f"z='{zoom_expr}':"
        f"x='{config['x_expr']}+((iw-iw/zoom)/2)':"
        f"y='{config['y_expr']}+((ih-ih/zoom)/2)':"
        f"d={frames}:s={WIDTH}x{HEIGHT}:fps={FPS},"
        "eq=saturation=1.02:contrast=1.02:brightness=0.01,"
        "unsharp=5:5:0.35:5:5:0.0,"
        "format=yuv420p"
    )

    cmd = [
        ffmpeg,
        "-y",
        "-loop",
        "1",
        "-i",
        str(image),
        "-t",
        f"{duration:.2f}",
        "-vf",
        crop_expr,
        "-an",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        str(output),
    ]
    run(cmd)
    return output


def main() -> None:
    ffmpeg = find_ffmpeg()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    built = [build_insert(ffmpeg, config) for config in INSERTS]
    for path in built:
        print(path)


if __name__ == "__main__":
    main()
