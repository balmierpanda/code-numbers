import sys


def sum_numbers(numbers):
    """Return the sum of a list of numbers."""
    return sum(numbers)


def main():
    """Print the sum of command-line numeric arguments."""
    if len(sys.argv) <= 1:
        print("Usage: python sum_numbers.py <number> [<number> ...]")
        return
    try:
        numbers = [float(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("All arguments must be numbers.")
        return
    print(sum_numbers(numbers))


if __name__ == "__main__":
    main()
