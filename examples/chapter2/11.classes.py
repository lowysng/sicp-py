# 2.5.1 Objects and Classes
"""A class serves as a template for all objecst whose type is that class.

The objects we have used so far all have built-in classes, but user-defined
classes can be created as well. A class definition specifies the attributes
and methods shared among objects of that class.
"""

"""Instantiating a class."""
# a = Account('Kirk')

"""Accessing attributes of an object."""
# a.holder # 'Kirk'
# a.balance # 0

"""Accessing methods of an object."""
# a.deposit(15) # 15
# a.withdraw(10) # 5
# a.balance # 5
# a.withdraw(10) # 'Insufficient funds'


# 2.5.2 Defining Classes
"""Classses are typically organized around manipulating instance attributes,
which are the name-value pairs associated with each instance of that class.
"""

"""The constructor of a class is the method that initializes objects of that class."""
class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

a = Account('Kirk')
a.balance # 0
a.holder # 'Kirk'
a.deposit(100) # 100
a.withdraw(90) # 10
a.withdraw(90) # 'Insufficient funds'


# 2.5.3 Message Passing and Dot Expressions
"""Methods and instance attributes are the fundamental elements of OOP.

The central idea in message passing was that data values should have behavior
by responding to messages that are relevant to the abstract type they represent.

Dot notation is a syntactic feature of Python that formalizes the message passing
metaphor.

Dot expression: <expression>.<name>

Dot expressions evaluate to the value of the attribute with the given <name>, for
the object that is the value of the <expression>.

getattr() is the function equivalent of dot notation.
"""
getattr(a, 'balance') # 10 (equivalent to expression => a.balance)
hasattr(a, 'deposit') # True

"""Attributes of an object include:
1. all instance attributes
2. all attributes (including methods) defined in its class

When methods are invoked on an object, the object is implicitly pass as the
first argument to the method. The object is bound to the parameter self.

Python distinguishes functions and bound methods, which couple together a function
and the object on which that method will be invoked.

These two results differ only in the fact that the first is a standard two-argument
function with parameters self and amount. The second is a one-argument method, where
then name self will be bound to the object automatically when the method is called,
which the parameter will be bound to the argument passed to the method.
"""
type(Account.deposit) # <class 'function'>
type(a.deposit) # <class 'method'>


# 2.5.4 Class Attributes
"""Class attributes (static variables) are attribute values that are shared scross 
all objects of a given class.

Class attributes are created by assignment statements.
"""
class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

# Evaluating dot expressions
"""To evaluate a dot expression, <expression>.<name>:
1 Evaluate the <expression> on the left of the dot, which yields the object.
2 <name> is matched against the instance attributes of that object
3 <name> is matched against the class attributes
4 if attribute is a function, a bound method is returned instead
"""

# Attribute assignment
a.interest = 0.08           # here we created a new instance attr (same name as class attr)
Account.interest            # 0.02 (class attr unchanged)
Account.interest = 0.05     # here we changed the class attr
