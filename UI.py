

import time

i = True
while i == True:
    
    i = int(input('Enter 1 to generate new image or 2 to exit: '))

    if i == 2:
        break

    f = open('prng-service.txt', "w")
    f.write("run")
    f.close()

    for num in range(5):
        print("*")
        time.sleep(1)
    
    print("\n Wrote run to prng-service.txt! \n")

    f = open('prng-service.txt', "r")
    line = f.readline()
    
    g = open('image-service.txt', "w")
    g.write(line)
    g.close()
    
    for num in range(5):
        print("*")
        time.sleep(1)
    
  
    h = open('image-service.txt', "r")
    pathh = h.readline()
    h.close()

    print("\n DONE!!")
    print("Path for image is: ", pathh)
    
    
    f.close()
    g.close()






