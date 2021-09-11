import unittest
import numpy as np
from .context import Piece, Orientation, Cube
from copy import copy

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

    def test_place_similar_but_separate_piece_twice_should_succeed(self):
        colors = np.array(['blue'])

        piece1 = Piece(colors)
        piece2 = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece1,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        # Even though the two pieces look the same, we should be able to insert both into the Cube
        self.assertTrue(cube.try_place_piece(piece2,
            origin = np.array([0, 1, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

    def test_new_cube_should_be_empty(self):
        cube = Cube(side_len = 3)
        self.assertTrue(cube.is_empty)

    def test_cube_should_not_be_empty_after_adding_piece(self):
        colors = np.array(['red', 'white', 'blue'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(not cube.is_empty)

    def test_clear_cube_should_succeed(self):
        colors = np.array(['red', 'white', 'blue'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        cube.clear()

        self.assertTrue(cube.is_empty)

    def test_adding_piece_after_clearing_cube_should_succeed(self):
        colors = np.array(['red', 'white', 'blue'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        cube.clear()
        self.assertTrue(cube.is_empty)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

    def test_new_cube_should_not_be_full(self):
        cube = Cube(side_len = 3)
        self.assertTrue(not cube.is_full)

    def test_partially_filled_cube_should_not_be_full(self):
        colors = np.array(['red', 'white', 'blue'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(not cube.is_full)

    def test_full_cube_should_be_full(self):
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

        self.assertTrue(cube.is_full)

    def test_removing_piece_not_in_cube_should_fail(self):
        colors1 = np.array(['red', 'white', 'blue'])
        colors2 = np.array(['blue'])

        piece1 = Piece(colors1)
        piece2 = Piece(colors2)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece1,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        with self.assertRaises(ValueError):
            cube.remove_piece(piece2)

    def test_removing_piece_in_cube_should_succeed(self):
        colors = np.array(['red', 'white', 'blue'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        cube.remove_piece(piece)

    def test_remove_single_piece_should_leave_cube_empty(self):
        colors = np.array(['red', 'white', 'blue'])

        piece = Piece(colors)
        cube = Cube(side_len = 3)
        cube_copy = copy(cube)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        cube.remove_piece(piece)
        self.assertTrue(cube.is_empty)
        self.assertTrue(cube == cube_copy)

    def test_remove_piece_from_full_cubeshould_leave_nonfull_cube(self):
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

            self.assertTrue(cube.is_full)

            cube.remove_piece(piece1)
            self.assertTrue(not cube.is_full)

    def test_remove_piece_after_cloning_should_result_in_equal_cubes(self):
        colors1 = np.array(['red', 'white', 'blue'])
        colors2 = np.array(['blue'])

        piece1 = Piece(colors1)
        piece2 = Piece(colors2)
        cube = Cube(side_len = 3)

        self.assertTrue(cube.try_place_piece(piece1,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        cube_copy = copy(cube)

        self.assertTrue(cube.try_place_piece(piece2,
            origin = np.array([0, 1, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(cube != cube_copy)
        cube.remove_piece(piece2)
        self.assertTrue(cube == cube_copy)
