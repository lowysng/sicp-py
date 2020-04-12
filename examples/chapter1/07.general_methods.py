from doctest import testmod
from math import sqrt

# 1.6.2 Functions as General Methods
# Example: Iterative Improvement Algorithm
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1.0/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


phi = 1.0/2 + sqrt(5)/2

def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'

improve_test()


# 1.6.3 Nested Definitions
# Example: Computing the Square Root
def average(x, y):
    return (x + y) / 2.0
    
def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)

# print(sqrt(256))