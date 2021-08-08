import unittest, types
from divs import divs


class ScoreListTest(unittest.TestCase):

    def test_1(self):
        ls = []
        for it in divs(10):
            ls.append(it)
        self.assertEqual([1, 2, 5, 10], ls)

    def test_2(self):
        ls = []
        for it in divs(1):
            ls.append(it)
        self.assertEqual([1], ls)

    def test_3(self):
        ls = []
        for it in divs(6):
            ls.append(it)
        self.assertEqual([1, 2, 3, 6], ls)
