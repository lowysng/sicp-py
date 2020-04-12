from operator import add, sub
from doctest import testmod

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b >= 0:
        h = add
    else:
        h = sub
    return h(a, b)

testmod()