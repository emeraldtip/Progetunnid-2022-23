def burh():
    Arvud = {}
    with open(input("Palun sisestage sisendfaili nimi: "),"r") as file:
        for line in file:
            a = line.split(" : ")
            Arvud[a[0]] = Arvud.get(a[0],0)+int(a[1])
    print(max(Arvud, key=Arvud.get)+" "+str(max(Arvud.values())))
    with open(input("Palun sisestage väljundfaili nimi: "),"w") as file:
        file.writelines([taht + " : " + str(arv)+"\n" for taht,arv in Arvud.items()])
burh()
while True:
    if(input("Kas soovid programmi uuesti jooksutada? ").lower()=="ei"):
        exit()
    else:
        burh()