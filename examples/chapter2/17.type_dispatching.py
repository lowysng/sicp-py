# Cross-type operation
"""We want to be able to add a rational number to a complex
number.
"""

# Type Dispatching
"""One way to implement cross-type operations is to select
behavior based on the types of the arguemnts to a function 
or method.
"""
from type_dispatch import Complex, ComplexRI, ComplexMA
c = ComplexRI(1, 1)
isinstance(c, ComplexRI) # True
isinstance(c, Complex) # True

from math import pi
def is_real(c):
    """Return whether c is a real number with no imaginary part."""
    if isinstance(c, ComplexRI):
        return c.imag == 0
    elif isinstance(c, ComplexMA):
        return c.angle % pi == 0

is_real(ComplexRI(1, 1)) # False
is_real(ComplexMA(2, pi)) # True

from type_dispatch import Rational
ComplexRI(1.5, 0) + Rational(3, 2) # 'ComplexRI(3, 0)'
Rational(-1, 2) * ComplexMA(4, pi/2) # 'ComplexMA(2, 1.5 * pi)'