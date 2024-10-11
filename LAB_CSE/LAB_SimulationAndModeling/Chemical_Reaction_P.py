import math as mat
import matplotlib.pyplot as plt

c1 = []
c2 = []
c3 = []
k1 = 0.025
k2 = 0.01
delta = 0.1
c1.append(50.0) 
c2.append(25.5) 
c3.append(0.0)
t = 0.0
time = 8.0
i = 0
print("{:^5}{:^12}{:^12}{:^12}".format("Time","C1","C2","C3"))

while(t<=time):
    print("{:^5}{:^12}{:^12}{:^12}".format(round(t,2),round(c1[i],2),round(c2[i],2),round(c3[i],2)))
    data1 = c1[i]+((k2*c3[i]-k1*c1[i])*c2[i])*delta
    c1.append(data1)
    data2 = c2[i]+((k2*c3[i]-k1*c1[i])*c2[i])*delta
    c2.append(data2)
    data3 = c3[i]+((k1*c1[i]*k1*c2[i])-k2*c3[i])*delta
    c3.append(data3)

    i = i+1
    t = t+delta
    if(t>=2.0): delta = 0.2
    if(t>=6.0): delta = 0.4


