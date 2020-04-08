n = int(input("请输入一个正整数："))
 
a, b, fn = 1, 1, 1
# sn = 1 if n==1 else 2
if n== 1:
    sn = 1
else:
    sn = 2

count = 3
while count <= n:
    fn = a + b
    a = b
    b = fn
    sn = sn + fn
    count = count + 1

print("F(%d) = %d" % (n, fn))
print("S(%d) = %d" % (n, sn))

