import unittest
import numpy as np
from .context import Piece

class PieceTests(unittest.TestCase):
    def test_get_colors_should_succeed(self):
        colors = np.array(['blue', 'yellow'])

        piece = Piece(colors)
        self.assertTrue(np.array_equal(piece.colors, np.copy(colors)))

    def test_too_few_colors_should_fail(self):
        colors = np.array([])

        with self.assertRaises(ValueError):
            piece = Piece(colors)

    def test_invalid_color_should_fail(self):
        colors = np.array(['blue', 'yellowwwww'])

        with self.assertRaises(ValueError):
            piece = Piece(colors)
