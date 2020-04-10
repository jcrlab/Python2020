
x = 3
print("x = %d, x 的地址：%d" % (x, id(x)))
def fun(x):
    x = -x
    print("x = %d, x 的地址：%d" % (x, id(x)))
    

fun(x)
print("x = %d, x 的地址：%d" % (x, id(x)))
print(x)




# print("x = %d, x 的地址：%d" % (x, id(x)))