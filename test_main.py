"""Unit tests for the arithmetic helpers in main.py."""

import unittest

from main import add, clamp, count_digits, digit_sum, divide, factorial, gcd, is_even, is_palindrome, is_perfect_square, is_power_of_two, is_prime, lcm, list_avg, list_max, list_min, multiply, sign, subtract


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

    def test_gcd_basic(self):
        self.assertEqual(gcd(12, 18), 6)

    def test_gcd_coprime_is_one(self):
        self.assertEqual(gcd(35, 64), 1)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(0, 9), 9)
        self.assertEqual(gcd(9, 0), 9)

    def test_gcd_both_zero(self):
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_negative_inputs_return_non_negative(self):
        self.assertEqual(gcd(-12, 18), 6)
        self.assertEqual(gcd(-12, -18), 6)

    def test_gcd_is_symmetric(self):
        self.assertEqual(gcd(54, 24), gcd(24, 54))

    def test_lcm_basic(self):
        self.assertEqual(lcm(4, 6), 12)

    def test_lcm_coprime_is_product(self):
        self.assertEqual(lcm(5, 7), 35)

    def test_lcm_equal_inputs(self):
        self.assertEqual(lcm(9, 9), 9)

    def test_lcm_one_divides_other(self):
        self.assertEqual(lcm(3, 12), 12)

    def test_lcm_with_zero_is_zero(self):
        self.assertEqual(lcm(0, 8), 0)
        self.assertEqual(lcm(8, 0), 0)
        self.assertEqual(lcm(0, 0), 0)

    def test_lcm_negative_inputs_return_non_negative(self):
        self.assertEqual(lcm(-4, 6), 12)
        self.assertEqual(lcm(-4, -6), 12)

    def test_lcm_is_symmetric(self):
        self.assertEqual(lcm(21, 6), lcm(6, 21))

    def test_clamp_value_inside_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_clamp_value_below_low(self):
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_clamp_value_above_high(self):
        self.assertEqual(clamp(42, 0, 10), 10)

    def test_clamp_value_on_boundaries(self):
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_clamp_equal_bounds(self):
        self.assertEqual(clamp(7, 4, 4), 4)

    def test_clamp_negative_range(self):
        self.assertEqual(clamp(-20, -10, -5), -10)
        self.assertEqual(clamp(-1, -10, -5), -5)

    def test_clamp_float_value(self):
        self.assertEqual(clamp(2.5, 0.0, 1.0), 1.0)

    def test_clamp_low_greater_than_high_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Lower bound"):
            clamp(5, 10, 0)

    def test_factorial_zero_and_one(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_factorial_small_values(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_large_value_is_exact(self):
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_factorial_negative_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "non-negative"):
            factorial(-1)

    def test_digit_sum_zero(self):
        self.assertEqual(digit_sum(0), 0)

    def test_digit_sum_multi_digit(self):
        self.assertEqual(digit_sum(12345), 15)

    def test_digit_sum_ignores_sign(self):
        self.assertEqual(digit_sum(-907), 16)

    def test_digit_sum_single_digit(self):
        self.assertEqual(digit_sum(7), 7)

    def test_is_perfect_square_zero_and_one(self):
        self.assertTrue(is_perfect_square(0))
        self.assertTrue(is_perfect_square(1))

    def test_is_perfect_square_true_for_squares(self):
        self.assertTrue(is_perfect_square(144))
        self.assertTrue(is_perfect_square(10000))

    def test_is_perfect_square_false_for_non_squares(self):
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(143))
        self.assertFalse(is_perfect_square(145))

    def test_is_perfect_square_negative_is_false(self):
        self.assertFalse(is_perfect_square(-4))

    def test_sign_positive(self):
        self.assertEqual(sign(42), 1)

    def test_sign_negative(self):
        self.assertEqual(sign(-7), -1)

    def test_sign_zero(self):
        self.assertEqual(sign(0), 0)

    def test_sign_float_values(self):
        self.assertEqual(sign(0.001), 1)
        self.assertEqual(sign(-2.5), -1)

    def test_is_palindrome_single_digits_and_zero(self):
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(7))

    def test_is_palindrome_true_for_palindromic_numbers(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(12321))

    def test_is_palindrome_false_for_non_palindromes(self):
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(120))

    def test_is_palindrome_negative_is_false(self):
        self.assertFalse(is_palindrome(-121))

    def test_is_power_of_two_true_for_powers(self):
        for n in (1, 2, 4, 8, 1024):
            self.assertTrue(is_power_of_two(n), n)

    def test_is_power_of_two_false_for_non_powers(self):
        for n in (3, 6, 10, 1023):
            self.assertFalse(is_power_of_two(n), n)

    def test_is_power_of_two_zero_is_false(self):
        self.assertFalse(is_power_of_two(0))

    def test_is_power_of_two_negative_is_false(self):
        self.assertFalse(is_power_of_two(-4))

    def test_count_digits_zero_has_one_digit(self):
        self.assertEqual(count_digits(0), 1)

    def test_count_digits_multi_digit(self):
        self.assertEqual(count_digits(12345), 5)

    def test_count_digits_ignores_sign(self):
        self.assertEqual(count_digits(-907), 3)

    def test_count_digits_single_digit(self):
        self.assertEqual(count_digits(7), 1)


if __name__ == "__main__":
    unittest.main()
