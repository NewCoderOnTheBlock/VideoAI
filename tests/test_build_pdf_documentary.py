from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from build_pdf_documentary import (
    find_ambience_source,
    format_srt_timestamp,
    load_narration,
    wrap_subtitle_text,
)


class BuildPdfDocumentaryTests(unittest.TestCase):
    def test_format_srt_timestamp(self) -> None:
        self.assertEqual(format_srt_timestamp(0.0), "00:00:00,000")
        self.assertEqual(format_srt_timestamp(65.432), "00:01:05,432")

    def test_load_narration_skips_comments(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "narration.txt"
            source.write_text(
                "# comment\n\nintro|Opening line.\nshot01|Fleet line.\n",
                encoding="utf-8",
            )
            self.assertEqual(
                load_narration(source),
                {
                    "intro": "Opening line.",
                    "shot01": "Fleet line.",
                },
            )

    def test_find_ambience_source_matches_supported_extension(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "shot03_harbor_approach.mp3"
            target.write_bytes(b"fake")
            self.assertEqual(find_ambience_source(Path(temp_dir), "shot03_harbor_approach"), target)

    def test_wrap_subtitle_text_prefers_two_lines(self) -> None:
        wrapped = wrap_subtitle_text(
            "Shipwrecks near Malta still preserve amphorae, anchors, and cargo that prove this maritime system."
        )
        self.assertIn("\n", wrapped)
        self.assertLessEqual(len(wrapped.splitlines()), 2)


if __name__ == "__main__":
    unittest.main()
