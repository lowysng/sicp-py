# 2.4.11a Implementing a mutable linked list
"""We will now develop an implementation of a mutable linked list, with the goal
of understanding how a mutable list could be represented using functions with
local state.

Requirements:
- function that has a linked list as its local state
- lists need to have an identity, like any mutable value 

Our function will be a dispatch function. A dispatch function accepts a 'task'
argument that specifies what the function should do, and additional parameterization
arguments.

Our mutable list will respond to five different messages:
1 len           (sequence abstraction)
2 getitem       (sequence abstraction)
3 push_first    (add element to list)
4 pop_first     (remove element from list)
5 str           (return string representation)
"""

from link import is_link, link, first, rest, len_link, getitem_link, join_link

def mutable_link():
    """Return a functional implementation of a mutable linked list."""
    contents = 'empty'
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(contents, ", ")
    return dispatch

def to_mutable_link(source):
    """Return a functional list with the same contents as source."""
    s = mutable_link()
    for element in reversed(source):
        s('push_first', element)
    return s

suits = ['heart', 'diamond', 'spade', 'club']
s = to_mutable_link(suits)
type(s)         # <class 'function'>
s('str')        # 'heart, diamond, spade, club'
s('pop_first')  # 'heart'
s('str')        # 'diamond, spade, club'

# Message passing
"""Notice that the logic for all operations on our linked list is encapsulated
within the dispatch function. This approach of writing a program that responds
to different messages is called message passing."""