import unittest
from .context import mypiece

class PieceTests(unittest.TestCase):
    def test_Mult(self):
        self.assertTrue(mypiece.MyMult(2, 4) == 8)
