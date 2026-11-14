# test-birinchi

A small Python arithmetic demo and reusable helper functions.

## Run the interactive demo

```bash
python main.py
```

The demo accepts two numbers and prints their sum, difference, product, and quotient. Division by zero is reported without a traceback.

## Run the tests

The project uses Python's built-in `unittest`; no third-party packages are required. The tests live in `test_main.py` and cover the add, subtract, multiply, and divide helpers, including the divide-by-zero error.

Run the tests from the repository root so that `test_main.py` can import `main.py`:

```bash
python -m unittest -v
```

The helpers can be imported from `main.py`:

- `add`, `subtract`, `multiply`, and `divide` perform basic arithmetic. `divide` raises `ValueError` if its denominator is zero.
- `is_even(n)` returns `True` when the integer `n` is divisible by 2.
- `list_max(values)` returns the largest value in a non-empty list. It raises `ValueError` if the list is empty.
- `list_min(values)` returns the smallest value in a non-empty list. It raises `ValueError` if the list is empty.

## Daily scripts

Small daily example scripts are stored as `daily_script_YYYYMMDD.py` at the repository root. Each one prints a greeting with its date when run directly, for example `python daily_script_20261027.py`.
