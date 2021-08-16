import unittest
from solution import capitalize


class Test(unittest.TestCase):

	def test_1(self):
		self.assertEqual(['Ali', 'Reyhaneh', 'Amir', 'Amir Abbas', 'Fatemeh Zahra'], capitalize(['ali', 'REYHANEH', 'aMIR', 'AMIR abbas', 'Fatemeh Zahra']))

	def test_2(self):
		self.assertEqual(['Nazanin Zahra', 'Ali Gholi Khane Bozorg'], capitalize(['nazaNIN ZAHRA', 'ALI GHOLI KHANE bozorg']))