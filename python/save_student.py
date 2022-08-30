from jinja2 import TemplateAssertionError


print("save student list")

name = input("student name:")
last_name = input("student last_name:")
team = input("student team:")

info = [name,last_name,team]


print("save info....")

print("studen name: {}\nstudent last_name: {}\nstudent team: {}\n".format(info[0],info[1],info[2]))

print ("save info already.....")