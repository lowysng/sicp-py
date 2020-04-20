# 2.7.1 String Conversion
"""An object value should behave like the kind of data it is meant
to represent, including product a string representation of itself.

Python stipulates that all objects should produce two different string
representations: 
1 human interpretable text
2 python interpretable text
"""
repr(12e12) # this is what python prints in an interactive session
repr(min) # '<built-in function min>'

from datetime import date
tues = date(2011, 9, 12)
repr(tues) # 'datetime.date(2011, 9, 12)'
str(tues) # '2011-09-12'

"""the repr function always invokes the __repr__() method on its argument."""
tues.__repr__() # 'datetime.date(2011, 9, 12)' (same as repr(tues))
tues.__str__() # '2011-09-12' (same as str(tues))

"""repr() and str() are polymorphic functions: they apply to multiple data types."""


# 2.7.2 Special Methods
"""In Python, certain special names are invoked by the Python interpreter
in special circumstances.

__init__() method is automatically invoked whenever an object is constructed
__str__() method is invoked when printing
__repr__() method is invoked in an interactive session
__bool__() method is invoked to determine the truth value of objects
__len__() method is invoked to determine the objects length
__getitem__() method is invoked by the element selection operator
__call__() method creates an object that behaves like a function
"""

class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def __str__(self):
        return '(str) This account belongs to ' + self.name + '.'
    def __repr__(self):
        return '(repr) This account belongs to ' + self.name + '.'
    def __bool__(self):
        return self.balance != 0
    def __len__(self):
        return self.balance
    def __call__(self):
        return self.name
    def __add__(self, other):
        return self.balance + other.balance

kirk = Account('Kirk')
bool(kirk) # False
kirk.balance = 10
bool(kirk) # True
len(kirk) # 10
kirk() # 'Kirk'
spock = Account('Spock')
spock.balance = 42
kirk + spock # 52