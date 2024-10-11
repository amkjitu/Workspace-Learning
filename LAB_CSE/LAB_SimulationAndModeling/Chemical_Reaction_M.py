import math as mat
import matplotlib.pyplot as plt

c1Y = []
c1X = []

c2Y = []
c2X = []

c3Y = []
c3X = []

c1 = []
c2 = []
c3 = []
k1 = 0.025
k2 = 0.01
delta = 0.1
c1.append(50.0) 
c2.append(25.5) 
c3.append(0.0)

c1Y.append(50)
c1X.append(0)

c2Y.append(25.5)
c2X.append(0)

c3Y.append(0)
c3X.append(0)

t = 0.0
time = 8.0
#time = 15
i = 0
print("{:^5}{:^12}{:^12}{:^12}".format("Time","C1","C2","C3"))
print("--------------------------------------")

while(t<=time):
    print("{:^5}{:^12}{:^12}{:^12}".format(round(t,2),round(c1[i],2),round(c2[i],2),round(c3[i],2)))
    data1 = c1[i]+((k2*c3[i]-k1*c1[i])*c2[i])*delta
    c1.append(data1)
    data2 = c2[i]+((k2*c3[i]-k1*c1[i])*c2[i])*delta
    c2.append(data2)
    data3 = c3[i]+2.0*((k1*c1[i]*c2[i])-k2*c3[i])*delta
    c3.append(data3)

    c1Y.append(data1)
    c1X.append(i)

    c2Y.append(data2)
    c2X.append(i)

    c3Y.append(data3)
    c3X.append(i)

    if(i==0):
        plt.plot(c1X,c1Y,color = 'green', label = 'C1')
        plt.plot(c2X,c2Y,color = 'blue', label = 'C2')
        plt.plot(c3X,c3Y,color = 'red', label = 'C3')
        plt.title("Chemical Reaction of C1 & C2 produces C3")
        plt.xlabel("X-axis: Iteration")
        plt.ylabel("Y-axis: Reaction")
    else:
        plt.plot(c1X,c1Y,color = 'green')
        plt.plot(c2X,c2Y,color = 'blue')
        plt.plot(c3X,c3Y,color = 'red')

    
    plt.legend()
    plt.pause(0.5)

    i = i+1
    t = t+delta
    if(t>=2.0): delta = 0.2
    if(t>=6.0): delta = 0.4

plt.show()


