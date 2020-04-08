USERNAME = "admin"
PASSWORD = "123"

count = 1
while count <= 3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == USERNAME and password == PASSWORD:
        print("Success!")
        break
    elif count == 3:
        print("Fail!")
    else:
        print("Wrong username or password!")
    count = count + 1

