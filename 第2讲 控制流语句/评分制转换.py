# 百分制转换为五级评分制

score = float(input("请输入成绩："))

grade = ""

if score <= 100:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 0:
        grade = "E"
    else:
        print("输入成绩需要 >= 0")
else:
    print("输入成绩需要 <= 100")

print("五级评分制为：", grade)