import random as rand
import matplotlib.pyplot as plt

Y = [0]
X = [0]
randomX = 0
randomY = 0
plt.plot(X,Y)
for i in range(41):
    random_p = rand.randint(0,9)
    #print(randomX,randomY)
    #Forward 
    if(random_p >= 0 and random_p <= 4):
       randomY += 1
       Y.append(randomY)
       X.append(randomX)
       plt.plot(X,Y)
       print(randomX,randomY)
    #Left
    elif(random_p >= 5 and random_p <= 7):
        randomX -= 1
        X.append(randomX)
        Y.append(randomY)
        plt.plot(X,Y)
        print(randomX,randomY)
    #Right
    else:
        randomX += 1
        X.append( randomX)
        Y.append(randomY)
        plt.plot(X,Y)
        print(randomX,randomY)

plt.show()
