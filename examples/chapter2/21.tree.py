# 2.9.2 Tree Class
"""A tree is any data structure that has an attribute a 
sequence of branches that are also trees.
"""
class Tree:
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))
    def is_leaf(self):
        return not self.branches

"""This Tree class can represent, for instance, the values
computed in an expression tree for the recursive implementation
of fib(), the function for computing Fibonacci numbers.
"""

def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.label + right.label, (left, right))

fib_tree(5) # Tree(3, (Tree(1, (Tree(0), Tree(1))), Tree(2, (Tree(1), Tree(1, (Tree(0), Tree(1)))))))


def sum_labels(t):
    """Sum the labels of a Tree instance, which may be None."""
    return t.label + sum([sum_labels(b) for b in t.branches])

# Memoization
"""The amount of computation time and memory saved by memoization 
in these cases is substantial. Instead of creating 18,454,929 different 
instances of the Tree class, we now create only 35.
"""
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

fib_tree = memo(fib_tree)
big_fib_tree = fib_tree(35)
big_fib_tree.label # 5702887
