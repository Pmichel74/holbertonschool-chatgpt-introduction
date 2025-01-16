#!/usr/bin/python3

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Function Description:
    This function takes an integer n and calculates its factorial using a recursive approach.
    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.

    Parameters:
    n (int): The number to calculate the factorial of. Must be a non-negative integer.

    Returns:
    int: The factorial of the number n. If n is 0 or 1, returns 1.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 factorial_recursive.py <number>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Number must be non-negative.")
        print(factorial(number))
    except ValueError as e:
        print(e)
        sys.exit(1)