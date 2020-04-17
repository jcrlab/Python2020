# 素数个数统计程序
# 作者：麒麟
# 时间：2020/4/14 20:00

def is_prime(x):
    # 功能：判断输入的正整数是否是素数
    # 输入：一个正整数 x
    # 返回：如果x是素数，返回 True；否则返回 False
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
    # 功能：统计不大于 n 的素数个数
    # 输入：一个正整数 n
    # 返回：返回1到n之间的素数个数，不包括1或n
    num = 0
    for i in range(2, n+1):
        if is_prime(i):
            num = num + 1

    return num

# 编写测试函数
def test(name, num_in, num_out):
    if count_prime(num_in) == num_out:
        print("%s 测试通过！" % name)
    else:
        print("%s 测试失败，未通过 <%d,%d>" % (name, num_in,num_out))

# 编写测试用例
test("Test 1",  1,  0)
test("Test 2",  2,  1)
test("Test 3", 32, 11)
test("Test 4", 72, 20)

