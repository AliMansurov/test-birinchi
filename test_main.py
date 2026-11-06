"""Unit tests for the arithmetic helpers in main.py."""

import unittest

from main import add, divide, is_even, multiply, subtract


class ArithmeticTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_and_float(self):
        self.assertEqual(add(-1.5, 4), 2.5)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(4, 7), -3)

    def test_multiply(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_negative_denominator(self):
        self.assertEqual(divide(9, -3), -3)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(1, 0)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-6))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(-3))


if __name__ == "__main__":
    unittest.main()
