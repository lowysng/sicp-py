# 2.4.11b Implementing a dictionary
"""A dictionary has a similar behavior to linked list (09.mutable_list.py).

Note: this implementation of a dictionary is not optimized for a fast record 
lookup.
"""

def dictionary():
    """Return a functional implementation of a dictionary."""
    records = []

    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value

    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)

    return dispatch

d = dictionary()
d('setitem', 3, 9)
d('setitem', 4, 16)
d('getitem', 3) # 9
d('getitem', 4) # 16


# 2.4.12 Dispatch dictionaries
"""The built-in dictionary data type provides a general method for looking up 
a value for a key. Instead of using conditionals to implement dispatching, we 
can use dictionaries with string keys.

To illustrate this, we will implement a mutable data type below called account.
It has a constructor account(), and selector check_balance(), as well as functions
to depost() or withdraw() funds.
"""

def account(initial_balance):

    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']

    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    
    dispatch = {
        'deposit': deposit,
        'withdraw': withdraw,
        'balance': initial_balance
    }

    return dispatch

def withdraw(account, amount):
    return account['withdraw'](amount)

def deposit(account, amount):
    return account['deposit'](amount)

def check_balance(account):
    return account['balance']

a = account(20)
deposit(a, 5)
withdraw(a, 17)
check_balance(a) # 8