print("""***************
User Entry
**************
""")

sys_user_name   = "mirlanbek"
sys_password    = "12345"

user_name   = input("Entry your user name: ")
password    = input("Entry your password: ")

if (user_name != sys_user_name and password == sys_password):
    print("user_name is wrong...")

elif (user_name == sys_user_name and password != sys_password):
    print("password is wrong...") 

elif (user_name != sys_user_name and password != sys_password):
    print("user_name and password is wrong...") 

else:
    print("you pass...")          

