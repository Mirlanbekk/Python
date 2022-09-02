from errno import ENETRESET


print("""***************
User Entry
**************
""")

sys_user_name   = "mirlanbek"
sys_password    = "12345"
enter_time      = 3

while True:

    user_name   = input("Entry your user name: ")
    password    = input("Entry your password: ")

    if (user_name != sys_user_name and password == sys_password):
        print("user_name is wrong...")
        enter_time -= 1

    elif (user_name == sys_user_name and password != sys_password):
        print("password is wrong...")
        enter_time -= 1


    elif (user_name != sys_user_name and password != sys_password):
        print("user_name and password is wrong...")
        enter_time -= 1
  

    else:
        print("you pass...")
        break

    if (enter_time == 0):
        print("your account is blocked")
        break



