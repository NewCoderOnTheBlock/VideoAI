from __future__ import annotations

from pathlib import Path

from render_support import find_ffmpeg, run


ROOT = Path(__file__).resolve().parent
PIKA_DIR = ROOT / "pika"
REFERENCE_DIR = PIKA_DIR / "reference_frames"
UPLOAD_DIR = PIKA_DIR / "upload_clips"
FPS = 30
WIDTH = 1280
HEIGHT = 720
CLIP_DURATION = 5.0


SHOTS = [
    {
        "source": ROOT / "pilot" / "assets" / "scene03_harbor.png",
        "output": UPLOAD_DIR / "shot03_harbor_approach.mp4",
    },
    {
        "source": ROOT / "pilot" / "assets" / "scene02_trade.png",
        "output": UPLOAD_DIR / "shot04_quay_loading.mp4",
    },
    {
        "source": REFERENCE_DIR / "scene04_marketplace_exchange.png",
        "output": UPLOAD_DIR / "shot05_marketplace_exchange.mp4",
    },
    {
        "source": ROOT / "pilot" / "assets" / "scene04_shipwrights.png",
        "output": UPLOAD_DIR / "shot06_ship_construction.mp4",
    },
    {
        "source": REFERENCE_DIR / "scene08_bormla_repair.png",
        "output": UPLOAD_DIR / "shot08_bormla_repair.mp4",
    },
]
def main() -> None:
    ffmpeg = find_ffmpeg()
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    frames = int(CLIP_DURATION * FPS)
    for shot in SHOTS:
        source = Path(shot["source"])
        output = Path(shot["output"])
        if not source.exists():
            raise FileNotFoundError(f"Missing source image: {source}")

        filtergraph = (
            f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,"
            f"crop={WIDTH}:{HEIGHT},"
            f"zoompan=z='min(zoom+0.00035,1.05)':"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s={WIDTH}x{HEIGHT}:fps={FPS},"
            f"format=yuv420p"
        )

        cmd = [
            ffmpeg,
            "-y",
            "-loop",
            "1",
            "-i",
            str(source),
            "-vf",
            filtergraph,
            "-frames:v",
            str(frames),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            str(output),
        ]
        run(cmd)
        print(output)


if __name__ == "__main__":
    main()
