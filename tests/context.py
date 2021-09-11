import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import src
from src.mypiece import Piece
from src.cube import Orientation
from src.cube import Cube
from src.coordhelper import CoordinateHelper, CoordinateOfPiece
from src.rules import CheckIfCubeFull
