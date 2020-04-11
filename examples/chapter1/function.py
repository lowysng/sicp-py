def square(x):
    return x * x

print(square(21))
print(square(2 + 5))
print(square(square(3)))

def sum_squares(x, y):
    return square(x) + square(y)

print(sum_squares(3, 4))