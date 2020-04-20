# 2.7.4 Generic Functions
"""Generic functions are methods or functions that apply
to arguments of different types.

Using interfaces and message passing (15.multiple.py) is only
one of several methods used to implement generic functions.

In this section we consider the other two: type dispatching and
type coercion.
"""
class Number:
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mul(other)

from math import gcd
class Rational(Number):
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g
        self.type_tag = 'rat'
    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)
    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)
    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

Rational(2, 5) + Rational(1, 10) # 'Rational(1, 2)'
Rational(1, 4) + Rational(2, 3) # 'Rational(1, 6)'