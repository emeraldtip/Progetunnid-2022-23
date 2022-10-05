a = input("Sisestage tehtemärk: ")
yks = int(input("Sisestage esimene arv: "))
kaks = int(input("Sisestage teine arv: "))
if a == "+":
    print(yks+kaks)
elif a == "-":
    print(yks-kaks)
elif a == "*":
    print(yks*kaks)
elif a == "/":
    print(yks/kaks)
else:
    print("Tehtemärk ei sobi")