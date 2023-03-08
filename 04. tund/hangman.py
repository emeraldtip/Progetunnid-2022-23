sona = "allmaaraudtee"

valjund = []
for x in sona:
    valjund.append("_")

katseid = 8
while katseid > 0:
    print("".join(valjund))
    sisend = input()
    if sisend == sona: 
        katseid = -1
        print("Palju õnne, sa võitsid")
    elif sisend in sona:
        for e in range(len(sona)):
            if sisend == sona[e]:
                valjund[e]=sisend
        if "".join(valjund) == sona:
              katseid = -1
              print("Palju õnne, sa võitsid")
    else:
        katseid -= 1
        print("Vale vastus " + (8-katseid)*"x")
            
if katseid == 0:
    print("Oled mängu kaotanud. L")
