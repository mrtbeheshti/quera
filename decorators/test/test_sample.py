import unittest, types
from decorator import decorator


class ScoreListTest(unittest.TestCase):

    def test_sample_1(self):
        def validator(x):
            return x > 0

        @decorator(validator)
        def f(x):
            return x

        self.assertEqual(f(10), 10)
        self.assertEqual(f(-1), 'error')

    def test_sample_2(self):
        def validator(x, y):
            return type(x) == int and type(y) == int

        @decorator(validator)
        def f(x, y):
            return x + y

        self.assertEqual(f(20, 10), 30)
        self.assertEqual(f("34", 20), 'error')
