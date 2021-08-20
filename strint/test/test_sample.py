import unittest 
from magic_numbers import Strint

class TestStrint(unittest.TestCase):
    def test_len(self):
        self.assertEqual(len(Strint(541)), 3)
        self.assertEqual(len(Strint(5)), 1)

    def test_call(self):
        number = Strint(8132495706)
        self.assertEqual(number(), '۸۱۳۲۴۹۵۷۰۶')

    def test_inheritance(self):
        self.assertTrue(issubclass(Strint, int))

    def test_lt(self):
        self.assertTrue(Strint(1593) < Strint(14))
        self.assertFalse(Strint(984) < Strint(4))
