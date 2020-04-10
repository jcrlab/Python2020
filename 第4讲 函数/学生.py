def student(name, ID = "20190001", 
            gender = "男", dept = "新闻学院"):
    print("姓名", name)
    print("学号", ID)
    print("性别", gender)
    print("部门", dept)
    print("------------")
    return

student("张三")
student("张三", ID = "2018201901")
student("张三", "法学院")
student("李四", "2020201901", "女")
student("张三","男")


