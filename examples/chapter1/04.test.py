from doctest import testmod, run_docstring_examples

def fib(n):
    """Compute the nth Fibonacci number, for n >= 2.
    
    >>> fib(1)
    0
    >>> fib(2)
    1
    >>> fib(5)
    3
    """
    if (n == 1):
        return 0
    if (n == 2):
        return 1

    def iter(i, first, second):
        if i == n:
            return second
        else:
            return iter(i + 1, second, first + second)

    return iter(2, 0, 1)

# Method 1: Use assert statements
def fib_test():
    assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
    assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
    assert fib(4) == 2, 'The 4th Fibonacci number should be 1'

# Method 2: Use testmod function from doctest module
testmod()

# Method 3: Use run_docstring_examples function from doctest module
run_docstring_examples(fib, globals(), True)