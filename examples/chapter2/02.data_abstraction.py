# 2.2.3 Abstraction Barriers
"""Earlier we defined operations in terms of a construction rational() and selectors
numer() and denom(). 

The underlying idea of data abstractions is to identify a basic set of operations
in which all manipulations of values of some kind will be expressed, and then to
use only those operations to manipulate thes data.

This makes it easier to change the representation of abstract data without
changing the behavior of a program that uses that data.

We can split our program into three layers:

1. add_rational(), mul_rational(), rationals_are_equal(), print_rational()
Functions in the first layer use rational numbers to perform computation. They treat
rationals as whole data values. It's important to note that these functions are not
concerned with how these rationals are implemented.

2. rational(), numer(), denom()
Those in the second part create rationals or implement rational operations. These
functions are used to implement those in the first layer.

3. list literals and element selection
Functions in the third layer are used to implement selectors and constructors for
rationals. These functions usually use compound data structures that are provided by the 
programming language. 

Structuring our programs this way, using abstraction barriers, makes them easier to 
maintain and to modify.
"""

# 2.2.4 The Properties of Data
"""Abstract data can be generally expressed using a collection of selectors and 
constructors, together with some behavior conditions. As long as the behavior conditions
are met, the selectors and constructors constitute a valid representation of a kind 
of data.

More concretely:
- rational() is our constructor
- numer() and denom() are our selectors
- the condition that our implementation must satisfy is that if x = rational(n, d) then
numer(x) / denom(x) == n / d

Let's change how our constructor and selectors are implemented, without changing their
behavior. Instead of using Python lists, we will use functions instead.
"""

def pair(x, y):
    """Return a function that represents a pair."""
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    """Return the element at index i of pair p."""
    return p(i)

def rational(n, d):
    return pair(n, d)

def numer(x):
    return select(x, 0)

def denom(x):
    return select(x, 1)

def add_rationals(x, y):
    """Unchanged from earlier sections"""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def print_rational(x):
    """Unchanged from earlier sections"""
    print(numer(x), '/', denom(x))

half = rational(1, 2)
print_rational(half) # 1  /  2
third = rational(1, 3)
print_rational(add_rationals(third, third)) # 6  /  9

"""Here is our original abstraction layers (Section 2.2.1 - 2.2.2):
1. add_rational(), mul_rational(), rationals_are_equal(), print_rational()
2. rational(), numer(), denom()
3. list literals and element selection

Here is our new abstraction layers (Section 2.2.3 - 2.2.4):
1. add_rational(), mul_rational(), rationals_are_equal(), print_rational()
2. rational(), numer(), denom()
3. pair(), select()

"""