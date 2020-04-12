def extract_last(num):
    if num < 10: 
        return num
    return num % 10

def remove_last(num):
    if num < 10:
        return num
    return num // 10

def extract_first(num):
    if num < 10:
        return num
    return extract_first(remove_last(num))

test = 7576
print(extract_first(test))
print(extract_last(test))