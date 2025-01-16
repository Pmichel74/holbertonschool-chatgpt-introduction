#!/usr/bin/python3
import sys


def factorial(n):
    """Calculate the factorial of a number."""
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
