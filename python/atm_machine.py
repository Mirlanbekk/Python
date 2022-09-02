print(""" **********************

Welcome to ATM.

Transaction;

1. check your balance
2. deposit money
3. withdraw money

For quit press q

***********************
""")

balance = 1000

while True:
    process = input("Select transaction:")

    if (process == "q"):
        print("Have a good day...")
        break
    elif (process == "1"):
        print("Balance {} $".format(balance))
    elif (process == "2"):
        amount = int(input("The amount you want to deposit:"))

        balance += amount

    elif (process == "3"):
        amount = int(input("The amount you want to:"))
        if (balance - amount < 0):
            print("you can't get that much money...")
            print("Your balance {} $".format(balance))
            continue
        balance -= amount

    else:
        print("please enter the valid transaction")           

