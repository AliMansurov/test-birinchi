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
