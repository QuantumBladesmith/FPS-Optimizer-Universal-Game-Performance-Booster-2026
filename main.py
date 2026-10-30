"""Entry point for engine."""

from utils import prepare


def main():
    result = prepare(10)
    print(f"Project: {result}")


if __name__ == "__main__":
    main()
