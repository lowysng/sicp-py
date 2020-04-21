# 2.8.1 Measuring Efficiency
"""The efficiency of a program is characterized by how many
times some event occurs, such as a function call.
"""
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

fib(5) # 5

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

fib = count(fib)
fib(19) # 4181 
fib.call_count # 13529 (number of fib() calls)

def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

fib = count_frames(fib)
fib(19) # 4181
fib.open_count # 0
fib.max_count # 19 (maximum number of frames that are ever simultaneously active)
fib(24) # 46368
fib.max_count # 24


# 2.8.2 Memoization
"""Tree-recursive computational processes (like fib() above) can often
be made more efficient through memoization.

A memoized function stores the return value for any arguments
it has previously received.
"""
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

counted_fib = count(fib)
fib = memo(counted_fib)
fib(19) # 4181
counted_fib.call_count # 20
fib(34) # 570287
counted_fib.call_count # 35


# 2.8.3 Orders of Growth
"""The order of growth of a process specifies how the resource
requirements of a process grow as a function of the input.
"""
from math import sqrt
def count_factors(n):
    sqrt_n = sqrt(n)
    k, factors = 1, 0
    while k < sqrt_n:
        if n % k == 0:
            factors += 2
        k += 1
    if k * k == n:
        factors += 1
    return factors

count_factors(576) # 21


# 2.8.4 Example: Exponentiation
"""Recursive definition:"""
def exp(b, n):
    if n == 0:
        return 1
    return b * exp(b, n-1)

"""Iterative definition:"""
def exp_iter(b, n):
    result = 1
    for _ in range(n):
        result = result * b
    return result

"""Successive squaring definition:"""
square = lambda x : x*x
def fast_exp(b, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return square(fast_exp(b, n//2))
    else:
        return b * fast_exp(b, n-1)

fast_exp(2, 100) # 1267650600228229401496703205376


# 2.8.5 Growth Categories
"""Common categories:
O(1)        Constant        Growth is independent of input
O(log n)    Logarithmic     Multiplying input increments resources
O(n)        Linear          Incrementing input increments resources
O(n^2)      Quadratic       Incrementing input adds n resources
O(b^n)      Exponential     Incrementing input multiplies resources
"""