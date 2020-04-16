# 2.5.5 Inheritance
"""We can use inheritance to define similar classes that differ in their
amount of specialization.

The subclass (also child class) inherits the attributes of its bas class
(also parent class or superclass). Attributes may be overriden.

Inheritance represents a is-a relationship between classes, which contrasts
with a has-a relationship. 

A checking account is a specific type of account.
A bank object has a list of account objects.
"""

# 2.5.6 Using Inheritance
class Account:
    """A bank account that has a non-negative balance."""
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)

checking = CheckingAccount('Sam')
print(checking.deposit(10))
print(checking.withdraw(5))

# Interfaces
"""An object interface is a collection of attributes and conditions on those attributes."""

# 2.5.7 Multiple Inheritance
"""Python supports the concept of a subclass inheriting attributes from mutliple base 
classes."""
class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1

such_a_deal = AsSeenOnTVAccount("John")
such_a_deal.balance         # 1
such_a_deal.deposit(20)     # 19 ($2 fee from SavingsAccount.deposit)
such_a_deal.withdraw(5)     # 13 ($1 fee from CheckingAccount.withdraw)


# 2.5.8 The Role Of Objects
"""Objects make data abstraction and message passing both convenient and flexible.
They promote a separation of concerns, each object encapsulates and manages
some part of the program's state.

OOP is particularly well-suited to programs that model systems that have separate
but interacting parts.

On the other hand, classes may not provide the best mechanism for implementing 
certain abstractions (functions are more straightforward for representing relationships
between inputs and outputs).

Python is a multi-paradigm language, learn to match the correct organizational paradigms to
different problems. 
"""