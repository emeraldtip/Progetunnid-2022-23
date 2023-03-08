from datetime import datetime
while True:
    a = input("Postitus: ")
    with open("logi.txt","a") as file:
        file.write(str(datetime.now())+": "+ a + "\n")


