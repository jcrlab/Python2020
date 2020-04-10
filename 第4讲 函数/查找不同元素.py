s = input().split(";")
A = s[0].split(" ")
B = s[1].split(" ")

# 解法 1: （A∪𝐵）∩⌝𝑍
Z = [i for i in A if i in B]
C = [j for j in A + B if j not in Z]

# 解法 2: （A∩⌝𝑍）∪(𝐵∩⌝𝑍)
Z = [i for i in A if i in B]
X = [j for j in A if j not in Z]
Y = [k for k in B if k not in Z]
C = X + Y

# 转化为 int 类型, 并排序
C = [int(t) for t in C]  # C = map(int, C)
C.sort()
C = [str(t) for t in C]

# Lambda 表达式排序
C.sort(key = lambda x: int(x))

print(" ".join(C))
# for i in C:
#     print(i, end=" ")