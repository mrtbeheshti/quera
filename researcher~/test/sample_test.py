import unittest
import Explorer


class ScoreListTest(unittest.TestCase):

    def test_1(self):
        result = {'sample_test_media/a': 1, 'sample_test_media/a/dir': 1}
        self.assertEqual(result, Explorer.explore("txt", "sample_test_media"))

    def test_2(self):
        result = {'sample_test_media/a/a/b': 1}
        self.assertEqual(result, Explorer.explore("mkv", "sample_test_media"))
