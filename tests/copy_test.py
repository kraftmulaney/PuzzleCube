import unittest
import numpy as np
from .context import Piece, Orientation, Cube
from copy import Error, copy

class CopyTests(unittest.TestCase):
    def test_copy_empty_cube_should_succeed(self):
        cube = Cube(side_len = 2)
        cubecopy = copy(cube)
        # $TODO
        raise Error("Not yet implemented")
