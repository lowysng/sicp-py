from operator import add, mul, truediv, floordiv

print(2 + 3)
print(add(2, 3))

print(2 + 3 * 4 + 5)
print(add(add(2, mul(3, 4)), 5))

print((2 + 3) * (4 + 5))
print(mul(add(2, 3), add(4, 5)))

print(5 / 4) # error
print(truediv(5, 4))

print(5 // 4)
print(floordiv(5, 4))