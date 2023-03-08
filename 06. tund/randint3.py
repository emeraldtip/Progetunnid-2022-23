from random import randint
arv = randint(0,100)
arvatud = False
while arvatud == False:
    sisend = int(input("arva arv: "))
    if sisend > arv:
        print("Arv on väiksem")
    elif sisend < arv:
        print("Arv on suurem")
    else:
        arvatud = True
        print("Arvasid arvu ära")
