from pathlib import Path

from build_pdf_documentary import find_ambience_source, format_srt_timestamp, load_narration


def test_format_srt_timestamp() -> None:
    assert format_srt_timestamp(0.0) == "00:00:00,000"
    assert format_srt_timestamp(65.432) == "00:01:05,432"


def test_load_narration_skips_comments(tmp_path: Path) -> None:
    source = tmp_path / "narration.txt"
    source.write_text(
        "# comment\n\nintro|Opening line.\nshot01|Fleet line.\n",
        encoding="utf-8",
    )
    assert load_narration(source) == {
        "intro": "Opening line.",
        "shot01": "Fleet line.",
    }


def test_find_ambience_source_matches_supported_extension(tmp_path: Path) -> None:
    target = tmp_path / "shot03_harbor_approach.mp3"
    target.write_bytes(b"fake")
    assert find_ambience_source(tmp_path, "shot03_harbor_approach") == target
