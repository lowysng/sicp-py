# 1.7 Recursive functions
# Computing the sum of the digits of a natural number
def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n

# 1.7.2 Mutual Recursion
# Computing the parity of an integer
# - a number is even if it is one more than an odd number
# - a number is odd if it is one more than an even number
# - 0 is even
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)
    
def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)

# 1.7.3 Printing in Recursive Functions
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n - 1)

def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
        play_alice(n - 2)
    else:
        play_alice(n - 1)

play_alice(20)

# 1.7.4 Tree Recursion
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)