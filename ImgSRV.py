

import time

i = True
while i == True:

    f = open('image-service.txt', "r")
    line = f.readline()

    time.sleep(1)
    print(" - Wating for value -")

    if line.isnumeric():

        current = line
        f.close()

        f = open('image-service.txt', "w")
        f.write("C:\\Users\\IamPi\\OneDrive\\Desktop\\OSU - CS Classes\\CS361 - Software Engineering 1\\Assignment1 - with python\\Images\\image" + current + ".jpg")

f.close()
