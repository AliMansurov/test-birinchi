# test-birinchi

A small Python arithmetic demo and reusable helper functions.

## Run the interactive demo

```bash
python main.py
```

The demo accepts two numbers and prints their sum, difference, product, and quotient. Division by zero is reported without a traceback.

## Run the tests

The project uses Python's built-in `unittest`; no third-party packages are required.

```bash
python -m unittest -v
```

The arithmetic helpers (`add`, `subtract`, `multiply`, and `divide`) can also be imported from `main.py`. `divide` raises `ValueError` if its denominator is zero.

## Daily scripts

Small daily example scripts are stored as `daily_script_YYYYMMDD.py` at the repository root. Each one prints a greeting with its date when run directly, for example `python daily_script_20261027.py`.
