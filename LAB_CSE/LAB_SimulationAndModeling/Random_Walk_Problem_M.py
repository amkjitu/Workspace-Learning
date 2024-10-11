import random as rand
import matplotlib.pyplot as plt

print("\n_________________________________________________________________________________________________")
print("{:^10}{:^20}{:^10}{:^25}".format("Step", "Random Number", "Direction", "Position"))
print("{:^10}{:^20}{:^10}{:^25}".format("", "", "","--------------------"))
print("{:^10}{:^20}{:^10}{:^10}{:^20}".format("", "", "", "X","Y"))
print("_________________________________________________________________________________________________")

Y = [0]
X = [0]
randomX = 0
randomY = 0
plt.plot(X,Y)
for i in range(1,41):
    random_p = rand.randint(0,9)
    print("{:^10}".format(i),end = '')
    print("{:^20}".format(random_p),end = '')
    #print(randomX,randomY)
    #Forward 
    if(random_p >= 0 and random_p <= 4):
       randomY += 1
       Y.append(randomY)
       X.append(randomX)
       print("{:^10}".format("Forward"),end = '')
       #print("{:^10}".format(randomY),end = '')
       plt.plot(X,Y,color = 'green')
       plt.pause(0.5)
       #print(randomX,randomY)
    #Left
    elif(random_p >= 5 and random_p <= 7):
        randomX -= 1
        print("{:^10}".format("Left"),end = '')
        #print("{:^10}".format(randomX),end = '')
        X.append(randomX)
        Y.append(randomY)
        plt.plot(X,Y,color = 'red')
        plt.pause(0.5)
        #print(randomX,randomY)
    #Right
    else:
        randomX += 1
        print("{:^10}".format("Right"),end = '')
        #print("{:^10}".format(randomX),end = '')
        X.append(randomX)
        Y.append(randomY)
        plt.plot(X,Y,color = 'red')
        plt.pause(0.5)
        #print(randomX,randomY)
    print("{:^10}".format(randomX),end = '')
    print("{:^19}".format(randomY),end = '')
    print()
    if i == 40:
        plt.annotate('Probable Location of  the drunkard', xy=(randomX,randomY), xytext=(randomX+2, randomY-5),arrowprops=dict(facecolor='blue', shrink=0.05))
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()