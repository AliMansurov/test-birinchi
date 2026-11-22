# test-birinchi

A small Python arithmetic demo and reusable helper functions.

## Run the interactive demo

```bash
python main.py
```

The demo accepts two numbers and prints their sum, difference, product, and quotient. Division by zero is reported without a traceback.

## Run the tests

The project uses Python's built-in `unittest`; no third-party packages are required. The tests live in `test_main.py` and cover the add, subtract, multiply, and divide helpers, including the divide-by-zero error, as well as `is_even`, `list_max`, `list_min`, `list_avg`, `is_prime`, and `gcd`.

Run the tests from the repository root so that `test_main.py` can import `main.py`:

```bash
python -m unittest -v
```

The helpers can be imported from `main.py`:

- `add`, `subtract`, `multiply`, and `divide` perform basic arithmetic. `divide` raises `ValueError` if its denominator is zero. `multiply` returns `0` when either operand is `0`, whether it is the first or the second. Two negative operands give a positive product, so `multiply(-4, -5)` returns `20`.
- `is_even(n)` returns `True` when the integer `n` is divisible by 2. This includes negative integers, such as `-6`.
- `is_prime(n)` returns `True` when the integer `n` is a prime number. Numbers less than 2, including negatives, `0`, and `1`, return `False`. For example, `is_prime(97)` returns `True` and `is_prime(49)` returns `False`.
- `gcd(a, b)` returns the greatest common divisor of two integers, always non-negative. Negative inputs use their absolute values, so `gcd(-12, 18)` returns `6`. `gcd(0, 0)` returns `0`.
- `list_max(values)` returns the largest value in a non-empty list. It raises `ValueError` if the list is empty. Zero is handled like any other value, so `list_max([-4, 0, -1])` returns `0`.
- `list_min(values)` returns the smallest value in a non-empty list. It raises `ValueError` if the list is empty. Zero is handled like any other value, so `list_min([4, 0, 7])` returns `0`.
- `list_avg(values)` returns the arithmetic mean of a non-empty list as a float. It raises `ValueError` if the list is empty. For example, `list_avg([1, 2])` returns `1.5`.

## Daily scripts

Small daily example scripts are stored as `daily_script_YYYYMMDD.py` at the repository root. Each one prints a greeting with its date when run directly, for example `python daily_script_20261027.py`.
