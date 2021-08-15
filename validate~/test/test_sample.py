import unittest
from ans import *


class ScoreListTest(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email('test.test91@yahoo.com'))
        self.assertFalse(validate_email('exampl#e@gmail.comm'))

    def test_validate_phone(self):
        self.assertTrue(validate_phone('09116547899'))
        self.assertFalse(validate_phone('091165478999'))
