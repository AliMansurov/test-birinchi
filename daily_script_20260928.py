"""Small daily example script."""

from datetime import date


def main() -> None:
    print(f"Hello from {date.today().isoformat()}!")


if __name__ == "__main__":
    main()
