# 2.9 Recursive Objects
"""Objects can have other objects as attribute values. When
an object of some class has an attribute value of that same 
class, it is a recursive object.
"""

# 2.9.1 Linked List Class
class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)

def link_expression(s):
    """Return a string that would evaluate to s."""
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)

Link.__repr__ = link_expression

s = Link(3, Link(4, Link(5)))
len(s) # 3
s[1] # 4
s # 'Link(3, Link(4, Link(5)))'

"""Closure property"""
s_first = Link(s, Link(6))
s_first # Link(Link(3, Link(4, Link(5))), Link(6))

"""Linked list manipulations"""
def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))
Link.__add__ = extend_link
s + s # Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))

"""Linked list comprehensions"""
square = lambda x : x * x
is_odd = lambda x : x % 2 == 1

def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))
map_link(square, s) # Link(9, Link(16, Link(25)))

def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered
map_link(square, filter_link(is_odd, s)) # Link(9, Link(25))

def join_link(s, separator):
    if s is Link.empty:
        return ''
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)
join_link(s, ", ") # '3, 4, 5'