from operator import add
from util import identity, square, triple, increment
from doctest import testmod

def make_repeater(h, n):
    """Return the function that computes the nth application of h.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times! 
    5
    """

    def n_repeater(x):
        def iter(i):
            if i == 0:
                return x
            if i == 1:
                return h(x)
            return h(iter(i - 1))
        return iter(n)

    return n_repeater

def accumulate(combiner, base, n, f):
    acc, k = base, 1
    while k <= n:
        acc, k = combiner(acc, f(k)), k + 1
    return acc

def compose1(h, g):
    """Return a function f, such that f(x) = h(g(x))."""
    def f(x):
        return h(g(x))
    return f


testmod()