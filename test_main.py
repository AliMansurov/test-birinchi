"""Unit tests for the arithmetic helpers in main.py."""

import unittest

from main import add, divide, multiply, subtract


class ArithmeticTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)

    def test_multiply(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
