import unittest
from ans import solve


class ScoreListTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual("10002 + 50 = 10052", solve("10# + 50 = 10052"))

    def test_2(self):
        self.assertEqual("-1", solve("12 + 13 = #6"))

    def test_3(self):
        self.assertEqual("52979783 + 40838457 = 93818240", solve("52979783 + 40838457 = #40"))
