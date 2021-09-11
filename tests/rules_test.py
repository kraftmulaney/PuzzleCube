import unittest
import numpy as np
from .context import Piece, Orientation, Cube, CheckIfCubeFull
from copy import copy

class FullCubeTests(unittest.TestCase):
    def test_empty_cube_shouldnt_return_isfull(self):
        colors = np.array(['blue', 'yellow'])

        cube = Cube(side_len = 3)

        rule = CheckIfCubeFull(cube)
        result = rule.check_cube()

        self.assertTrue(not result)

    def test_partially_filled_cube_shouldnt_return_is_full(self):
        colors = np.array(['red', 'white', 'blue'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        rule = CheckIfCubeFull(cube)
        result = rule.check_cube()

        self.assertTrue(not result)

    def test_full_cube_should_return_is_full(self):
        colors = np.array(['blue', 'white'])

        piece1 = Piece(colors)
        piece2 = Piece(colors)
        piece3 = Piece(colors)
        piece4 = Piece(colors)
        cube = Cube(side_len = 2)

        self.assertTrue(cube.try_place_piece(piece1,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(cube.try_place_piece(piece2,
            origin = np.array([0, 0, 1]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(cube.try_place_piece(piece3,
            origin = np.array([0, 1, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(cube.try_place_piece(piece4,
            origin = np.array([0, 1, 1]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        rule = CheckIfCubeFull(cube)
        result = rule.check_cube()

        self.assertTrue(result)
