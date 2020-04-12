# 1.5.3 Definining Functions II: Local Assignment
def percent_difference(x, y):
    difference = abs(x - y)
    return 100 * difference / x

result = percent_difference(40, 50)
print(result)


# 1.5.4 Conditional Statements
def absolute_value(x):
    """Compute abs(x)."""
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x

result = absolute_value(-2)
print(result)

print(4 < 2)
print(5 >= 5)
print(0 == -0)
print(True and False)
print(True or False)
print(not False)


# 1.5.5 Iteration
def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    def iter(i, first, second):
        if i == n:
            return second
        else:
            return iter(i + 1, second, first + second)

    return iter(2, 0, 1)