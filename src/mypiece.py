import matplotlib.colors as mcolors
import numpy as np
from enum import Enum

class Orientation(Enum):
    TOWARDS_XPOSITIVE = 1,
    TOWARDS_XNEGATIVE = 2,
    TOWARDS_YPOSITIVE = 3,
    TOWARDS_YNEGATIVE = 4,
    TOWARDS_ZPOSITIVE = 5,
    TOWARDS_ZNEGATIVE = 6

def check_valid_orienation(orientation):
    orientation_str = str(orientation)
    return hasattr(Orientation, orientation_str.split('.')[-1])

def validate_color(color):
    return color in mcolors.CSS4_COLORS

def validate_origin(origin):
        # Just being extra paranoid that a nupy array is being used
        return (str(type(origin)) == "<class 'numpy.ndarray'>") and (len(origin) == 3)

class Piece():
    def __init__(self, colors):
        if len(colors) < 1:
            raise ValueError("At least one color required")

        for color in colors:
            if not validate_color(color):
                raise ValueError(f"Invalid color: {color}")

        self.colors = colors
