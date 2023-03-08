with open("Midagi.txt","w+") as file:
    file.write("ahaha")
    file.seek(0) #liigutab kursori faili algusesse, muidu kursor faili lõpus, lugemist ei toimu
    print(file.readlines())