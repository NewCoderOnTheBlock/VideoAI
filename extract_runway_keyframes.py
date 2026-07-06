from __future__ import annotations

from pathlib import Path

from render_support import find_ffmpeg, run


ROOT = Path(__file__).resolve().parent
RUNWAY_DIR = ROOT / "runway" / "keyframes"
PIKA_DIR = ROOT / "pika"
UPLOAD_DIR = PIKA_DIR / "upload_clips"


VIDEO_SHOTS = [
    {
        "input": PIKA_DIR / "boat.mp4",
        "output": RUNWAY_DIR / "shot01_trade_network_fleet.png",
        "timestamp": "00:00:02.50",
    },
    {
        "input": PIKA_DIR / "biggerscaleboat.mp4",
        "output": RUNWAY_DIR / "shot02_hero_gaulos_ship.png",
        "timestamp": "00:00:02.50",
    },
    {
        "input": UPLOAD_DIR / "shot03_harbor_approach.mp4",
        "output": RUNWAY_DIR / "shot03_harbor_approach.png",
        "timestamp": "00:00:02.50",
    },
    {
        "input": UPLOAD_DIR / "shot04_quay_loading.mp4",
        "output": RUNWAY_DIR / "shot04_quay_loading.png",
        "timestamp": "00:00:02.50",
    },
    {
        "input": UPLOAD_DIR / "shot05_marketplace_exchange.mp4",
        "output": RUNWAY_DIR / "shot05_marketplace_exchange.png",
        "timestamp": "00:00:02.50",
    },
    {
        "input": UPLOAD_DIR / "shot06_ship_construction.mp4",
        "output": RUNWAY_DIR / "shot06_ship_construction.png",
        "timestamp": "00:00:02.50",
    },
    {
        "input": PIKA_DIR / "map.mp4",
        "output": RUNWAY_DIR / "shot07_trade_route_map.png",
        "timestamp": "00:00:02.50",
    },
    {
        "input": UPLOAD_DIR / "shot08_bormla_repair.mp4",
        "output": RUNWAY_DIR / "shot08_bormla_repair.png",
        "timestamp": "00:00:02.50",
    },
]
def main() -> None:
    ffmpeg = find_ffmpeg()
    RUNWAY_DIR.mkdir(parents=True, exist_ok=True)

    for shot in VIDEO_SHOTS:
        source = Path(shot["input"])
        output = Path(shot["output"])
        if not source.exists():
            raise FileNotFoundError(f"Missing input clip: {source}")

        cmd = [
            ffmpeg,
            "-y",
            "-ss",
            str(shot["timestamp"]),
            "-i",
            str(source),
            "-frames:v",
            "1",
            str(output),
        ]
        run(cmd)
        print(output)


if __name__ == "__main__":
    main()
