def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


if __name__ == "__main__":
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))

    print(f"Addition: {add(first, second)}")
    print(f"Subtraction: {subtract(first, second)}")
