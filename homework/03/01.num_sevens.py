from doctest import testmod

def num_sevens(x):
    """Returns the number of times 7 appears as a digit of x.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
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

    def seven(x):
        if x == 7:
            return 1
        else:
            return 0

    if x < 10:
        return seven(x)
    else:
        return num_sevens(remove_last_digit(x)) + seven(extract_last_digit(x))


testmod()