from random import randint
tahed = ["a","b","c","d","e"]
valjund = ""
with open("tahed.txt","w") as fail:
    for i in range(randint(1,4000)):
        valjund += tahed[randint(0,len(tahed)-1)]
    fail.write(valjund)