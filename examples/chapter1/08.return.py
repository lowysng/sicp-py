import general_methods as gm

# 1.6.4 Functions as Returned Values
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def square(x):
    return x * x

def successor(x):
    return x + 1

square_successor = compose1(square, successor)
print(square_successor(12))


# 1.6.5 Example: Newton's Method
def newton_update(f, df):
    def update(x):
        return x - (f(x) / df(x))
    return update

def find_zero(f, df):
    def near_zero(x):
        return gm.approx_eq(f(x), 0)
    return gm.improve(newton_update(f, df), near_zero)

# Computing the square root using Newton's method
# sqrt(64) = x such that x^2 - 64 = 0
def square_root_newton(a):
    def f(x):
        return (x * x) - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

print(square_root_newton(64.0))

# Generally: The degree root n of a is x such that x^n - a = 0
def power(x, n):
    product, k = 1, 0
    while k <= n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n - 1)
    return find_zero(f, df)

print(nth_root_of_a(2, 64))
print(nth_root_of_a(3, 64))
print(nth_root_of_a(6, 64))