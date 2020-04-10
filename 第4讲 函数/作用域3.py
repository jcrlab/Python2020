
x = [1,2,3]
print("x = %s, x 的地址：%d" % (str(x), id(x)))
def fun(y):
    print("y = %s, y 的地址：%d" % (str(y), id(y)))
    y.append(0)
    return

fun(x)
print("x = %s, x 的地址：%d" % (str(x), id(x)))
print(x)