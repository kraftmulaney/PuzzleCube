import numpy as np
from mypiece import Orientation, Piece
from cube import Cube

piece1 = Piece(['red', 'white', 'blue'])
piece2 = Piece(['green', 'red'])

print("Creating empty cube...")
cube = Cube(side_len = 3)

print("Placing piece #1...")
cube.try_place_piece(
    piece1,
    origin = np.array([0, 0, 0]),
    orientation = Orientation.TOWARDS_XPOSITIVE)

print("Placing piece #2...")
cube.try_place_piece(
    piece2,
    origin = np.array([0, 1, 0]),
    orientation = Orientation.TOWARDS_XPOSITIVE)

print(cube)
