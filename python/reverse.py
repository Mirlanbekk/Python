


a = input()
l = len(a)  # length of a string.
k = []

for i in range(l-1,-1,-1):  #1st element starting point. 2sd ending element. 3th increment or decrement.
    k.append(a[i])  
r = "".join(k)   # convert list elements to a single string.
print(r)    


