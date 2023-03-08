numbrid = []
a = True
while a == True:
    vaartus = input("Sisesta üks arv: ")
    if vaartus == "STOP":
        a = False
    else:
        numbrid.append(int(vaartus))
numbrid.sort()
for arv in numbrid:
    print(arv)
