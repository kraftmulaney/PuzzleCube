import matplotlib.colors as mcolors
import numpy as np

def validate_color(color):
    return color in mcolors.CSS4_COLORS

class Piece():
    def __init__(self, colors):
        if len(colors) < 1:
            raise ValueError("At least one color required")

        for color in colors:
            if not validate_color(color):
                raise ValueError(f"Invalid color: {color}")

        self.colors = colors
