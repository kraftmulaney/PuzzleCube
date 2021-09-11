import unittest
import numpy as np
from .context import Piece, Orientation, Cube
from copy import copy

class CopyTests(unittest.TestCase):
    def test_copy_empty_cube_should_be_equal(self):
        cube = Cube(side_len = 2)
        cubecopy = copy(cube)

        self.assertTrue(cube == cubecopy)

    def test_empty_cubes_of_different_sizes_should_be_unequal(self):
        cube1 = Cube(side_len = 2)
        cube2 = Cube(side_len = 4)

        self.assertTrue(cube1 != cube2)

    def test_copy_cube__with_one_piece_should_be_equal(self):
        piece = Piece(np.array(['blue']))
        cube = Cube(side_len = 2)

        self.assertTrue(cube.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        cubecopy = copy(cube)
        self.assertTrue(cube == cubecopy)

    def test_cubes_with_two_identical_pieces_added_separately_should_be_equal(self):
        piece = Piece(np.array(['blue', 'white']))

        cube1 = Cube(side_len = 3)
        self.assertTrue(cube1.try_place_piece(piece,
            origin = np.array([1, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        cube2 = Cube(side_len = 3)
        self.assertTrue(cube2.try_place_piece(piece,
            origin = np.array([1, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(cube1 == cube2)

    def test_cubes_with_two_identical_pieces_but_in_different_locations_should_be_unequal(self):
        piece = Piece(np.array(['blue', 'white']))

        cube1 = Cube(side_len = 2)
        self.assertTrue(cube1.try_place_piece(piece,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        cube2 = Cube(side_len = 2)
        self.assertTrue(cube2.try_place_piece(piece,
            origin = np.array([0, 1, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(cube1 != cube2)

    def test_cubes_with_two_pieces_added_in_different_order_should_be_equal(self):
        piece1 = Piece(np.array(['blue']))
        piece2 = Piece(np.array(['white']))

        # First, place the two pieces in order: 1 then 2
        cube1 = Cube(side_len = 2)
        self.assertTrue(cube1.try_place_piece(piece1,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))
        self.assertTrue(cube1.try_place_piece(piece2,
            origin = np.array([1, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        # Now, place the two pieces in order: 2 then 1
        cube2 = Cube(side_len = 2)
        self.assertTrue(cube2.try_place_piece(piece2,
            origin = np.array([1, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))
        self.assertTrue(cube2.try_place_piece(piece1,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(cube1 == cube2)

    def test_cubes_with_two_identical_but_separate_pieces_should_be_unequal(self):
        piece_identical1 = Piece(np.array(['blue', 'white']))
        piece_identical2 = Piece(np.array(['blue', 'white']))

        cube1 = Cube(side_len = 3)
        self.assertTrue(cube1.try_place_piece(piece_identical1,
            origin = np.array([1, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        print(cube1._Cube__listpieces)

        cube2 = Cube(side_len = 3)
        self.assertTrue(cube2.try_place_piece(piece_identical2,
            origin = np.array([1, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(cube1 != cube2)

    def test_cubes_with_identical_grid_of_colors_but_different_pieces_should_be_unequal(self):
        piece1 = Piece(np.array(['blue']))
        piece2 = Piece(np.array(['white']))
        piece_1and2 = Piece(np.array(['blue', 'white']))

        # Cube1 will have two small pieces placed separately 
        cube1 = Cube(side_len = 3)
        self.assertTrue(cube1.try_place_piece(piece1,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))
        self.assertTrue(cube1.try_place_piece(piece2,
            origin = np.array([1, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        # Cube2 will have one larger piece, that is the combination of piece1 and piece2 
        cube2 = Cube(side_len = 3)
        self.assertTrue(cube2.try_place_piece(piece_1and2,
            origin = np.array([0, 0, 0]),
            orientation = Orientation.TOWARDS_XPOSITIVE))

        self.assertTrue(cube1 != cube2)
