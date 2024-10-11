import numpy as np
import matplotlib.pyplot as plt
  
##Ehane amra normally distributed random number in python dekhbo!!!
#numpy.random.normal(loc = 0.0, scale = 1.0, size = None): by default
#size(dimesion,elements in each dimension): if size is None (default), a single value is returned.
#ekhane: loc = mean, scale = standard deviation, size = Output shape

plt.style.use('ggplot')
plt.xlim(-1000,1000)
plt.ylim(-600,600)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

shot = int(input("Enter the no. of Shots: "))

print("---------------------------------------------------------------------")
print("{:^10}{:^15}{:^10}{:^15}{:^10}{:^10}".format("Bomb Strike", "RNN", "x", "RNN", "y", "Result"))
print("---------------------------------------------------------------------")

rx = np.random.normal(size = shot)
ry = np.random.normal(size = shot)

countMiss = 0  
countHit = 0  
arrOfcoX = []
arrOfcoY = []

def drawTargetArea():
    x = [-500,500,500,-500,-500]
    y = [-300,-300,300,300,-300]
    plt.plot(x,y,color='yellow',label="Target")

drawTargetArea()

for i in range(shot):
    rx[i]=round(rx[i],2)
    ry[i]=round(ry[i],2)
    coX = round(500*rx[i],2)
    coY = round(300*ry[i],2)
    arrOfcoX.append(coX)
    arrOfcoY.append(coY)
    plt.legend()
    if(abs(coX)<=500 and abs(coY) <= 300):
        print("{:^10}{:^15}{:^10}{:^15}{:^10}{:^10}".format(i+1,rx[i], coX, ry[i], coY, "Hit"))
        countHit+=1
        if countHit == 1: plt.scatter(coX,coY,color='red',label = "hit")
        plt.title(("Target\nNo of hits = {} | No of misses = {}".format(countHit,countMiss)))
        plt.scatter(coX,coY,color='red')
        
        plt.pause(0.5)
    else:
        print("{:^10}{:^15}{:^10}{:^15}{:^10}{:^10}".format(i+1,rx[i], coX, ry[i], coY, "Miss"))
        countMiss+=1
        if countMiss == 1: plt.scatter(coX,coY,color='black',label = "Miss")
        plt.title(("Target\nNo of hits = {} | No of misses = {}".format(countHit,countMiss)))
        plt.scatter(coX,coY,color='black')
        plt.pause(0.5)
print("---------------------------------------------------------------------")
print("No of hits = {} | No of misses = {}".format(countHit,countMiss))
print("Number of strikes on target = {} %".format((countHit/shot)*100))

plt.show()



