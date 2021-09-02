import matplotlib.colors as mcolors
import numpy as np
from mypiece import Orientation, check_valid_orienation, validate_origin, Piece
from coordhelper import CoordinateHelper

class Cube():
    def __init__(self, dx, dy, dz):
        if dx < 1:
            raise ValueError("dx")

        if dy < 1:
            raise ValueError("dy")

        if dz < 1:
            raise ValueError("dz")

        self._listpieces = set()
        self._dx = dx
        self._dy = dy
        self._dz = dz

        self._empty_cube()

    def _empty_cube(self):
        _cube_values = np.full((self._dx, self._dy, self._dx),
            "",
            dtype=np.dtype('U50'))

    def _is_coord_within_cube(self, coord):
        if not validate_origin(coord):
            raise TypeError("Invalid coordinate")

        x = coord[0]
        y = coord[1]
        z = coord[2]

        if x < 0 or x >= self._dx:
            return False

        if y < 0 or y >= self._dy:
            return False

        if z < 0 or z >= self._dz:
            return False
        
        return True

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

        # Place the piece
        # $TODO

        self._listpieces.add(piece)

        return True        
