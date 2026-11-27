# test-birinchi

A small Python arithmetic demo and reusable helper functions.

## Run the interactive demo

```bash
python main.py
```

The demo accepts two numbers and prints their sum, difference, product, and quotient. Division by zero is reported without a traceback.

## Run the tests

The project uses Python's built-in `unittest`; no third-party packages are required. The tests live in `test_main.py` and cover the add, subtract, multiply, and divide helpers, including the divide-by-zero error, as well as `is_even`, `list_max`, `list_min`, `list_avg`, `is_prime`, `is_perfect_square`, `gcd`, `lcm`, `clamp`, `factorial`, `digit_sum`, `sign`, `is_palindrome`, `is_power_of_two`, and `count_digits`.

Run the tests from the repository root so that `test_main.py` can import `main.py`:

```bash
python -m unittest -v
```

The helpers can be imported from `main.py`:

- `add`, `subtract`, `multiply`, and `divide` perform basic arithmetic. `divide` raises `ValueError` if its denominator is zero. `multiply` returns `0` when either operand is `0`, whether it is the first or the second. Two negative operands give a positive product, so `multiply(-4, -5)` returns `20`.
- `is_even(n)` returns `True` when the integer `n` is divisible by 2. This includes negative integers, such as `-6`.
- `is_prime(n)` returns `True` when the integer `n` is a prime number. Numbers less than 2, including negatives, `0`, and `1`, return `False`. For example, `is_prime(97)` returns `True` and `is_prime(49)` returns `False`.
- `is_perfect_square(n)` returns `True` when the integer `n` is the square of an integer. Zero counts as a perfect square, and negative integers always return `False`. For example, `is_perfect_square(144)` returns `True` and `is_perfect_square(145)` returns `False`.
- `is_palindrome(n)` returns `True` when the decimal digits of the integer `n` read the same forwards and backwards. Negative integers always return `False`, so `is_palindrome(-121)` returns `False`. For example, `is_palindrome(12321)` returns `True` and `is_palindrome(123)` returns `False`.
- `is_power_of_two(n)` returns `True` when the integer `n` is a positive power of two, such as `1`, `2`, `4`, or `1024`. Zero and negative integers return `False`. For example, `is_power_of_two(1024)` returns `True` and `is_power_of_two(10)` returns `False`.
- `gcd(a, b)` returns the greatest common divisor of two integers, always non-negative. Negative inputs use their absolute values, so `gcd(-12, 18)` returns `6`. `gcd(0, 0)` returns `0`.
- `lcm(a, b)` returns the least common multiple of two integers, always non-negative. If either input is `0`, the result is `0`. Negative inputs use their absolute values, so `lcm(-4, 6)` returns `12`. For example, `lcm(4, 6)` returns `12`.
- `clamp(value, low, high)` limits `value` to the inclusive range `[low, high]`. Values below `low` return `low`, and values above `high` return `high`. It raises `ValueError` if `low` is greater than `high`. For example, `clamp(42, 0, 10)` returns `10`.
- `factorial(n)` returns `n!` for a non-negative integer `n`, with `factorial(0)` equal to `1`. It raises `ValueError` if `n` is negative. For example, `factorial(5)` returns `120`.
- `digit_sum(n)` returns the sum of the decimal digits of the integer `n`, ignoring its sign. For example, `digit_sum(-907)` returns `16`, and `digit_sum(0)` returns `0`.
- `count_digits(n)` returns the number of decimal digits in the integer `n`, ignoring its sign. Zero counts as one digit. For example, `count_digits(-907)` returns `3`, and `count_digits(0)` returns `1`.
- `sign(n)` returns `1` if `n` is positive, `-1` if `n` is negative, and `0` if `n` is zero. It works for floats as well as integers. For example, `sign(-2.5)` returns `-1`.
- `list_max(values)` returns the largest value in a non-empty list. It raises `ValueError` if the list is empty. Zero is handled like any other value, so `list_max([-4, 0, -1])` returns `0`.
- `list_min(values)` returns the smallest value in a non-empty list. It raises `ValueError` if the list is empty. Zero is handled like any other value, so `list_min([4, 0, 7])` returns `0`.
- `list_avg(values)` returns the arithmetic mean of a non-empty list as a float. It raises `ValueError` if the list is empty. For example, `list_avg([1, 2])` returns `1.5`.

## Daily scripts

Small daily example scripts are stored as `daily_script_YYYYMMDD.py` at the repository root. Each one prints a greeting with its date when run directly, for example `python daily_script_20261027.py`.
