# 2.2.1 Example: Rational Numbers
"""A rational number is a ratio of integers, and rational numbers
constitute an important sub-class of real numbers.

Assume that we already have a way of constructing and manipulating rational numbers:
- rational(n, d) returns the rational number with numerator n and denominator d
- numer(x) returns the numerator of the rational number x
- denom(x) returns the denominator of the rational number x

This strategy for designing programs is called "wishful thinking". We can now define
the following functions:
"""

def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

# 2.2.2 Pairs
"""To implement the concrete level of our data abstraction, we will use a Python
compound structure called a list.
"""

[10, 20]        # a list literal

"""We can use Python lists represent a rational number as a pair of two integers.
"""

def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

"""We can use the arithmetic operations we defined earlier to manipulate rational numbers.
"""

half = rational(1, 2)
print_rational(half) # 1  /  2
third = rational(1, 3)
print_rational(mul_rationals(half, third)) # 1  /  6
print_rational(add_rationals(third, third)) # 6  /  9

"""Let's better our rational number implementation by having it reduce rational
numbers to lowest terms.
"""

from math import gcd
def rational(n, d):
    g = gcd(n, d)
    return (n // g, d // g)

print_rational(add_rationals(third, third)) # 2  / 3