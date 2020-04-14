# 2.4.10 Generators
"""A generator is an iterator returned by a special class of funtion called
a generator function. Generator functions use yield statements (as opposed to
return statements) to return elements of a series.
"""

def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current)+1)

letters = letters_generator()
type(letters) # <class 'generator'> (remember: a generator is the same as an iterator)
print(next(letters))
print(next(letters))