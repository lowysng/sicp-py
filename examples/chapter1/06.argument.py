from doctest import testmod

# 1.6.1 Functions as Arguments
def sum_naturals(n):
    """
    >>> sum_naturals(100)
    5050
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """
    >>> sum_cubes(100)
    25502500
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + (k * k * k), k + 1
    return total

def pi_sum(n):
    """
    >>> pi_sum(100)
    3.1365926848388144
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + (8.0 / ((4*k-3) * (4*k-1))), k + 1
    return total

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x * x * x

def sum_cubes(n):
    """
    >>> sum_cubes(3)
    36
    """
    return summation(n, cube)

def identity(x):
    return x

def sum_naturals(n):
    """
    >>> sum_naturals(10)
    55
    """
    return summation(n, identity)

def pi_term(x):
    return (8.0 / ((4*x-3) * (4*x-1)))

def pi_sum(n):
    """
    >>> pi_sum(1e6)
    3.141592153589902
    """
    return summation(n, pi_term)

testmod()