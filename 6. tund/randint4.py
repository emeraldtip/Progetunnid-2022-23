from random import randint
tähed = ["a","e","k","i","o","m","n"]
sõna = ""
for i in range(randint(0,15)):
    sõna = sõna + tähed[randint(0,len(tähed)-1)]
print(sõna)