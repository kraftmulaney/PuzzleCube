import unittest
import numpy as np
from .context import Piece, Orientation, Cube

class CubeTests(unittest.TestCase):
    def test_create_cube_should_succeed(self):
        cube = Cube(side_len = 3)

    def test_create_cube_bogus_sidelen_should_fail(self):
        with self.assertRaises(ValueError):
            cube = Cube(side_len = -1)

    def test_place_small_piece_inbounds_should_succeed(self):
        colors = np.array(['red'])

        piece = Piece(colors)
        cube = Cube(side_len = 1)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

    def test_place_piece_inbounds_should_succeed(self):
        colors = np.array(['red', 'white', 'blue'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

    def test_place_piece_too_long_should_fail(self):
        colors = np.array(['red', 'white', 'blue', 'red'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(not cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

    def test_place_piece_out_of_bounds_should_fail(self):
        colors = np.array(['red', 'white', 'blue'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(not cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XNEGATIVE))

    def test_place_two_nonoverlapping_pieces_should_succeed(self):
        colors = np.array(['red', 'white', 'blue'])

        piece1 = Piece(colors)
        piece2 = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece1,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        # Not overlapping
        self.assertTrue(cube.try_place_piece(piece2,
            origin = np.array([0, 1, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

    def test_place_overlapping_piece_should_fail(self):
        colors = np.array(['red', 'white', 'blue'])

        piece1 = Piece(colors)
        piece2 = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece1,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        # This should fail since overlapping
        self.assertTrue(not cube.try_place_piece(piece2,
            origin = np.array([0, 2, 0]),
            orientation = Orientation.TOWARDS_YNEGATIVE))

    def test_place_overlapping_sameorigin_should_fail(self):
        colors = np.array(['blue'])

        piece1 = Piece(colors)
        piece2 = Piece(colors)
        cube = Cube(side_len = 1)

        self.assertTrue(cube.try_place_piece(piece1,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        # This should fail since overlapping
        self.assertTrue(not cube.try_place_piece(piece2,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

    def test_place_same_piece_twice_should_fail(self):
        colors = np.array(['red', 'white', 'blue'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        # Not overlapping, but cant place same piece twice
        with self.assertRaises(ValueError):
            cube.try_place_piece(piece,
                origin = np.array([0, 1, 0]),
                orientation = Orientation.TOWARDS_XPOSITIVE)
