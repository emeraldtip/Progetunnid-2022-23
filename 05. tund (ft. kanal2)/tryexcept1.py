asi = True
while asi: #lühem viis kirjutada asi == true (tegelikult tekitab == operaator justkui booleani - ehk true v false, nii et see on väga loogiline)
    try:
        a = int(input("Sisesta esimene arv: "))
        asi = False
    except:
        print("Sisend pole arv")
asi = True #resetime ära selle
while asi: 
    try:
        b = int(input("Sisesta teine arv: "))
        asi = False
    except:
        print("Sisend pole arv")

#Juhin tähelepanu, et kui tegeletakse teiste programmeerimsikeeltega, mis ei ole phython, siis peaksid mõlemad muutujad - a ja b olema väljaspool while loope juba määratud olema, muidu neid üldkonkekstis ei eksisteeriks ja nendega ei saa hiljem enam midagi teha. Python on aga selliste asjade puhul väga paindlik

print("Tulemus on: " + str(a+b)) #kui kasutada + operaatorit stringide puhul, tuleb arvud ümber convertida stringideks