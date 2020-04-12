from doctest import testmod

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    def iter(n, i):
        print(n)
        if n == 1:
            return i
        elif (n % 2 == 0):
            return iter(n/2, i+1)
        else:
            return iter((n * 3) + 1, i+1)
    return iter(x, 1)

testmod()