# Coercion
"""Another way (see 17.type_dispatching) of implementing cross-type operations 
is to view one type as another type. This process is called coercion.
Coercion requires that the different data types too be not completely
independent.

Advantages:
- coercion requires only one function for each pair of types
- more sophisticated coercion schemes:
    => coercing two different types into third common type
    => iterative coercion

Drawbacks:
- coercion function can lose information when they are applied
"""

# Coercion function
"""This coercion function transforms a rational number to a complex
number with zero imaginary part.
"""
def rational_to_complex(r):
    return ComplexRI(r.numer/r.denom, 0)

from coercion import Rational, ComplexRI, ComplexMA
from math import pi
ComplexRI(1.5, 0) + Rational(3, 2) # 'ComplexRI(3, 0)'
Rational(-1, 2) * ComplexMA(4, pi/2) # 'ComplexMA(2, 1.5 * pi)'