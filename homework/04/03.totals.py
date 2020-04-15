from tree import tree, print_tree
from mobile import examples, is_planet, total_weight, end, left, right, size
from doctest import testmod

def totals_tree(m):
    """Return a tree representing the mobile with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    if is_planet(m):
        return tree(size(m))
    
    return tree(total_weight(m), [totals_tree(end(left(m))), totals_tree(end(right(m)))])

testmod()