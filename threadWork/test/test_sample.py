import unittest, time, functions
from solution import solve


class ScoreListTest(unittest.TestCase):

    def test_time_len(self):
        dur = int(round(time.time() * 1000))

        solve()
        print("hello\n")

        dur = int(round(time.time() * 1000)) - dur
        self.assertEqual(True, dur < 500)
