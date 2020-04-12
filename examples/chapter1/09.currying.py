# 1.6.6 Currying
# Converting a function that takes multiple arguments into a chain of 
# functions that each take a single argument
# f(x, y) => g(x)(y) === f(x, y)
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1

def curry2(f):
    def g(x):
        def h(x):
            return f(x, y)
        return h
    return g

def uncurry2(f):
    def g(x, y):
        return f(x)(y)
    return g
