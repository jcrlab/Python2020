x = 3
def fun1(x):
    x = 2
    def fun2(x):
        x = 1
    fun2(x)
    print(x)
    return

fun1(x)
print(x)