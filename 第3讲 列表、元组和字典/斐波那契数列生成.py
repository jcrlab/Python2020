n = int(input("请输入正整数 n = "))
# L = [1] if n == 1 else [1, 1]
if n == 1:
    L = [1]
else:
    L = [1, 1]

for i in range(2, n):
    # L.append(L[-2] + L[-1])
    fn = L[-2] + L[-1]
    L.append(fn)
    
print(L)

