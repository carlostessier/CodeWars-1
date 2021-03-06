import unittest

from katas.kyu_7.square_digits import square_digits


class SquareDigitsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(square_digits(9119), 811181)

    def test_equals_2(self):
        self.assertEqual(square_digits(12345), 1491625)
