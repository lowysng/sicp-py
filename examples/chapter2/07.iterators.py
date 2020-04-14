# 2.4.7 Iterators
"""Iterators provide means for processing elements of a container value
sequentially.

The iterator abstraction has two components: a mechanism for retrieving 
the next element in the sequence being processed and a mechanism for 
signaling that the end of the sequence has been reached and no further
elements remain.
"""

primes = [2, 3, 5, 7]
type(primes) # <class 'list'>

iterator = iter(primes)
type(iterator) # <class 'list_iterator'>

next(iterator) # 2
next(iterator) # 3


"""Calling iter on an iterator will return that iterator, not a copy."""
iterator2 = iter(iterator)

next(iterator2) # 5
next(iterator) # 7

"""Any value that can produce iterators is called an iterable value.

These include sequence values such as strings and tuples, as well as
otehr containers such as sets and dictionaries.

Several built-in functions take as arguments iterable values and
return iterators. These functions are used extensively for lazy sequence
processing.
"""

"""map()"""
def double_and_print(x):
    print('***', x, '=>', 2*x, 'xxx')
    return 2*x

s = range(3, 7)
doubled = map(double_and_print, s) # double_and_print() not yet called

next(doubled) # double_and_print() called for the first time
next(doubled)
list(doubled)

"""filter()"""
def is_odd(x):
    if x % 2 != 0:
        print(x, 'is odd')
        return True
    else:
        return False

s = range(0, 10)
odds = filter(is_odd, s)

next(odds) # 1
next(odds) # 3
next(odds) # 5
list(odds) # [7, 9]