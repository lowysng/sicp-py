from operator import add, sub
from doctest import testmod

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    def extract_last_digit(n):
        if n < 10:
            return n
        else:
            return n % 10
        
    def remove_last_digit(n):
        if n < 10:
            return n
        else:
            return n // 10
    
    def contains_seven(x):
        if extract_last_digit(x) == 7:
            return True
        if not x < 10:
            return contains_seven(remove_last_digit(x))
        else:
            return False

    def is_multiple_of_seven(x):
        return x % 7 == 0

    def change_sign(operator):
        if operator == add:
            return sub
        return add

    def iter(i, operator, pingpong_val):
        if i == n:
            return pingpong_val
        if is_multiple_of_seven(i) or contains_seven(i):
            return iter(i + 1, change_sign(operator), change_sign(operator)(pingpong_val, 1))
        else: 
            return iter(i + 1, operator, operator(pingpong_val, 1))

    return iter(1, add, 1)

testmod()