from tree import tree, copy_tree, is_leaf, branches, print_tree, label
from doctest import testmod

def replace_leaf(t, old, replacement):
    """Returns a new tree where every leaf value equal to old has
    been replaced with replacement.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    if is_leaf(t):
      if label(t) == old:
        return tree(replacement)
      return tree(label(t))
    return tree(label(t), [replace_leaf(branch, old, replacement) for branch in branches(t)])

testmod()