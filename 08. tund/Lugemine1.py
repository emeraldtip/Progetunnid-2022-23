#eeldan, et oled tekstifaili loonud
#teekonda ainult siis vaja kui pole samas kaustas kus programm jookseb, muidu saab lihtsalt failinime panna

#10 tähte
nimi = input("Sisesta faili nimi (vajadusel koos tekonnaga): ")
with open(nimi,"r",encoding="UTF8") as fail:
    print(fail.read(10))

#5 rida (avame faili uuesti, et otsast alustada)
with open(nimi,"r",encoding="UTF8") as fail:
    for i in range(5):
        print(fail.readline())

#kõik read
with open(nimi,"r",encoding="UTF8") as fail:
    read = fail.readlines()
    for i in range(len(read)-1,-1,-1): #esimene len(read)-1 - võtame ridade arvu. Kuna python alustab lugemist 0ist ss pythoni jaoks on viimane täht indeksiga ridade arv -1 ja esimene on 0. Teine arv näitab, mille juures lõpetatakase. Kuna meie tahame lugeda kõik alates indeksist pikkus - 1  kuni 0, siis et see kõk need üle kordaks peame minema ühe võrra üle ehk -1. Viimane -1 tähistab, et iga tsükliga lahutatakse 1.
        print(read[i])