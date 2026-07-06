from __future__ import annotations

from pathlib import Path

from render_support import escape_drawtext, find_ffmpeg, find_font, font_arg, run


ROOT = Path(__file__).resolve().parent
PILOT_DIR = ROOT / "pilot"
ASSET_DIR = PILOT_DIR / "assets"
OUTPUT_DIR = PILOT_DIR / "output"
CLIP_DIR = OUTPUT_DIR / "clips_alive"
SEGMENT_DIR = CLIP_DIR / "segments"
FPS = 25
WIDTH = 1920
HEIGHT = 1080
SEGMENT_DURATION = 3.8
CROSSFADE_DURATION = 0.8


SCENES = [
    {
        "base": ASSET_DIR / "scene01_fleet.png",
        "alt": ASSET_DIR / "scene01_fleet_alt.png",
        "output": CLIP_DIR / "scene01_fleet_alive.mp4",
        "title": "Trade Network",
        "subtitle": "Merchant ships advance as wind, wake, and formation keep moving",
    },
    {
        "base": ASSET_DIR / "scene02_trade.png",
        "alt": ASSET_DIR / "scene02_trade_alt.png",
        "output": CLIP_DIR / "scene02_trade_alive.mp4",
        "title": "Cargo Exchange",
        "subtitle": "The quay stays active as workers pass goods and shift along the hull",
    },
    {
        "base": ASSET_DIR / "scene03_harbor.png",
        "alt": ASSET_DIR / "scene03_harbor_alt.png",
        "output": CLIP_DIR / "scene03_harbor_alive.mp4",
        "title": "Safe Harbor",
        "subtitle": "Bormla feels lived in through drifting ships, ripples, and quay traffic",
    },
    {
        "base": ASSET_DIR / "scene04_shipwrights.png",
        "alt": ASSET_DIR / "scene04_shipwrights_alt.png",
        "output": CLIP_DIR / "scene04_shipwrights_alive.mp4",
        "title": "Shipbuilding Skill",
        "subtitle": "The hull and shipwrights move through the next beat of the build",
    },
]

def scene_duration() -> float:
    return (SEGMENT_DURATION * 3.0) - (CROSSFADE_DURATION * 2.0)


def build_intro(ffmpeg: str, font: Path) -> Path:
    output = CLIP_DIR / "intro_alive.mp4"
    font_file = font_arg(font)
    filtergraph = (
        f"fade=t=in:st=0:d=0.4,"
        f"fade=t=out:st=2.6:d=0.4,"
        f"drawtext=fontfile='{font_file}':text='Phoenician Trade':"
        f"x=(w-text_w)/2:y=420:fontsize=72:fontcolor=white,"
        f"drawtext=fontfile='{font_file}':text='Motion pilot v2 with in-scene activity':"
        f"x=(w-text_w)/2:y=520:fontsize=34:fontcolor=white@0.92"
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


def build_segment(
    ffmpeg: str,
    source: Path,
    output: Path,
    duration: float,
    zoom_start: float,
    zoom_end: float,
) -> Path:
    frames = int(duration * FPS)
    zoom_step = (zoom_end - zoom_start) / max(frames - 1, 1)
    filtergraph = (
        f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,"
        f"crop={WIDTH}:{HEIGHT},"
        f"zoompan=z='min({zoom_start}+on*{zoom_step:.8f},{zoom_end})':"
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
    return output


def build_scene_clip(ffmpeg: str, font: Path, scene: dict[str, object], index: int) -> Path:
    base = Path(scene["base"])
    alt = Path(scene["alt"])
    output = Path(scene["output"])
    title = escape_drawtext(str(scene["title"]))
    subtitle = escape_drawtext(str(scene["subtitle"]))
    duration = scene_duration()
    font_file = font_arg(font)

    seg1 = build_segment(
        ffmpeg,
        base,
        SEGMENT_DIR / f"scene{index:02d}_a1.mp4",
        SEGMENT_DURATION,
        1.0,
        1.035,
    )
    seg2 = build_segment(
        ffmpeg,
        alt,
        SEGMENT_DIR / f"scene{index:02d}_b.mp4",
        SEGMENT_DURATION,
        1.01,
        1.045,
    )
    seg3 = build_segment(
        ffmpeg,
        base,
        SEGMENT_DIR / f"scene{index:02d}_a2.mp4",
        SEGMENT_DURATION,
        1.02,
        1.055,
    )

    offset_one = SEGMENT_DURATION - CROSSFADE_DURATION
    offset_two = (SEGMENT_DURATION * 2.0) - (CROSSFADE_DURATION * 2.0)
    fade_out_start = duration - 0.6
    filtergraph = (
        f"[0:v][1:v]xfade=transition=dissolve:duration={CROSSFADE_DURATION}:offset={offset_one}[v01];"
        f"[v01][2:v]xfade=transition=dissolve:duration={CROSSFADE_DURATION}:offset={offset_two},"
        f"fade=t=in:st=0:d=0.5,"
        f"fade=t=out:st={fade_out_start}:d=0.6,"
        f"drawbox=x=70:y=820:w=1780:h=170:color=black@0.30:t=fill,"
        f"drawtext=fontfile='{font_file}':text='{title}':"
        f"x=110:y=855:fontsize=48:fontcolor=white,"
        f"drawtext=fontfile='{font_file}':text='{subtitle}':"
        f"x=112:y=918:fontsize=28:fontcolor=white@0.92[v]"
    )
    cmd = [
        ffmpeg,
        "-y",
        "-i",
        str(seg1),
        "-i",
        str(seg2),
        "-i",
        str(seg3),
        "-filter_complex",
        filtergraph,
        "-map",
        "[v]",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        str(output),
    ]
    run(cmd)
    return output


def build_concat_file(parts: list[Path]) -> Path:
    concat_file = OUTPUT_DIR / "concat_alive.txt"
    lines = [f"file '{part.resolve().as_posix()}'" for part in parts]
    concat_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return concat_file


def main() -> None:
    ffmpeg = find_ffmpeg()
    font = find_font()
    CLIP_DIR.mkdir(parents=True, exist_ok=True)
    SEGMENT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    missing: list[str] = []
    for scene in SCENES:
        for key in ("base", "alt"):
            path = Path(scene[key])
            if not path.exists():
                missing.append(str(path))
    if missing:
        raise FileNotFoundError("Missing pilot assets:\n" + "\n".join(missing))

    parts = [build_intro(ffmpeg, font)]
    for index, scene in enumerate(SCENES, start=1):
        parts.append(build_scene_clip(ffmpeg, font, scene, index))

    concat_file = build_concat_file(parts)
    final_output = OUTPUT_DIR / "phoenician_pilot_preview_alive.mp4"
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
