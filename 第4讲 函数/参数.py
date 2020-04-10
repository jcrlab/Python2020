
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def sum_power(*numbers, name):
    print(name)
    print(numbers)
    print(type(numbers))
    s = 0
    for n in numbers:
        s = s + n * n
    return s
