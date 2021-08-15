import unittest
from function import calc


class ScoreListTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual((9.666666666666666, 5, 20), calc([4, 5, 20]))

    def test_2(self):
        self.assertEqual((12.0, 5, 30), calc([1, 5, 30]))

    def test_3(self):
        self.assertEqual((20.25, 24.5, 30), calc([2, 20, 30, 29]))
