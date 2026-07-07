from __future__ import annotations

import asyncio
import os
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

from render_support import escape_drawtext, find_ffmpeg, find_font, font_arg, run


ROOT = Path(__file__).resolve().parent
WORKSPACE_ROOT = ROOT.parent


def resolve_dir(env_name: str, local_path: Path, fallback_path: Path, required_names: tuple[str, ...]) -> Path:
    env_value = os.environ.get(env_name)
    if env_value:
        return Path(env_value).resolve()

    def has_required(path: Path) -> bool:
        return path.exists() and all((path / name).exists() for name in required_names)

    if has_required(local_path):
        return local_path.resolve()
    if has_required(fallback_path):
        return fallback_path.resolve()
    return local_path.resolve()


SELECTED_DIR = resolve_dir(
    "VIDEO_SELECTED_DIR",
    ROOT / "pika" / "finals" / "selected",
    WORKSPACE_ROOT / "pika" / "finals" / "selected",
    ("intro_ocean.mp4", "shot01_trade_network_fleet.mp4"),
)
OUTPUT_DIR = Path(
    os.environ.get("VIDEO_OUTPUT_DIR", str(ROOT / "pilot" / "output" / "pdf_cut"))
).resolve()
VIDEO_DIR = OUTPUT_DIR / "video_parts"
AUDIO_DIR = OUTPUT_DIR / "audio_parts"
MIXED_AUDIO_DIR = OUTPUT_DIR / "mixed_audio_parts"
DEFAULT_NARRATION = (
    ROOT / "pdf_cut_narration_extended_draft.txt"
    if (ROOT / "pdf_cut_narration_extended_draft.txt").exists()
    else ROOT / "pdf_cut_narration.txt"
)
NARRATION_FILE = Path(
    os.environ.get("VIDEO_NARRATION_FILE", str(DEFAULT_NARRATION))
).resolve()
AMBIENCE_DIR = resolve_dir(
    "VIDEO_AMBIENCE_DIR",
    ROOT / "audio" / "ambience",
    WORKSPACE_ROOT / "audio" / "ambience",
    ("intro_ocean.wav",),
)
MUSIC_DIR = resolve_dir(
    "VIDEO_MUSIC_DIR",
    ROOT / "audio" / "music",
    WORKSPACE_ROOT / "audio" / "music",
    ("bed.mp3",),
)

WIDTH = 1280
HEIGHT = 720
FPS = 24
SAMPLE_RATE = 24000
VOICE = os.environ.get("VIDEO_TTS_VOICE", "en-GB-SoniaNeural")
VOICE_RATE = os.environ.get("VIDEO_TTS_RATE", "-8%")
VOICE_PITCH = os.environ.get("VIDEO_TTS_PITCH", "-14Hz")
AMBIENCE_EXTENSIONS = (".wav", ".mp3", ".m4a", ".flac", ".ogg")
DEFAULT_AMBIENCE_VOLUME = 0.10
MUSIC_VOLUME = 0.045


STANDARD_SEGMENTS: list[dict[str, object]] = [
    {"key": "intro_ocean", "source": "intro_ocean.mp4", "ambience_volume": 0.10},
    {"key": "shot01_trade_network_fleet", "source": "shot01_trade_network_fleet.mp4", "ambience_volume": 0.10},
    {"key": "shot02_hero_gaulos_ship", "source": "shot02_hero_gaulos_ship.mp4", "ambience_volume": 0.09},
    {"key": "shot03_harbor_approach", "source": "shot03_harbor_approach.mp4", "ambience_volume": 0.12},
    {"key": "shot04_quay_loading", "source": "shot04_quay_loading.mp4", "ambience_volume": 0.13},
    {"key": "shot05_marketplace_exchange", "source": "shot05_marketplace_exchange.mp4", "ambience_volume": 0.12},
    {"key": "shot06_ship_construction", "source": "shot06_ship_construction.mp4", "ambience_volume": 0.11},
    {"key": "shot07_trade_route_map", "source": "shot07_trade_route_map.mp4", "ambience_volume": 0.06},
    {"key": "shot08_bormla_repair", "source": "shot08_bormla_repair.mp4", "ambience_volume": 0.11},
    {"key": "shot09_night_navigation", "source": "shot09_night_navigation.mp4", "ambience_volume": 0.07},
    {"key": "shot10_underwater_shipwreck", "source": "shot10_underwater_shipwreck.mp4", "ambience_volume": 0.05},
    {"key": "shot11_modern_conservation", "source": "shot11_modern_conservation.mp4", "ambience_volume": 0.04},
    {
        "key": "end_legacy",
        "source": None,
        "duration": 4.0,
        "card_text": "The Phoenician Legacy Lives On",
        "card_subtitle": "Bormla still stands at the heart of Maltese maritime memory.",
        "background_from": "shot11_modern_conservation.mp4",
        "ambience_volume": 0.0,
    },
]

EXTENDED_SEGMENTS: list[dict[str, object]] = [
    {"key": "intro_ocean", "source": "intro_ocean.mp4", "ambience_volume": 0.10},
    {"key": "shot01_trade_network_fleet", "source": "shot01_trade_network_fleet.mp4", "ambience_volume": 0.10},
    {"key": "insert_trade_goods_detail", "source": "insert_trade_goods_detail.mp4", "ambience_volume": 0.11},
    {"key": "shot02_hero_gaulos_ship", "source": "shot02_hero_gaulos_ship.mp4", "ambience_volume": 0.09},
    {"key": "insert_gaulos_broadside_hull", "source": "insert_gaulos_broadside_hull.mp4", "ambience_volume": 0.08},
    {"key": "shot03_harbor_approach", "source": "shot03_harbor_approach.mp4", "ambience_volume": 0.12},
    {"key": "shot04_quay_loading", "source": "shot04_quay_loading.mp4", "ambience_volume": 0.13},
    {"key": "shot05_marketplace_exchange", "source": "shot05_marketplace_exchange.mp4", "ambience_volume": 0.12},
    {"key": "shot06_ship_construction", "source": "shot06_ship_construction.mp4", "ambience_volume": 0.11},
    {"key": "shot07_trade_route_map", "source": "shot07_trade_route_map.mp4", "ambience_volume": 0.06},
    {"key": "insert_cultural_influence_map", "source": "insert_cultural_influence_map.mp4", "ambience_volume": 0.03},
    {"key": "shot08_bormla_repair", "source": "shot08_bormla_repair.mp4", "ambience_volume": 0.11},
    {"key": "shot09_night_navigation", "source": "shot09_night_navigation.mp4", "ambience_volume": 0.07},
    {"key": "shot10_underwater_shipwreck", "source": "shot10_underwater_shipwreck.mp4", "ambience_volume": 0.05},
    {"key": "shot11_modern_conservation", "source": "shot11_modern_conservation.mp4", "ambience_volume": 0.04},
    {
        "key": "end_legacy",
        "source": None,
        "duration": 4.0,
        "card_text": "The Phoenician Legacy Lives On",
        "card_subtitle": "Bormla still stands at the heart of Maltese maritime memory.",
        "background_from": "shot11_modern_conservation.mp4",
        "ambience_volume": 0.0,
    },
]


def select_segments(narration_path: Path) -> list[dict[str, object]]:
    cut_mode = os.environ.get("VIDEO_CUT_MODE", "").strip().lower()
    if cut_mode == "standard":
        return STANDARD_SEGMENTS
    if cut_mode == "extended":
        return EXTENDED_SEGMENTS
    if "extended" in narration_path.stem:
        return EXTENDED_SEGMENTS
    return STANDARD_SEGMENTS


def load_narration(path: Path) -> dict[str, str]:
    narration: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        key, text = line.split("|", 1)
        narration[key.strip()] = text.strip()
    return narration


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


def normalize_clip(ffmpeg: str, source: Path, output: Path) -> None:
    cmd = [
        ffmpeg,
        "-y",
        "-i",
        str(source),
        "-vf",
        (
            f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,"
            f"crop={WIDTH}:{HEIGHT},fps={FPS},format=yuv420p"
        ),
        "-an",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        str(output),
    ]
    run(cmd)


def extract_end_card_background(ffmpeg: str, source_clip: Path, output_image: Path) -> None:
    cmd = [
        ffmpeg,
        "-y",
        "-sseof",
        "-0.10",
        "-i",
        str(source_clip),
        "-frames:v",
        "1",
        str(output_image),
    ]
    run(cmd)


def build_end_card(
    ffmpeg: str,
    font: Path,
    output: Path,
    duration: float,
    title: str,
    subtitle: str,
    background_image: Path | None,
) -> None:
    font_file = font_arg(font)
    title_text = escape_drawtext(title)
    subtitle_text = escape_drawtext(subtitle)
    base_filters = [
        f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase",
        f"crop={WIDTH}:{HEIGHT}",
        "gblur=sigma=12",
        "eq=brightness=-0.10:saturation=0.82",
        f"drawbox=x=0:y={HEIGHT-210}:w={WIDTH}:h=210:color=black@0.40:t=fill",
        (
            f"drawtext=fontfile='{font_file}':text='{title_text}':"
            f"x=(w-text_w)/2:y=250:fontsize=50:fontcolor=white"
        ),
        (
            f"drawtext=fontfile='{font_file}':text='{subtitle_text}':"
            f"x=(w-text_w)/2:y=340:fontsize=28:fontcolor=white"
        ),
        f"fade=t=in:st=0:d=0.4",
        f"fade=t=out:st={max(duration - 0.5, 0.1):.2f}:d=0.4",
    ]

    if background_image and background_image.exists():
        cmd = [
            ffmpeg,
            "-y",
            "-loop",
            "1",
            "-i",
            str(background_image),
            "-t",
            f"{duration:.2f}",
            "-vf",
            ",".join(base_filters),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            str(output),
        ]
    else:
        cmd = [
            ffmpeg,
            "-y",
            "-f",
            "lavfi",
            "-i",
            f"color=c=#0f1822:s={WIDTH}x{HEIGHT}:r={FPS}:d={duration}",
            "-vf",
            ",".join(base_filters[-5:]),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            str(output),
        ]
    run(cmd)


async def synthesize_with_edge_tts(text: str, output: Path) -> None:
    import edge_tts

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate=VOICE_RATE,
        pitch=VOICE_PITCH,
    )
    await communicate.save(str(output))


def synthesize_with_windows_sapi(text: str, output: Path) -> None:
    powershell_script = f"""
Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$voiceNames = $s.GetInstalledVoices() | ForEach-Object {{ $_.VoiceInfo.Name }}
if ($voiceNames -contains 'Microsoft Zira Desktop') {{
  $s.SelectVoice('Microsoft Zira Desktop')
}} elseif ($voiceNames -contains 'Microsoft Hazel Desktop') {{
  $s.SelectVoice('Microsoft Hazel Desktop')
}}
$s.Rate = -1
$s.SetOutputToWaveFile('{output.resolve()}')
$s.Speak(@'
{text}
'@)
$s.Dispose()
"""
    completed = subprocess.run(
        ["powershell", "-NoProfile", "-Command", powershell_script],
        text=True,
        capture_output=True,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip())


def synthesize_with_flite(ffmpeg: str, text: str, output: Path) -> None:
    escaped = text.replace("\\", "\\\\").replace(":", r"\:").replace("'", r"\'")
    cmd = [
        ffmpeg,
        "-y",
        "-f",
        "lavfi",
        "-i",
        f"flite=text='{escaped}':voice=rms",
        "-ar",
        str(SAMPLE_RATE),
        str(output),
    ]
    run(cmd)


def synthesize_segment(ffmpeg: str, text: str, base_output: Path) -> Path:
    mp3_output = base_output.with_suffix(".mp3")
    wav_output = base_output.with_suffix(".wav")

    try:
        asyncio.run(synthesize_with_edge_tts(text, mp3_output))
        return mp3_output
    except Exception:
        if mp3_output.exists():
            mp3_output.unlink()

    if sys.platform.startswith("win"):
        synthesize_with_windows_sapi(text, wav_output)
        return wav_output

    synthesize_with_flite(ffmpeg, text, wav_output)
    return wav_output


def fit_audio_to_duration(ffmpeg: str, ffprobe: str, source: Path, output: Path, duration: float) -> None:
    source_duration = probe_duration(ffprobe, source)
    filters: list[str] = []
    if source_duration > duration:
        tempo = source_duration / duration
        filters.append(f"atempo={tempo:.5f}")
    filters.append(f"apad=pad_dur={duration + 0.5:.2f}")
    filters.append(f"atrim=0:{duration:.2f}")
    cmd = [
        ffmpeg,
        "-y",
        "-i",
        str(source),
        "-af",
        ",".join(filters),
        "-ar",
        str(SAMPLE_RATE),
        "-ac",
        "1",
        str(output),
    ]
    run(cmd)


def find_ambience_source(directory: Path, stem: str) -> Path | None:
    for extension in AMBIENCE_EXTENSIONS:
        candidate = directory / f"{stem}{extension}"
        if candidate.exists():
            return candidate
    return None


def find_music_bed(directory: Path) -> Path | None:
    for stem in ("bed", "documentary_bed", "ambient_bed"):
        found = find_ambience_source(directory, stem)
        if found:
            return found
    return None


def prepare_ambience_track(
    ffmpeg: str,
    source: Path,
    output: Path,
    duration: float,
    volume: float,
) -> None:
    fade_in = min(0.35, max(duration / 4, 0.1))
    fade_out = min(0.45, max(duration / 3, 0.1))
    fade_out_start = max(duration - fade_out, 0.0)
    filters = [
        f"volume={volume:.3f}",
        f"afade=t=in:st=0:d={fade_in:.2f}",
        f"afade=t=out:st={fade_out_start:.2f}:d={fade_out:.2f}",
        f"atrim=0:{duration:.2f}",
    ]
    cmd = [
        ffmpeg,
        "-y",
        "-stream_loop",
        "-1",
        "-i",
        str(source),
        "-t",
        f"{duration:.2f}",
        "-vn",
        "-af",
        ",".join(filters),
        "-ar",
        str(SAMPLE_RATE),
        "-ac",
        "1",
        str(output),
    ]
    run(cmd)


def mix_narration_and_ambience(ffmpeg: str, narration: Path, ambience: Path, output: Path) -> None:
    cmd = [
        ffmpeg,
        "-y",
        "-i",
        str(narration),
        "-i",
        str(ambience),
        "-filter_complex",
        "[0:a][1:a]amix=inputs=2:duration=first:dropout_transition=0,alimiter=limit=0.92[aout]",
        "-map",
        "[aout]",
        "-ar",
        str(SAMPLE_RATE),
        "-ac",
        "1",
        str(output),
    ]
    run(cmd)


def prepare_music_bed(ffmpeg: str, source: Path, output: Path, duration: float) -> None:
    fade_out = min(2.0, max(duration / 10, 1.0))
    fade_out_start = max(duration - fade_out, 0.0)
    filters = [
        f"volume={MUSIC_VOLUME:.3f}",
        "highpass=f=80",
        "lowpass=f=7000",
        "afade=t=in:st=0:d=1.2",
        f"afade=t=out:st={fade_out_start:.2f}:d={fade_out:.2f}",
        f"atrim=0:{duration:.2f}",
    ]
    cmd = [
        ffmpeg,
        "-y",
        "-stream_loop",
        "-1",
        "-i",
        str(source),
        "-t",
        f"{duration:.2f}",
        "-vn",
        "-af",
        ",".join(filters),
        "-ar",
        str(SAMPLE_RATE),
        "-ac",
        "1",
        str(output),
    ]
    run(cmd)


def mix_program_audio(ffmpeg: str, dry_mix: Path, music_bed: Path, output: Path) -> None:
    cmd = [
        ffmpeg,
        "-y",
        "-i",
        str(dry_mix),
        "-i",
        str(music_bed),
        "-filter_complex",
        "[0:a][1:a]amix=inputs=2:duration=first:dropout_transition=0,alimiter=limit=0.90[aout]",
        "-map",
        "[aout]",
        "-ar",
        str(SAMPLE_RATE),
        "-ac",
        "1",
        str(output),
    ]
    run(cmd)


def write_concat_file(path: Path, files: list[Path]) -> None:
    path.write_text(
        "\n".join(f"file '{file.resolve().as_posix()}'" for file in files) + "\n",
        encoding="utf-8",
    )


def format_srt_timestamp(seconds: float) -> str:
    total_ms = int(round(seconds * 1000))
    hours, rem = divmod(total_ms, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, millis = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def wrap_subtitle_text(text: str, width: int = 42) -> str:
    lines = textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)
    if len(lines) <= 2:
        return "\n".join(lines)
    return "\n".join([lines[0], " ".join(lines[1:])])


def write_srt(path: Path, rows: list[dict[str, object]]) -> None:
    lines: list[str] = []
    for index, row in enumerate(rows, start=1):
        lines.extend(
            [
                str(index),
                f"{format_srt_timestamp(float(row['start']))} --> {format_srt_timestamp(float(row['end']))}",
                wrap_subtitle_text(str(row["text"])),
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ffmpeg = find_ffmpeg()
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        raise FileNotFoundError("ffprobe is required but was not found in PATH")

    font = find_font()
    narration = load_narration(NARRATION_FILE)
    segments = select_segments(NARRATION_FILE)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    MIXED_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    AMBIENCE_DIR.mkdir(parents=True, exist_ok=True)
    MUSIC_DIR.mkdir(parents=True, exist_ok=True)

    video_parts: list[Path] = []
    audio_parts: list[Path] = []
    subtitle_rows: list[dict[str, object]] = []
    ambience_report: list[str] = []
    elapsed = 0.0

    for index, segment in enumerate(segments, start=1):
        key = str(segment["key"])
        text = narration.get(key)
        if not text:
            raise KeyError(f"Missing narration for segment '{key}' in {NARRATION_FILE}")

        video_output = VIDEO_DIR / f"{index:02d}_{key}.mp4"
        source_name = segment.get("source")
        if source_name:
            source = SELECTED_DIR / str(source_name)
            if not source.exists():
                raise FileNotFoundError(f"Missing selected clip: {source}")
            normalize_clip(ffmpeg, source, video_output)
            duration = probe_duration(ffprobe, video_output)
        else:
            duration = float(segment["duration"])
            background_image: Path | None = None
            background_source = segment.get("background_from")
            if background_source:
                source_clip = SELECTED_DIR / str(background_source)
                background_image = VIDEO_DIR / f"{index:02d}_{key}_background.png"
                extract_end_card_background(ffmpeg, source_clip, background_image)
            build_end_card(
                ffmpeg,
                font,
                video_output,
                duration,
                str(segment["card_text"]),
                str(segment["card_subtitle"]),
                background_image,
            )

        raw_audio = synthesize_segment(ffmpeg, text, AUDIO_DIR / f"{index:02d}_{key}_raw")
        fitted_narration = AUDIO_DIR / f"{index:02d}_{key}_narration.wav"
        fit_audio_to_duration(ffmpeg, ffprobe, raw_audio, fitted_narration, duration)

        final_audio = MIXED_AUDIO_DIR / f"{index:02d}_{key}.wav"
        ambience_source = find_ambience_source(AMBIENCE_DIR, key)
        ambience_volume = float(segment.get("ambience_volume", DEFAULT_AMBIENCE_VOLUME))
        if ambience_source and ambience_volume > 0:
            ambience_output = AUDIO_DIR / f"{index:02d}_{key}_ambience.wav"
            prepare_ambience_track(ffmpeg, ambience_source, ambience_output, duration, ambience_volume)
            mix_narration_and_ambience(ffmpeg, fitted_narration, ambience_output, final_audio)
            ambience_report.append(f"{key}: {ambience_source.name} at volume {ambience_volume:.2f}")
        else:
            shutil.copyfile(fitted_narration, final_audio)
            if ambience_source:
                ambience_report.append(f"{key}: skipped {ambience_source.name} because volume was 0")
            else:
                ambience_report.append(f"{key}: no ambience file found")

        video_parts.append(video_output)
        audio_parts.append(final_audio)
        subtitle_rows.append(
            {
                "start": elapsed,
                "end": elapsed + duration,
                "text": text,
            }
        )
        elapsed += duration

    video_concat = OUTPUT_DIR / "video_concat.txt"
    audio_concat = OUTPUT_DIR / "audio_concat.txt"
    write_concat_file(video_concat, video_parts)
    write_concat_file(audio_concat, audio_parts)

    silent_video = OUTPUT_DIR / "phoenician_pdf_documentary_silent.mp4"
    voice_ambience_audio = OUTPUT_DIR / "phoenician_pdf_documentary_voice_ambience.wav"
    narration_audio = OUTPUT_DIR / "phoenician_pdf_documentary_narration.wav"
    subtitle_path = OUTPUT_DIR / "phoenician_pdf_documentary.srt"
    ambience_report_path = OUTPUT_DIR / "ambience_report.txt"
    music_report_path = OUTPUT_DIR / "music_report.txt"
    final_video = OUTPUT_DIR / "phoenician_pdf_documentary_subtitled.mp4"

    run(
        [
            ffmpeg,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(video_concat),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            str(silent_video),
        ]
    )

    run(
        [
            ffmpeg,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(audio_concat),
            "-ar",
            str(SAMPLE_RATE),
            "-ac",
            "1",
            str(voice_ambience_audio),
        ]
    )

    music_bed_source = find_music_bed(MUSIC_DIR)
    if music_bed_source:
        prepared_music = AUDIO_DIR / "music_bed_prepared.wav"
        prepare_music_bed(ffmpeg, music_bed_source, prepared_music, elapsed)
        mix_program_audio(ffmpeg, voice_ambience_audio, prepared_music, narration_audio)
        music_report_path.write_text(
            f"music bed: {music_bed_source.name} at volume {MUSIC_VOLUME:.3f}\n",
            encoding="utf-8",
        )
    else:
        shutil.copyfile(voice_ambience_audio, narration_audio)
        music_report_path.write_text("music bed: none\n", encoding="utf-8")

    ambience_report_path.write_text("\n".join(ambience_report) + "\n", encoding="utf-8")
    write_srt(subtitle_path, subtitle_rows)

    subtitle_arg = subtitle_path.resolve().as_posix().replace(":", r"\:")
    run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(silent_video),
            "-i",
            str(narration_audio),
            "-vf",
            f"subtitles='{subtitle_arg}'",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            str(final_video),
        ]
    )

    print(final_video)
    print(narration_audio)
    print(subtitle_path)
    print(ambience_report_path)
    print(music_report_path)


if __name__ == "__main__":
    main()
