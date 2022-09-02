from pyrsistent import b


a = [1,2,3,4,5]
b = list()

for i in a:
    b.append(i)
print(b)    


"""    or we can use list comprehension   """

a = [ 1,2,3,4,5]

b = [i for i in a]

print(b)

"""  OR   """

a = [(1,2),(3,4),(5,6)]

b = [i * j for (i,j) in a]

print(b)