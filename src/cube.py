import matplotlib.colors as mcolors
import numpy as np
from mypiece import Orientation, check_valid_orienation, validate_origin, Piece
from coordhelper import CoordinateHelper

class Cube():
    # Some parameters for how to pretty-print
    __print_divider = "  |  "
    __print_divider_footer = "__|__"
    __print_cell_width = 8

    def __init__(self, side_len):
        if side_len < 1:
            raise ValueError("side_len")

        self.__listpieces = set()
        self.__side_len = side_len

        self.__empty_cube()

    def __empty_cube(self):
        self.__cube_values = np.full((self.__side_len, self.__side_len, self.__side_len),
            "",
            dtype=np.dtype('U50'))

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

        # Note: __listpieces can be compared easily since it's a Set, and order doesn't matter
        return (self.__side_len == other.__side_len) and \
            (np.array_equal(self.__cube_values, other.__cube_values)) and \
            (self.__listpieces == other.__listpieces)

    # Returns False if the piece cant be placed there
    def try_place_piece(self, piece, origin, orientation):
        if not check_valid_orienation(orientation):
            raise TypeError("Invalidid orientation")

        if not validate_origin(origin):
            raise TypeError("Invalid origin")

        if piece in self.__listpieces:
            raise ValueError("That piece is already placed")

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

        # $TODO Note that I'm not yet storing the position or orientation of a piece.  So supporting "remove piece" is impossible
        self.__listpieces.add(piece)

        return True

    # $TODO Move pretty print into its own class
    def __print_header(self):
        return "_" * ((self.__side_len * self.__side_len * Cube.__print_cell_width)
            + len(Cube.__print_divider) * 2) + "\n"

    def __print_emptyrow(self):
        result = ""
        for z in range(0, self.__side_len - 1):
            result = result + " " * (Cube.__print_cell_width * self.__side_len)
            result = result + Cube.__print_divider

        result = result + "\n"
        return result

    def __print_footer(self):
        result = ""
        for z in range(0, self.__side_len):
            result = result + "_" * (Cube.__print_cell_width * self.__side_len)
            if (z != self.__side_len - 1):
                result = result + Cube.__print_divider_footer

        return result

    def __print_cube_row(self, row, z):
        result = ""
        for x in range(0, self.__side_len):
            color = self.__cube_values[x, row, z]
            color = "." if (color == "") else color
            result = result + \
                color[0:Cube.__print_cell_width].ljust(Cube.__print_cell_width)
        return result

    def __print_all_rows(self, row):
        result = ""
        for z in range(0, self.__side_len):
            result = result + self.__print_cube_row(row, z)
            if (z != self.__side_len - 1):
                result = result + Cube.__print_divider
        return result

    def __str__(self):
        result = self.__print_header()
        result = result + self.__print_emptyrow()
        for y in range(0, self.__side_len):
            result = result + self.__print_all_rows(y)
            if (y != self.__side_len - 1):
                result = result + "\n" + self.__print_emptyrow()

        result = result + "\n" + self.__print_footer()
        return result
