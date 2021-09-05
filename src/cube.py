import matplotlib.colors as mcolors
import numpy as np
from mypiece import Orientation, check_valid_orienation, validate_origin, Piece
from coordhelper import CoordinateHelper
from print_cube import CubePrettyPrinter

class Cube():
    def __init__(self, side_len):
        if side_len < 1:
            raise ValueError("side_len")

        self.__side_len = side_len
        self.clear()

        self.__pp = CubePrettyPrinter(side_len)

    def clear(self):
        self.__listpieces = {}

        self.__cube_values = np.full((self.__side_len, self.__side_len, self.__side_len),
            "",
            dtype=np.dtype('U50'))

        self.__count_pieces = 0

    def __is_xyz_within_cube(self, x, y, z):
        if x < 0 or x >= self.__side_len:
            return False

        if y < 0 or y >= self.__side_len:
            return False

        if z < 0 or z >= self.__side_len:
            return False
        
        return True

    def __is_coord_within_cube(self, coord):
        if not validate_origin(coord):
            raise TypeError("Invalid coordinate")

        x = coord[0]
        y = coord[1]
        z = coord[2]

        return self.__is_xyz_within_cube(x, y, z)

    def __get_color(self, x, y, z):
        if not self.__is_xyz_within_cube(x, y, z):
            raise ValueError("Invalid xyz")
        return self.__cube_values[x, y, z]

    def __set_color(self, x, y, z, color):
        if not self.__is_xyz_within_cube(x, y, z):
            raise ValueError("Invalid xyz")
        self.__cube_values[x, y, z] = color

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)

        # We want a shallow copy of __listpieces and __cube_values, so that this cube's copy can have different pieces added/removed
        # However, we can't just do a deepcopy of __listpieces, since we don't want the pieces themselves to be new objects
        result.__listpieces = self.__listpieces.copy()
        result.__cube_values = self.__cube_values.copy()

        return result

    def __eq__(self, other):
        if not isinstance(other, Cube):
            # Don't attempt to compare against unrelated types
            return NotImplemented

        # Note: __listpieces can be compared easily since it's a Dictionary, and order doesn't matter
        return (self.__side_len == other.__side_len) and \
            (np.array_equal(self.__cube_values, other.__cube_values)) and \
            (self.__listpieces.keys() == other.__listpieces.keys())

    # Returns False if the piece cant be placed there
    def try_place_piece(self, piece, origin, orientation):
        if not check_valid_orienation(orientation):
            raise TypeError("Invalidid orientation")

        if not validate_origin(origin):
            raise TypeError("Invalid origin")

        if piece in self.__listpieces.keys():
            raise ValueError("That piece is already placed")

        self.__sanity_check_piece_count()

        piece_coords = CoordinateHelper.GetIndividualPieceCoordinates(
            piece,
            origin,
            orientation)

        # Check to see if piece fits fully within the cube
        for piece_coord in piece_coords:
            if not self.__is_coord_within_cube(piece_coord.loc):
                return False

            if self.__get_color(
                piece_coord.loc[0],
                piece_coord.loc[1],
                piece_coord.loc[2]) != "":
                return False

        # Place the piece
        for piece_coord in piece_coords:
            self.__set_color(
                piece_coord.loc[0],
                piece_coord.loc[1],
                piece_coord.loc[2],
                piece_coord.color)

        # In the list of Pieces, you can quickly lookup origin and orientation where piece was placed in the cube
        self.__listpieces[piece] = (origin, orientation)
        self.__count_pieces = self.__count_pieces + 1
        self.__sanity_check_piece_count()

        return True

    def remove_piece(self, piece):
        if not piece in self.__listpieces.keys():
            raise ValueError("That piece isnt in the cube")

        self.__sanity_check_piece_count()

        # Clear all the elements in the Cube for this piece
        origin, orientation = self.__listpieces[piece]
        piece_coords = CoordinateHelper.GetIndividualPieceCoordinates(
            piece,
            origin,
            orientation)

        for piece_coord in piece_coords:
            # Double-check that expected color is where it should be as we remove it
            assert self.__get_color(
                piece_coord.loc[0],
                piece_coord.loc[1],
                piece_coord.loc[2]) == piece_coord.color

            self.__set_color(
                piece_coord.loc[0],
                piece_coord.loc[1],
                piece_coord.loc[2],
                "")

        del self.__listpieces[piece]
        self.__count_pieces = self.__count_pieces - 1
        self.__sanity_check_piece_count()

    def __count_individual_pieces(self):
        return np.count_nonzero(self.__cube_values != "")

    @property
    def is_empty(self):
        self.__sanity_check_piece_count()
        return self.__count_individual_pieces() == 0

    @property
    def is_full(self):
        self.__sanity_check_piece_count()
        return self.__count_individual_pieces() == self.__side_len**3

    def __str__(self):
        return self.__pp.pretty_print_cube(self.__cube_values)

    def __sanity_check_piece_count(self):
        assert (self.__count_pieces >= 0) and (self.__count_pieces <= self.__side_len**3)
        assert self.__count_pieces == len(self.__listpieces.keys())
