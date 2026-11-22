"""Basic arithmetic utilities with a small interactive demo."""


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


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers, always non-negative.

    gcd(0, 0) returns 0. Negative inputs are treated by their absolute values.
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


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
