R = int(input("Dê a quantidade de R: "))
M = int(input("Dê a quantidade de M: "))
V = int(input("Dê a quantidade de V: "))

total = R*1 + M*2 + V*3

if total >= 150:
    print("R")
elif total >= 120:
    print("M")
elif total >= 100:
    print("V")
else:
    print("N") 