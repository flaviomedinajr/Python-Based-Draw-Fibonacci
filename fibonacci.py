# Author: Flavio Medina

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


# Helper function to recursively draw squares/arcs
def recursion(a, s):
    # a is an array
    # s is size
    
    # Recursively draws square and arc for each Fibonacci number.
    if s < 1:
        return
    
    draw_square(a[s])
    draw_arc(a[s])
    recursion(a, s - 1)



# Draw a quarter-circle arc
def draw_arc(r):
    # r is radius

    # Draws a 90-degree arc with given radius using turtle.circle.
    turtle.pendown()
    turtle.circle(-r, 90)
    turtle.penup()



# Draw a square with a random fill color
def draw_square(s):
    # s is side

    # Draws a square of given side length and fills it with a random color.
    turtle.pensize(2)

    turtle.pendown()


    turtle.colormode(255)
    turtle.fillcolor(random.randint(0, 255), random.randint(0, 255),
                     random.randint(0, 255))
    turtle.begin_fill()
    for _ in range(0, 4):
        turtle.forward(s)
        turtle.right(90)
    turtle.penup()
    turtle.end_fill()



# Main driver function
def main():
    # This main function can test individual Fibonacci functions or draw the spiral.

    # array = arrays.Array(20)
    
    # print(fibonacci(9))                     # Test 1: Fibonacci number
    # print(fill_fibonacci_array(array))     # Test 2: Fill Fibonacci array
    # print_ratios(fill_fibonacci_array(array))  # Test 3: Print ratios

    draw_fibonacci_spiral()                  # Test 4: Draw the spiral
    input("Enter to continue....")


# Python standard entry point
if __name__ == "__main__":
    main()