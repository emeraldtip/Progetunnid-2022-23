def listLiit(nimekiri):
    summa = 0
    for i in nimekiri:
        summa = summa + i
    return summa

def tagurpidistaja(sone):
    tagurpidi = ""
    for i in range(len(sone)-1,-1,-1):
        tagurpidi+=sone[i]
    return tagurpidi
print(tagurpidistaja("eoooo"))
print(listLiit([0,1,2,6,7,8,9,0,4,32,3,6,8,9,4,3,2]))