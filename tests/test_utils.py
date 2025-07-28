"""
build123d Helper Utilities tests

name: test_utils.py
by:   jwagenet
date: July 28th 2025

desc: Unit tests for the build123d helper utilities module
"""

import unittest

from build123d import *
from build123d.utils import FontInfo


class TestFontHelpers(unittest.TestCase):
    """Tests for font helpers."""

    def test_available_fonts(self):
        """Test expected output for available fonts."""
        fonts = available_fonts()
        self.assertIsInstance(fonts, list)
        for font in fonts:
            self.assertIsInstance(font, FontInfo)
            self.assertIsInstance(font.name, str)
            self.assertIsInstance(font.styles, tuple)
            for style in font.styles:
                self.assertIsInstance(style, FontStyle)

        names = [font.name for font in fonts]
        self.assertEqual(names, sorted(names))


if __name__ == "__main__":
    unittest.main()
