def gcd(x, y):
    if x % y == 0:
        return y
    else :
        return gcd(y, x%y)

a, b = input().split()
c = gcd(int(a), int(b))
print(c)