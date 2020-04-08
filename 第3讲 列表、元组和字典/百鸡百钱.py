S = "公鸡%d只、母鸡%d只、小鸡%d只；"

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5*x + 3*y + z/3 == 100:
            print(S % (x, y, z))
print("执行结束！")
