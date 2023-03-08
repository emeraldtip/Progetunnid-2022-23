loop = True
read = []
while loop:
    a = input("Sisesta rida: ") + "\n"
    if a == "stop\n":
        loop = False
    else:
        read.append(a)

with open("kasutajakirjutab.txt","w") as file:
    file.writelines(read)