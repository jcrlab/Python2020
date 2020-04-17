def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True
    return

def count_prime(n):
    num = 0
    for i in range(2, n+1):
        if is_prime(i):
            num = num + 1

    return num

N = int(input())
print(count_prime(N))
