# 1.6.7 Lambda Expressions
# Creating functions without giving it a name
def compose1(f, g):
    return lambda x : f(g(x))

s = lambda x : x * x

