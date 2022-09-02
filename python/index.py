a = int(input("kilonuzu giriniz: "))
b = float(input("boyunuzu giriniz: "))

BKI = a / b * b
if BKI < 18.5:
    print("zayif")
elif BKI >= 18.5 and BKI < 25:
    print("Normal")
elif BKI >= 25 and BKI < 30:
    print("Fazla kilolu")
else:
    print("Obez")            

