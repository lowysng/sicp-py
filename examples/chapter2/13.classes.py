# 2.6 Implementing Classes and Objects
"""In this section we implement classes and objects using just functions
and dictionaries."""

# 2.6.1 Instances
"""Instance has named attributes, which can be set and retrieved."""

def make_instance(cls):
    """Return a new object instance, which is a dispatch dictionary."""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)
    def set_value(name, value):
        attributes[name] = value
    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance

def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise."""
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value

i = make_instance('x')          # constructing an instance
i['set']('balance', 10)         # i.balance = 10
i['get']('balance')             # i.balance

# 2.6.2 Classes
def make_class(attributes, base_class=None):
    """Return a new class, which is a dispatch dictionary."""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    def set_value(name, value):
        attributes[name] = value
    def new(*args):
        return init_instance(cls, *args)
    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls

def init_instance(cls, *args):
    """Return a new object with type cls, initialized with args."""
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance


# 2.6.3 Using Implemented Objects
def make_account_class():
    """Return the Account class, which has deposit and withdraw methods."""
    interest = 0.02
    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 0)
    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        new_balance = self['get']('balance') + amount
        self['set']('balance', new_balance)
        return self['get']('balance')
    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        balance = self['get']('balance')
        if amount > balance:
            return 'Insufficient funds'
        self['set']('balance', balance - amount)
        return self['get']('balance')
    return make_class(locals())

Account = make_account_class()              # instantiating an account
kirk_account = Account['new']('Kirk')       # creating an instance
kirk_account['get']('holder')               # 'Kirk'
kirk_account['get']('interest')             # 0.02
kirk_account['get']('deposit')(20)          # 20
kirk_account['get']('withdraw')(5)          # 15

"""Setting an attribute of an instance does not change the corresponding attribute 
of its class.
"""
kirk_account['set']('interest', 0.04)
Account['get']('interest')                  # 0.02

"""Subclasses are created by overloading a subset of the class attributes."""
def make_checking_account_class():
    """Return the CheckingAccount class, which imposes a $1 withdrawal fee."""
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        fee = self['get']('withdraw_fee')
        return Account['get']('withdraw')(self, amount + fee)
    return make_class(locals(), Account)

CheckingAccount = make_checking_account_class()
jack_acct = CheckingAccount['new']('Spock')
jack_acct['get']('interest')                # 0.01
jack_acct['get']('deposit')(20)             # 20
jack_acct['get']('withdraw')(5)             # 14