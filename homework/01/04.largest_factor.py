from math import sqrt
from doctest import testmod

def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    if isPrime(x):
        return 1
    else:
        i = 2
        while i < x:
            if x % i == 0:
                return x / i
            i = i + 1

def isPrime(n):
    """Return True if n is a prime number, otherwise return False.

    >>> isPrime(2)
    True
    >>> isPrime(3)
    True
    >>> isPrime(4)
    False
    >>> isPrime(13)
    True
    >>> isPrime(14)
    False
    """
    def smallest_divisor(n):
        return find_divisor(n, 2)
    def find_divisor(n, test_divisor):
        if test_divisor * test_divisor > n:
            return n
        elif n % test_divisor == 0:
            return test_divisor
        else:
            return find_divisor(n, test_divisor + 1)
    return smallest_divisor(n) == n

testmod()