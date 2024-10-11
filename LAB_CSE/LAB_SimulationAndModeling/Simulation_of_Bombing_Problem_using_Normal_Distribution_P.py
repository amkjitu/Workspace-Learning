import numpy as np
rx = np.random.normal(size = 20)
ry = np.random.normal(size = 20)
  
# printing numbers
for i in range(19):
    coX = 500*rx[i]
    coY = 300*ry[i]
    print("x = {}, y = {}".format(coX,coY))
    if(abs(coX)<=500 and abs(coY) <= 300):
        print("Hit")
    else:
        print("Miss")

