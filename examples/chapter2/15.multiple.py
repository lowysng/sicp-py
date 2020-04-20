# 2.7.3 Multiple Representations
"""In certain cases there might be more than one useful
representation for a data object.
"""

# Example: Representing complex numbers
"""Complex numbers may be represented in two ways:
1 rectangular form (real and imaginary parts)
2 polar form (magnitude and angle)
"""

# Start at the highest level of abstraction
"""A Complex number is a Number, and numbers can be 
added or multiplied together.

Notes about the Number objects:
- they must have add and mul methods
- purpose is not to be instantiated directly
"""
class Number:
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mul(other)

# Define add() and mul() for complex numbers
"""Notes:
- this implementation assumes that two classes exist for complex numbers
"""
class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)

# Python @property decorators
"""Used to compute the other representation whenever it is
needed.
"""
from math import atan2
class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

ri = ComplexRI(5, 12)
ri.real # 5
ri.magnitude # 13.0

from math import sin, cos, pi
class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)

ma = ComplexMA(2, pi/2)
ma.imag # 2.0

# Implementation complete
"""Note that both ComplexRI and ComplexMA share the same interface:
1 .real
2 .imag
3 .magnitude
4 .angle
"""
from math import pi 
ComplexRI(1, 2) + ComplexMA(2, pi/2) # ComplexRI(1, 4)
ComplexRI(0, 1) * ComplexRI(0, 1) # ComplexMA(1, 1 * pi)