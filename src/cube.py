import matplotlib.colors as mcolors
import numpy as np
from mypiece import Orientation, check_valid_orienation, validate_origin, Piece
from coordhelper import CoordinateHelper

class Cube():
    # Some parameters for how to pretty-print
    _print_divider = "  |  "
    _print_divider_foot = "__|__"
    _print_cell_width = 8

    def __init__(self, side_len):
        if side_len < 1:
            raise ValueError("side_len")

        self._listpieces = set()
        self._side_len = side_len

        self._empty_cube()

    def _empty_cube(self):
        self._cube_values = np.full((self._side_len, self._side_len, self._side_len),
            "",
            dtype=np.dtype('U50'))

    def _is_xyz_within_cube(self, x, y, z):
        if x < 0 or x >= self._side_len:
            return False

        if y < 0 or y >= self._side_len:
            return False

        if z < 0 or z >= self._side_len:
            return False
        
        return True

    def _is_coord_within_cube(self, coord):
        if not validate_origin(coord):
            raise TypeError("Invalid coordinate")

        x = coord[0]
        y = coord[1]
        z = coord[2]

        return self._is_xyz_within_cube(x, y, z)

    def _get_color(self, x, y, z):
        if not self._is_xyz_within_cube(x, y, z):
            raise ValueError("Invalid xyz")
        return self._cube_values[x, y, z]

    def _set_color(self, x, y, z, color):
        if not self._is_xyz_within_cube(x, y, z):
            raise ValueError("Invalid xyz")
        self._cube_values[x, y, z] = color

    # Returns False if the piece cant be placed there
    def try_place_piece(self, piece, origin, orientation):
        if not check_valid_orienation(orientation):
            raise TypeError("Invalidid orientation")

        if not validate_origin(origin):
            raise TypeError("Invalid origin")

        if piece in self._listpieces:
            raise ValueError("That piece is already placed")

        piece_coords = CoordinateHelper.GetIndividualPieceCoordinates(
            piece,
            origin,
            orientation)

        # Check to see if piece fits fully within the cube
        for piece_coord in piece_coords:
            if not self._is_coord_within_cube(piece_coord.loc):
                return False

            if self._get_color(
                piece_coord.loc[0],
                piece_coord.loc[1],
                piece_coord.loc[2]) != "":
                return False

        # Place the piece
        for piece_coord in piece_coords:
            self._set_color(
                piece_coord.loc[0],
                piece_coord.loc[1],
                piece_coord.loc[2],
                piece_coord.color)

        self._listpieces.add(piece)

        return True        

    def _print_header(self):
        return "_" * ((self._side_len * self._side_len * Cube._print_cell_width)
            + len(Cube._print_divider) * 2) + "\n"

    def _print_emptyrow(self):
        result = ""
        for z in range(0, self._side_len - 1):
            result = result + " " * (Cube._print_cell_width * self._side_len)
            result = result + Cube._print_divider

        result = result + "\n"
        return result

    def _print_footer(self):
        result = ""
        for z in range(0, self._side_len):
            result = result + "_" * (Cube._print_cell_width * self._side_len)
            if (z != self._side_len - 1):
                result = result + Cube._print_divider_foot

        return result

    def _print_cube_row(self, row, z):
        result = ""
        for x in range(0, self._side_len):
            color = self._cube_values[x, row, z]
            color = "." if (color == "") else color
            result = result + \
                color[0:Cube._print_cell_width].ljust(Cube._print_cell_width)
        return result

    def _print_all_rows(self, row):
        result = ""
        for z in range(0, self._side_len):
            result = result + self._print_cube_row(row, z)
            if (z != self._side_len - 1):
                result = result + Cube._print_divider
        return result

    def __str__(self):
        result = self._print_header()
        result = result + self._print_emptyrow()
        for y in range(0, self._side_len):
            result = result + self._print_all_rows(y)
            if (y != self._side_len - 1):
                result = result + "\n" + self._print_emptyrow()

        result = result + "\n" + self._print_footer()
        return result
