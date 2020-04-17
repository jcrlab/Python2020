def isPal(x):
    temp = x[::-1]
    id1 = id(x)
    id2 = id(temp)
    if temp == x:
        return True
    else:
        return False

text = input()

if isPal(list(text)):
    print("Yes")
else:
    print("No")


