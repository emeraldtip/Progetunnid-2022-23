numbrid = {}
valik = 0
menu = """1. Prindi numbrid
2. Lisa Number
3. Eemalda Number
4. Otsi Numbrit
5. Välju"""#Multiline string, kui keegi seda mäletab.
while True:
    print(menu)
    try: #kui kasutaja sisestab nt. stringi inti asemel
        valik = int(input("Sisesta valik (1-5): "))
    except:
        valik = 0 #Kasutame ära enne eksisteerivat koodi
    if valik == 1:
        print("Numbrid:")
        for x in numbrid.keys():
            print("Nimi: ", x, "\tNumber:", numbrid[x],"\n") # kui \n on newline siis \t on tab
    elif valik == 2:
        print("Lisa nimi ja number")
        nimi = input("Nimi: ")
        number = input("Number: ")
        numbrid[nimi] = number
    elif valik == 3:
        print("Eemalda nimi ja Number")
        nimi = input("Nimi: ")
        if nimi in numbrid:
            del numbrid[nimi]
        else:
            print("------------------\nNime ei eksisteeri\n------------------")
    elif valik == 4:
        print("Otsi numbrit")
        nimi = input("Nimi: ")
        if nimi in numbrid:
            print("Number on", numbrid[nimi])
        else:
            print("------------------\nNime ei eksisteeri\n------------------")
    elif valik == 5:
        exit() #väljub programmist
    else:
       print("-------------------\nValik pole valiidne\n-------------------") #teine viis multiline stringi tegemist
