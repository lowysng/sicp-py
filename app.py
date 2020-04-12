def remove_last_digit(num):
    return num // 10

def get_nth_digit(num, n):
    return (num % pow(10, n)) // pow(10, n - 1)

def get_last_digit(num):
    return get_nth_digit(num, 1)

def get_first_digit(num):
    if num < 10:
        return num
    return get_first_digit(remove_last_digit(num))


print(get_nth_digit(12353, 2))
print(get_first_digit(12353))
print(get_last_digit(12353))