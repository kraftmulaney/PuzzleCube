import matplotlib.colors as mcolors
import numpy as np
from mypiece import Orientation, check_valid_orienation, validate_origin, Piece

class CoordinateOfPiece():
    def __init__(self, loc, color):
        self.loc = loc
        self.color = color

    def __eq__(self, other):
        if not isinstance(other, CoordinateOfPiece):
            # Don't attempt to compare against unrelated types
            return NotImplemented

        return np.array_equal(self.loc, other.loc) and self.color == other.color

# Static class
class CoordinateHelper():
    to_vector = {
        Orientation.TOWARDS_XPOSITIVE: [1,  0,  0],
        Orientation.TOWARDS_XNEGATIVE: [-1, 0,  0],
        Orientation.TOWARDS_YPOSITIVE: [0,  1,  0],
        Orientation.TOWARDS_YNEGATIVE: [0, -1,  0],
        Orientation.TOWARDS_ZPOSITIVE: [0,  0,  1],
        Orientation.TOWARDS_ZNEGATIVE: [0,  0, -1]
    }

    # Returns a list of tuples: coordinate, and the color at that coordinate
    # NOTE: The ordering of the list always starts with the item at the origin
    def GetIndividualPieceCoordinates(piece, origin, orientation):
        if not check_valid_orienation(orientation):
            raise TypeError("Invalidid orientation")

        if not validate_origin(origin):
            raise TypeError("Invalid origin")

        vector = CoordinateHelper.to_vector[orientation]

        loc = np.copy(origin)
        result = []

        for c in piece.colors:
            result.append(CoordinateOfPiece(loc, c))
            loc = loc + vector

        return result
