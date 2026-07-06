from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import render_support


class RenderSupportTests(unittest.TestCase):
    def test_escape_drawtext_escapes_reserved_characters(self) -> None:
        value = r"Harbor: captain's \ log"
        self.assertEqual(
            render_support.escape_drawtext(value),
            r"Harbor\: captain\'s \\ log",
        )

    def test_font_arg_escapes_windows_drive_separator(self) -> None:
        self.assertEqual(
            render_support.font_arg(Path("C:/Windows/Fonts/georgia.ttf")),
            r"C\:/Windows/Fonts/georgia.ttf",
        )

    def test_find_font_prefers_environment_override(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            font_path = Path(temp_dir) / "custom.ttf"
            font_path.write_text("stub", encoding="utf-8")
            with patch.dict("os.environ", {"VIDEOAI_FONT": str(font_path)}, clear=False):
                self.assertEqual(render_support.find_font(), font_path)


if __name__ == "__main__":
    unittest.main()
