import math as mat
import matplotlib.pyplot as plt

#v1 is the input voltage
#v2 is the output voltage
#t represents time and h is the time increment
#el is the starting value of vl

v1Y = []
v1X = []

v2Y = []
v2X = []

a11 = -50; a21 = -100000.0; a22 = -2.15*10.0
b1 = - a11; b2 = - a21
t = 0.0; v1 = 0.0; v2 = 0.0
h = 0.05; e1 = 1.5; n = 25

print("a11 = {:<8} a21 = {:<10} a22 = {:<8} h = {:<8} el = {:<8}".format(round(a11,2),round(a21,2),round(a22,2),round(h,2),round(e1,2)))
print("{:^4}{:^15}{:^17}{:^17}".format("i","Time(u sec)","Voltage(v1)","Voltage(v2)"))
print("---------------------------------------------------")

for i in range(1,n+1):
    k11 = h*((a11*v1)+e1)
    k12 = h*((a21*v1)+(a22*v2)+b2)
    k21 = h*(a11*(v1+0.5*k11)+b1)
    k22 = h*(a21*(v1+0.5*k11)+a22*(v2+0.5*k12)+b2)
    k31 = h*(a11*(v1+0.5*k21)+b1)
    k32 = h*(a21*(v1+0.5*k21)+a22*(v2+0.5*k22)+b2)
    k41 = h*(a11*(v1+k31)+b1)
    k42 = h*(a21*(v1+k31)+a22*(v2+k32)+b2)

    v1 = v1 + (k11+2.0*k21+2.0*k31+k41)/6.0
    v2 = v2 + (k12+2.0*k22+2.0*k32+k42)/6.0
    t=t+h

    v1Y.append(v1)
    v1X.append(i)

    v2Y.append(v2)
    v2X.append(i)

    if(i==1):
        plt.plot(v1X,v1Y,color = 'green', label = 'V1')
        plt.plot(v2X,v2Y,color = 'blue', label = 'V2')
        plt.title("Simulation of an Amplifier Circuit")
    else:
        plt.plot(v1X,v1Y,color = 'green')
        plt.plot(v2X,v2Y,color = 'blue')

    plt.xlabel("X-axis: Iteration")
    plt.ylabel("Y-axis: Voltage")
    plt.legend()
    plt.pause(0.5)

    print("{:^4}{:^15}{:^17}{:^17} ".format(i,round(t,2),round(v1,2),round(v2,2)))

plt.show()


