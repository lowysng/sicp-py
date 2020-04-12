def pressure(v, t, n=6.022e23):
    """Compute the pressure in pascals of an ideal gas.

    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particules of gas
    """
    k = 1.38e-23 # Boltzmann's constant
    return n * k * t / v

print(pressure(1, 273.15))
print(pressure(1, 273.15, 3 * 6.022e23))