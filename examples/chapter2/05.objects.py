# 2.4 Mutable Data
"""Adding state to data is a central ingredient of a paradigm called 
object-oriented programming. In OOP, data objects evolve independently 
of the rest of the program.
"""

# 2.4.1 The Object Metaphor
"""Objects combine data values with behaviors. They represent information,
and interact with other objects. 
"""

"""Date object"""
from datetime import date # the name date is bound a class
tues = date(2014, 5, 13) # constructing an instance of the date class

"""Object attributes"""
tues.year # 2014

"""Object methods"""
tues.strftime('%A, %B %d')

"""More objects"""
'1234'.isnumeric() # True
'rOBERT dE nIRO'.swapcase() # 'Robert De Niro'
'eyes'.upper().endswith('YES') # True


# 2.4.2 Sequence Objects
"""Mutable objects are used to represent values that change over time.

An object may have changing properties due to mutating operations.
"""

chinese = ['coin', 'string', 'myriad']

suits = chinese
suits.pop() # 'myriad'
suits.remove('string')
suits.append('cup')
suits.extend(['sword', 'club'])
suits[2] = 'spade'
suits # ['coin', 'cup', 'spade', 'club']

suits[0:2] = ['heart', 'diamond']
suits # ['heart', 'diamond', 'spade', 'club']

"""The object bound to the name chinese has also changed, because it 
is the same list object that was bound to suits.
"""

chinese # ['heart', 'diamond', 'spade', 'club']

"""Lists can be copied using the list constructor function. Changes to
one list do not affect another, unless they share structure.
"""

nest = list(suits)
nest[0] = suits

suits.insert(2, 'Joker')
nest # [['heart', 'diamond', 'Joker', 'spade', 'club'], 'diamond', 'spade', 'club']

nest[0].pop(2) # 'Joker'
suits # ['heart', 'diamond', 'spade', 'club']

"""The is comparison operator tests whether two expressions evaluate to the 
identical object.
"""

suits is nest[0] # True
suits is ['heart', 'diamond', 'spade', 'club'] # False (checks for identity)
suits == ['heart', 'diamond', 'spade', 'club'] # True (checks for equality)

"""Slicing a list creates a new list."""
a = [11, 12, 13]
b = a[1:]
b[1] = 15

"""Although the list is copied, the values contained within the list are not."""
a = [11, [12, 13], 14]
b = a[:]
b[1][1] = 15
b[0] = 10

"""More list manipulations:
1 Adding two lists together creates a new list.
2 The append() method mutates the list, increasing its length by one.
3 The extend() method mutates the list, increasing its length by the argument length.
4 The pop() method mutates the list, removing and returning the last element.
5 The remove() method mutates the list, removing the first item that is equal to the arg.
6 The index() method returns the index of the first item that is equal to the arg.
7 The insert() method mutates the list, adding the arg to the list at the given index.
8 The count() method returns how many times an item equals the argument.
"""

"""List comprehensions always creates a new list."""

"""A tuple is an instance of an immutable sequence."""
(1, 2 + 3) # (1, 5)
type( (10, 20)) # <class 'tuple'>
() # ()
(10,) # (10,)

"""Tuple methods (methods for manipulating the contents are not available)."""
code = ("up", "up", "down", "down") + ("left", "right") * 2
len(code) # 8
code[3] # 'down'
code.count("down") # 2
code.index("left") # 4

"""While it is not possible to change which elements are in a tuple. it is
possible to change the value of a mutable element contained within a tuple."""
nest = (10, 20, [30, 40])
nest[2].pop() # 40


# 2.4.3 Dictionaries
"""Dictionaries are Python's built-in data type for storing and manipulating 
correspondence relationships. A dictionary contains key-value pairs, where
both keys and values are objects.

Values inside of a dictionary are indexed by descriptive keys. 

Dictionary restrictions:
1 A key of a dictionary cannot be or contain a mutable value.
2 There can be at most one value for a given key.
"""
numerals = {'I': 1.0, 'V': 5, 'X': 10}
numerals['X'] # 10
numerals['I'] = 1
numerals['L'] = 50
numerals # {'I': 1.0, 'X': 10, 'L': 50, 'V': 5} (dictionaries are unordered until Python 3.6)

numerals.get('A', 0) # If 'A' is a key, return the corresponding value, otherwise return 0
numerals.get('V', 0)

{x: x*x for x in range(3,6)} # {3: 9, 4: 16, 5: 25}

"""The methods keys, values, and items all return iterable values."""
sum(numerals.values()) # 66

"""A list of key-value pairs can be converted into a dictionary by calling 
the dict constructor function."""
dict([(3, 9), (4, 16), (5, 25)]) # {3: 9, 4: 16, 5: 25}