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



# Fill array with Fibonacci numbers
def fill_fibonacci_array(a, i = 0):
    # Recursively fills an array `a` with Fibonacci numbers.
    # i is the current index in the array.

    if i >= len(a):
        return a
    a[i] = fibonacci(i + 1)
    return fill_fibonacci_array(a, i + 1)



# Print ratios between adjacent Fibonacci numbers
def print_ratios(a, i = 0):
    # Just a friendly reminder, a is an array & i is an index

    # Recursively prints division and ratio 
    # between consecutive Fibonacci numbers in the array.

    try:
        x = a[i]
        y = a[i]

        division = y / x
        result = (x + y) / y

    except ZeroDivisionError:
        result = 0
    except IndexError:
        return # Base case: stop recursion when out of range

    if result == 0:
        print(f"{x:>4n} {y:>4n} Undefined")
    else:
        print(f"{x:>4n} {y:>4n} {division:.5f} {result:.5f}")

    print_ratios(a, i + 1)


# Fibonacci Spiral Drawer
def draw_fibonacci_spiral():
    # Uses Turtle graphics to draw a spiral 
    # made of squares and arcs sized using Fibonacci numbers.

    turtle.reset() 
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()

    # a_a is array_a
    a_a = arrays.Array(15) # Create a new array of size 15

    # a_b is array_b
    a_b = fill_fibonacci_array(a_a) # Fill it with Fibonacci numbers

    total_size = sum(a_b) # Calculate total size for centering

    turtle.goto(-total_size // 4, -total_size // 10)
    turtle.left(90)

    recursion(a_b, 13) # Draw from the 13th Fibonacci number down


# 
def recursion(a, s):
    # a is an array
    # s is size
    
   
    if s < 1:
        return
    
