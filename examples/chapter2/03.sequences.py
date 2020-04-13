# 2.3 Sequences
"""A sequence is a collection of values. It is a powerful, fundamental abstraction
in computer science. There are many different types of sequences, but they all share 
certain common properties:

1. Length: A sequence has a finite length. An empty sequence has a length 0.

2. Element selection: A sequence has an element corresponding to any non-negative integer
index less than its length, starting at 0 for the first element.

Python includes several native data types that are sequences, the most important of
which is the list.
"""


# 2.3.1 Lists

"""List basic operations"""
digits = [1, 8, 2, 8]
len(digits) # 4 (length)
digits[3] # 8 (element selection)

"""List arithmetics"""
[2, 7] + digits * 2 # [2, 7, 1, 8, 2, 8, 1, 8, 2, 8]

"""Nested lists"""
pairs = [[10, 20], [30, 40]]
pairs[1] # [30, 40]
pairs[1][0] # 30


# 2.3.2 Sequence Iteration

"""for statement"""
def count(s, value):
    """Count the number of occurrences of value in sequence s."""
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total

count(digits, 8) # 2

"""Sequence unpacking"""
pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
same_count = 0

for x, y in pairs:
    if x == y:
        same_count = same_count + 1

same_count # 2

"""Ranges"""
range(1, 10) # a range of integers from 1 to 9
list(range(5, 8)) # [5, 6, 7]
list(range(4)) # [0, 1, 2, 3]

for _ in range(3):
    print('Go Bears!')

# 2.3.3 Sequence processing

"""List comprehensions"""
odds = [1, 3, 5, 7, 9]
[x+1 for x in odds] # [2, 4, 6, 8, 10]
[x for x in odds if 25 % x == 0] # [1, 5]

"""Aggregation"""
sum(odds) # 25
min(odds) # 1
max(odds) # 9

def divisor(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

divisor(4) # [1, 2]
divisor(12) # [1, 2, 3, 4, 6]

"""Perfect numbers from 1 to 1000 (excluding 1)"""
[n for n in range(1, 1000) if sum(divisor(n)) == n] # [6, 28, 496]

"""Finding the minimum perimeter of a rectangle with integer side lengths, given its area."""
def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisor(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

area = 80
minimum_perimeter(area) # 36

"""Higher-Order Functions"""
def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce_it(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    divides_n = lambda x : n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

from operator import add
def sum_of_divisors(n):
    return reduce_it(add, divisors_of(n), 0)

def perfect(n):
    return sum_of_divisors(n) == n

keep_if(perfect, range(1, 1000)) # [1, 6, 28, 496]


# 2.3.4 Sequence Abstraction

"""Membership"""
digits = [1, 8, 2, 8]
2 in digits # True
1828 not in digits # True

"""Slicing"""
digits[0:2] # [1, 8]
digits[1:] # [8, 2, 8]