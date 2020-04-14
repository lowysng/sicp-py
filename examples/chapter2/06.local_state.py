# 2.4.4 Local State
"""Like lists and dictionaries, functions can also have local states.

To do this we can use the nonlocal statment. Note: functions that
use nonlocal statements are non-pure.
"""

def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""
    def withdraw(amount):
        nonlocal balance # balance inside withdraw() refers to values outside the local frame
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

withdraw = make_withdraw(100)
print(withdraw(25))
print(withdraw(25))
print(withdraw(60))
print(withdraw(15))