import unittest
import NoTwoAdjacent

class TestAdd(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(add.NoTwoAdjacent(3, 8), 84)
        self.assertEqual(add.NoTwoAdjacent(4, 6), 35)
        self.assertEqual(add.NoTwoAdjacent(5, 7), 56)
