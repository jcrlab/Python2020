"""
模拟用户名、密码输入

允许的用户名和密码有：
    admin / 123456
    root  / toor
"""

username = input("username: ")
password = input("password: ")

if username == "admin":
    if password == "123456":
        print("Success !")
    else:
        print("Wrong password!")
elif username == "root":
    if password == "toor":
        print("Success !")
    else:
        print("Wrong password!")
else:
    print("Wrong username!")

