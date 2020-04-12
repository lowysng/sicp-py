from doctest import testmod

def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def iter(n, i):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif pow(2, i) > n:
            return 0
        else:
            return iter(n - pow(2, i), i) + iter(n, i + 1)

    return iter(total, 0)

testmod()