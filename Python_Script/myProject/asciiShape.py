#!/usr/bin/python3

l = 10

a = "*"

for i in range(l):
    for j in range(l-i):
        print(" ", end='')
    print(a)
    a += "**"


l -= 1
space = 1
aNum = ((l*2)-1)
a = "*" * aNum
for i in range(l):
    print(" " + space * " " + a)
    aNum -= 2
    a = "*" * aNum
    space += 1
