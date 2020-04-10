f1 = lambda x, n : x ** n
f2 = lambda x : x if x >= 0 else -x
f3 = lambda x, y : x * y

print(f1(2,3))
print(f2(-3))
print(f3(-3, 4))
