"""Basic arithmetic utilities with a small interactive demo."""

from math import isqrt


def add(a: float, b: float) -> float:
    """Return the sum of two numbers (integers or floats)."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b (the first argument minus the second)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers (integers or floats)."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b; raise ValueError when b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def is_even(n: int) -> bool:
    """Return True if the integer n is divisible by 2, including negative integers."""
    return n % 2 == 0


def is_prime(n: int) -> bool:
    """Return True if the integer n is a prime number.

    Numbers less than 2 (including negatives, 0, and 1) are not prime.
    """
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def is_perfect_square(n: int) -> bool:
    """Return True if the integer n is the square of an integer.

    Zero counts as a perfect square. Negative integers are never perfect squares.
    """
    if n < 0:
        return False
    root = isqrt(n)
    return root * root == n


def is_palindrome(n: int) -> bool:
    """Return True if the decimal digits of the integer n read the same both ways.

    Negative integers are never palindromes because of the leading minus sign,
    so is_palindrome(-121) returns False.
    """
    if n < 0:
        return False
    text = str(n)
    return text == text[::-1]


def is_power_of_two(n: int) -> bool:
    """Return True if the integer n is a positive power of two (1, 2, 4, 8, ...).

    Zero and negative integers are not powers of two.
    """
    return n > 0 and n & (n - 1) == 0


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers, always non-negative.

    gcd(0, 0) returns 0. Negative inputs are treated by their absolute values.
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of two integers, always non-negative.

    If either input is 0, the result is 0. Negative inputs are treated by their
    absolute values.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def clamp(value: float, low: float, high: float) -> float:
    """Return value limited to the inclusive range [low, high].

    Values below low return low, and values above high return high.
    Raises ValueError when low is greater than high.
    """
    if low > high:
        raise ValueError("Lower bound must not be greater than upper bound.")
    return max(low, min(value, high))


def factorial(n: int) -> int:
    """Return n! for a non-negative integer n, with factorial(0) equal to 1.

    Raises ValueError when n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    result = 1
    for factor in range(2, n + 1):
        result *= factor
    return result


def digit_sum(n: int) -> int:
    """Return the sum of the decimal digits of n, ignoring its sign.

    digit_sum(0) returns 0.
    """
    return sum(int(digit) for digit in str(abs(n)))


def count_digits(n: int) -> int:
    """Return the number of decimal digits in n, ignoring its sign.

    count_digits(0) returns 1, since zero is written with one digit.
    """
    return len(str(abs(n)))


def sign(n: float) -> int:
    """Return -1 if n is negative, 1 if n is positive, and 0 if n is zero."""
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


def list_max(values: list[float]) -> float:
    """Return the largest value in a non-empty list.

    If several values are equal to the maximum, the value itself is returned,
    so the result is the same regardless of which copy is picked.
    Raises ValueError when the list is empty.
    """
    if not values:
        raise ValueError("Cannot take the maximum of an empty list.")
    return max(values)


def list_min(values: list[float]) -> float:
    """Return the smallest value in a non-empty list.

    The result is one of the values in the list.
    Raises ValueError when the list is empty.
    """
    if not values:
        raise ValueError("Cannot take the minimum of an empty list.")
    return min(values)


def list_avg(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list as a float.

    Raises ValueError when the list is empty.
    """
    if not values:
        raise ValueError("Cannot average an empty list.")
    return sum(values) / len(values)


if __name__ == "__main__":
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))

    print(f"Addition: {add(first, second)}")
    print(f"Subtraction: {subtract(first, second)}")
    print(f"Multiplication: {multiply(first, second)}")
    try:
        print(f"Division: {divide(first, second)}")
    except ValueError as error:
        print(error)
