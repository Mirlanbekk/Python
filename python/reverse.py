


a = input()
l = len(a)  # length of a string.
k = []

for i in range(l-1,-1,-1):  
    k.append(a[i])
r = "".join(k)   # convert list elements to a single string.
print(r)    