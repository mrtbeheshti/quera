import unittest
from reverse import Reverse


class ScoreListTest(unittest.TestCase):

    def _test_ls(self, ls):
        tmp = list(ls)
        out = []
        for it in Reverse(ls):
            out.append(it)
        out.reverse()
        for a, b in zip(tmp, out):
            self.assertEqual(a, b)
        self.assertEqual(len(tmp), len(out))
        for a, b in zip(tmp, ls):
            self.assertEqual(a, b)

    def test_1(self):
        ls = [1, 2, 3, 4, 5]
        out = []
        for it in Reverse(ls):
            out.append(it)

        self.assertEqual(out, [5, 4, 3, 2, 1])

    def test_2(self):
        ls = ['mano', 'ali', 'ye', 'teamim']

        out = []
        for it in Reverse(ls):
            out.append(it)

        self.assertEqual(out, ['teamim', 'ye', 'ali', 'mano'])
