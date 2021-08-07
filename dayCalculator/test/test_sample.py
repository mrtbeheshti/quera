import unittest
from function import day_calculator


class ScoreListTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(30, day_calculator('1999-2-13'))

    def test_2(self):
        self.assertEqual('Not yet born', day_calculator('1999-01-13'))
