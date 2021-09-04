import unittest
import numpy as np
from .context import Piece, Orientation, Cube, CoordinateHelper, CoordinateOfPiece


class CoordinateHelperTests(unittest.TestCase):
    def __compare_coord_lists(self, list1, list2):
        if len(list1) != len(list2):
            return False

        for i1, i2 in zip(list1, list2):
            if i1 != i2:
                return False

        return True

    def __place_piece_helper(self, piece, origin, orientation, expected_result):
        piece_coords = CoordinateHelper.GetIndividualPieceCoordinates(piece,
            origin,
            orientation)

        self.assertTrue(self.__compare_coord_lists(piece_coords, expected_result))

    def test_place_small_piece_should_succeed(self):
        self.__place_piece_helper(
             piece  = Piece(np.array(['blue'])),
             origin = np.array([0, 0, 0]),
             orientation = Orientation.TOWARDS_XPOSITIVE,
             expected_result = [CoordinateOfPiece(np.array([0 ,0, 0]), 'blue')])

    def test_place_piece_xpos_should_succeed(self):
        self.__place_piece_helper(
             piece  = Piece(np.array(['red', 'white', 'blue'])),
             origin = np.array([1, 1, 1]),
             orientation = Orientation.TOWARDS_XPOSITIVE,
             expected_result = 
             [
                 CoordinateOfPiece(np.array([1, 1, 1]), 'red'),
                 CoordinateOfPiece(np.array([2, 1, 1]), 'white'),
                 CoordinateOfPiece(np.array([3, 1, 1]), 'blue')
             ])

    def test_place_piece_xneg_should_succeed(self):
        self.__place_piece_helper(
             piece  = Piece(np.array(['red', 'white', 'blue'])),
             origin = np.array([1, 1, 1]),
             orientation = Orientation.TOWARDS_XNEGATIVE,
             expected_result = 
             [
                 CoordinateOfPiece(np.array([1,  1, 1]), 'red'),
                 CoordinateOfPiece(np.array([0,  1, 1]), 'white'),
                 CoordinateOfPiece(np.array([-1, 1, 1]), 'blue')
             ])

    def test_place_piece_ypos_should_succeed(self):
        self.__place_piece_helper(
             piece  = Piece(np.array(['red', 'white', 'blue'])),
             origin = np.array([1, 1, 1]),
             orientation = Orientation.TOWARDS_YPOSITIVE,
             expected_result = 
             [
                 CoordinateOfPiece(np.array([1, 1, 1]), 'red'),
                 CoordinateOfPiece(np.array([1, 2, 1]), 'white'),
                 CoordinateOfPiece(np.array([1, 3, 1]), 'blue')
             ])

    def test_place_piece_yneg_should_succeed(self):
        self.__place_piece_helper(
             piece  = Piece(np.array(['red', 'white', 'blue'])),
             origin = np.array([1, 1, 1]),
             orientation = Orientation.TOWARDS_YNEGATIVE,
             expected_result = 
             [
                 CoordinateOfPiece(np.array([1, 1, 1]), 'red'),
                 CoordinateOfPiece(np.array([1, 0, 1]), 'white'),
                 CoordinateOfPiece(np.array([1, -1, 1]), 'blue')
             ])

    def test_place_piece_zpos_should_succeed(self):
        self.__place_piece_helper(
             piece  = Piece(np.array(['red', 'white', 'blue'])),
             origin = np.array([1, 1, 1]),
             orientation = Orientation.TOWARDS_ZPOSITIVE,
             expected_result = 
             [
                 CoordinateOfPiece(np.array([1, 1, 1]), 'red'),
                 CoordinateOfPiece(np.array([1, 1, 2]), 'white'),
                 CoordinateOfPiece(np.array([1, 1, 3]), 'blue')
             ])

    def test_place_piece_zneg_should_succeed(self):
        self.__place_piece_helper(
             piece  = Piece(np.array(['red', 'white', 'blue'])),
             origin = np.array([1, 1, 1]),
             orientation = Orientation.TOWARDS_ZNEGATIVE,
             expected_result = 
             [
                 CoordinateOfPiece(np.array([1, 1, 1]), 'red'),
                 CoordinateOfPiece(np.array([1, 1, 0]), 'white'),
                 CoordinateOfPiece(np.array([1, 1, -1]), 'blue')
             ])
