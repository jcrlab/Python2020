def student(name, id = "20190001", gender = "男", dept = "新闻学院"):
    print("姓名", name)
    print("学号", id)
    print("性别", gender)
    print("部分", dept)
    print("------------")
    return

student("张三")
student("张三", id = "2018201901")
student("张三", dept = "法学院")
student("李四", id = "2020201901", gender = "女")


