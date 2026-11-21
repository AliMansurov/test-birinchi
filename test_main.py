"""Unit tests for the arithmetic helpers in main.py."""

import unittest

from main import add, divide, is_even, is_prime, list_avg, list_max, list_min, multiply, subtract


class ArithmeticTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_and_float(self):
        self.assertEqual(add(-1.5, 4), 2.5)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(4, 7), -3)

    def test_subtract_from_zero(self):
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_multiply_two_negatives(self):
        self.assertEqual(multiply(-4, -5), 20)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(0, 42), 0)

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

    def test_is_even_large_integers(self):
        self.assertTrue(is_even(1000000))
        self.assertFalse(is_even(1000001))

    def test_is_even_negative_boundary(self):
        self.assertTrue(is_even(-2))
        self.assertFalse(is_even(-1))

    def test_list_max(self):
        self.assertEqual(list_max([3, 9, -2]), 9)
        self.assertEqual(list_max([-5]), -5)

    def test_list_max_single_element(self):
        self.assertEqual(list_max([7]), 7)

    def test_list_max_with_duplicate_maximum(self):
        self.assertEqual(list_max([4, 9, 9, 1]), 9)

    def test_list_max_all_negative(self):
        self.assertEqual(list_max([-7, -3, -9]), -3)

    def test_list_max_with_zero(self):
        self.assertEqual(list_max([-4, 0, -1]), 0)

    def test_list_max_empty_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "empty list"):
            list_max([])

    def test_list_min(self):
        self.assertEqual(list_min([3, 9, -2]), -2)
        self.assertEqual(list_min([-5]), -5)

    def test_list_min_with_duplicate_minimum(self):
        self.assertEqual(list_min([4, 1, 1, 9]), 1)

    def test_list_min_all_positive(self):
        self.assertEqual(list_min([8, 2, 5]), 2)

    def test_list_min_with_zero(self):
        self.assertEqual(list_min([4, 0, 7]), 0)

    def test_list_min_empty_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "empty list"):
            list_min([])

    def test_list_avg(self):
        self.assertEqual(list_avg([2, 4, 6]), 4)

    def test_list_avg_single_element(self):
        self.assertEqual(list_avg([7]), 7)

    def test_list_avg_returns_float_for_non_integer_mean(self):
        self.assertEqual(list_avg([1, 2]), 1.5)

    def test_list_avg_negative_values(self):
        self.assertEqual(list_avg([-3, -1, -2]), -2)

    def test_list_avg_mixed_signs_to_zero(self):
        self.assertEqual(list_avg([-5, 0, 5]), 0)

    def test_list_avg_empty_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "empty list"):
            list_avg([])

    def test_is_prime_small_primes(self):
        for n in (2, 3, 5, 7, 11, 13):
            self.assertTrue(is_prime(n), n)

    def test_is_prime_small_composites(self):
        for n in (4, 6, 8, 9, 10, 15):
            self.assertFalse(is_prime(n), n)

    def test_is_prime_zero_and_one_are_not_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_is_prime_negative_numbers_are_not_prime(self):
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(-2))

    def test_is_prime_square_of_prime_is_not_prime(self):
        self.assertFalse(is_prime(49))
        self.assertFalse(is_prime(121))

    def test_is_prime_larger_prime(self):
        self.assertTrue(is_prime(97))


if __name__ == "__main__":
    unittest.main()
