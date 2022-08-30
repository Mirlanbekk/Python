print("""
******************************************
Calculator program

Calculator;

1. add
2. extraction
3. multiplication
4. divide
******************************************
""")


a = int(input("First Number: "))
b = int(input("Second Number: "))

operation = input("Choose your operation: ")

if operation == "+":
    print("{} with {} total add {}".format(a,b,a + b))

elif operation == "-":
    print("{} with {} total extraction {}".format(a,b,a - b))

elif operation == "*":
    print("{} with {} total multiplication {}".format(a,b,a * b))

elif operation == "/":
    print("{} with {} total divide {}".format(a,b,a / b))

else:
    print ("Wrong operation.")            
