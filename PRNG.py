
# WHILE LOOP LOGIC

import random
random.seed(0)

import time


i = True
while i == True:

    print(" - Waiting for run - ")
    time.sleep(3)

    f = open('prng-service.txt', "r")
    line = f.readline()
   
    if line == "run":
        
        value = random.randint(1, 5)
        value = str(value)
        f.close()

        f = open('prng-service.txt', "w")
        f.write(value)

    f.close()
        






print("DONE")