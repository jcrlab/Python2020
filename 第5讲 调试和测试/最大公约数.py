def gcd(x, y):
    assert x >= y
    #print("(%d, %d)" % (x, y))
    if x % y == 0:
        return y
    else :
        return gcd(y, x%y)

a, b = input().split()
a, b = int(a), int(b)
#if a < b:
#    a, b = b, a

print(gcd(a, b))


