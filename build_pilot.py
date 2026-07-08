from __future__ import annotations

from pathlib import Path

from render_support import escape_drawtext, find_ffmpeg, find_font, font_arg, run


ROOT = Path(__file__).resolve().parent
PILOT_DIR = ROOT / "pilot"
ASSET_DIR = PILOT_DIR / "assets"
OUTPUT_DIR = PILOT_DIR / "output"
CLIP_DIR = OUTPUT_DIR / "clips"
FPS = 25
WIDTH = 1920
HEIGHT = 1080


SCENES = [
    {
        "input": ASSET_DIR / "scene01_fleet.png",
        "output": CLIP_DIR / "scene01_fleet.mp4",
        "title": "Trade Network",
        "subtitle": "Phoenician merchant fleets cross the Mediterranean",
        "duration": 9.0,
    },
    {
        "input": ASSET_DIR / "scene02_trade.png",
        "output": CLIP_DIR / "scene02_trade.mp4",
        "title": "Cargo Exchange",
        "subtitle": "Amphorae and millstones move through a working quay",
        "duration": 9.0,
    },
    {
        "input": ASSET_DIR / "scene03_harbor.png",
        "output": CLIP_DIR / "scene03_harbor.mp4",
        "title": "Safe Harbor",
        "subtitle": "Bormla offers shelter, geography, and strategic reach",
        "duration": 9.0,
    },
    {
        "input": ASSET_DIR / "scene04_shipwrights.png",
        "output": CLIP_DIR / "scene04_shipwrights.mp4",
        "title": "Shipbuilding Skill",
        "subtitle": "Gaulos craftsmanship relies on joinery, timber, and resin",
        "duration": 9.0,
    },
]
def build_intro(ffmpeg: str, font: Path) -> Path:
    output = CLIP_DIR / "intro.mp4"
    font_file = font_arg(font)
    filtergraph = (
        f"fade=t=in:st=0:d=0.4,"
        f"fade=t=out:st=2.6:d=0.4,"
        f"drawtext=fontfile='{font_file}':text='Phoenician Trade':"
        f"x=(w-text_w)/2:y=430:fontsize=72:fontcolor=white,"
        f"drawtext=fontfile='{font_file}':text='Visual pilot built from the PDF and scene notes':"
        f"x=(w-text_w)/2:y=530:fontsize=34:fontcolor=white@0.9"
    )
    cmd = [
        ffmpeg,
        "-y",
        "-f",
        "lavfi",
        "-i",
        f"color=c=#0f1822:s={WIDTH}x{HEIGHT}:r={FPS}:d=3",
        "-vf",
        filtergraph,
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        str(output),
    ]
    run(cmd)
    return output


def build_scene_clip(ffmpeg: str, font: Path, scene: dict[str, object]) -> Path:
    source = Path(scene["input"])
    output = Path(scene["output"])
    title = escape_drawtext(str(scene["title"]))
    subtitle = escape_drawtext(str(scene["subtitle"]))
    duration = float(scene["duration"])
    frames = int(duration * FPS)
    font_file = font_arg(font)
    filtergraph = (
        f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,"
        f"crop={WIDTH}:{HEIGHT},"
        f"zoompan=z='min(zoom+0.00035,1.08)':"
        f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
        f"d={frames}:s={WIDTH}x{HEIGHT}:fps={FPS},"
        f"format=yuv420p,"
        f"fade=t=in:st=0:d=0.5,"
        f"fade=t=out:st={duration - 0.6}:d=0.6,"
        f"drawbox=x=70:y=820:w=1780:h=170:color=black@0.30:t=fill,"
        f"drawtext=fontfile='{font_file}':text='{title}':"
        f"x=110:y=855:fontsize=48:fontcolor=white,"
        f"drawtext=fontfile='{font_file}':text='{subtitle}':"
        f"x=112:y=918:fontsize=28:fontcolor=white@0.92"
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
    return output


def build_concat_file(parts: list[Path]) -> Path:
    concat_file = OUTPUT_DIR / "concat.txt"
    lines = [f"file '{part.resolve().as_posix()}'" for part in parts]
    concat_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return concat_file


def main() -> None:
    ffmpeg = find_ffmpeg()
    font = find_font()
    CLIP_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    missing = [str(scene["input"]) for scene in SCENES if not Path(scene["input"]).exists()]
    if missing:
        raise FileNotFoundError("Missing pilot assets:\n" + "\n".join(missing))

    parts = [build_intro(ffmpeg, font)]
    for scene in SCENES:
        parts.append(build_scene_clip(ffmpeg, font, scene))

    concat_file = build_concat_file(parts)
    final_output = OUTPUT_DIR / "phoenician_pilot_preview.mp4"
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
