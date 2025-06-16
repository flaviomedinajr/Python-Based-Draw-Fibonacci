import arrays # External module for fixed-size arrays
import turtle
import random

# Recursive Fibonacci Function
def fibonacci(n):
    # n is number

    # Returns the nth number in the Fibonacci sequence.
    # Base cases for n = 1 (returns 0) and n = 2 (returns 1).
    # Raises an error for non-positive input.
    if n<= 0:
        raise ValueError("Undefined")
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)