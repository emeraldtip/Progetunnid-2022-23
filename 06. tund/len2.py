nimekiri = []
pikimsõna = ""
sõnapikkus = 0
for i in range(10):
    sisend = input("sisesta sõna: ")
    if len(sisend) > sõnapikkus:
        pikimsõna = sisend
        sõnapikkus = len(sisend)
print(pikimsõna)
