numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

# test
print("Test:")
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))

print("-" * 40)


# custom definitions


def summary():
    result = 0
    for number in numbers:
        result += number
    print(result)


def min_num():
    x = 0
    for number in numbers:
        result = number
        if result < x:
            x = result
    print(x)


def max_num():
    x = 0
    for number in numbers:
        result = number
        if result > x:
            x = result
    print(x)


def avg():
    result = 0
    for number in numbers:
        result += number
    x = float(result / len(numbers))
    print(x)


min_num()
max_num()
summary()
avg()