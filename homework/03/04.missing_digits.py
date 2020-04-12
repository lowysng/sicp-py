from doctest import testmod

def missing_digits(num):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    """
    def remove_last_digit(num):
        return num // 10

    def get_num_digits(num):
        def iter(num, count):
            if num < 10:
                return count + 1
            else:
                return iter(remove_last_digit(num), count + 1)
        return iter(num, 0)

    def get_nth_digit(num, n):
        return (num % pow(10, n)) // pow(10, n - 1)

    def get_last_digit(num):
        return get_nth_digit(num, 1)

    def get_first_digit(num):
        if num < 10:
            return num
        return get_first_digit(remove_last_digit(num))

    def iter(num, checking_for, count, i):
        if get_first_digit(num) == checking_for:
            return count
        if get_nth_digit(num, i) == checking_for + 1:
            return iter(num, checking_for, count, i + 1)
        if get_nth_digit(num, i) == checking_for:
            return iter(num, checking_for - 1, count, i + 1)
        else:
            return iter(num, checking_for - 1, count + 1, i)

    if num < 10:
        return 0
        
    return iter(num, get_last_digit(num) - 1, 0, 2)


testmod()