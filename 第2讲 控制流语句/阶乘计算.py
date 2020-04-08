# 使用 while 循环计算 n 的阶乘

n = int(input("输入一个整数："))
s = 1
i = 1

while i <= n:
    s = s * i
    i = i + 1

print("%d! = %d" %(n, s))
    