"""Basic arithmetic utilities with a small interactive demo."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b; raise ValueError when b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


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
