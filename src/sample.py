import numpy as np
from mypiece import Orientation, Piece
from cube import Cube
from copy import copy

piece1 = Piece(['red', 'white', 'blue'])
piece2 = Piece(['green', 'red'])
piece3 = Piece(['aqua'])
piece4 = Piece(['purple'])

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

print("Placing piece #3...")
cube.try_place_piece(
    piece3,
    origin = np.array([0, 0, 1]),
    orientation = Orientation.TOWARDS_XPOSITIVE)

print("Cloning cube...")
cubecopy = copy(cube)

cubes_equal = cube == cubecopy
print(f"\nCubes are equual: {cubes_equal}")

print("\nPlacing piece #4 to original cube only")
cube.try_place_piece(
    piece4,
    origin = np.array([0, 2, 0]),
    orientation = Orientation.TOWARDS_XPOSITIVE)

print("\nOriginal Cube:")
print(cube)

print ("\nCloned Cube:")
print(cubecopy)

cubes_equal = cube == cubecopy
print(f"\nCubes are equual: {cubes_equal}")
