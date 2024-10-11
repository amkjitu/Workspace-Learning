#It is serial chase problem. Four animals A,B,C,D are there in the field. A chases B, B chases C, C chases D.
#as soon as the target is with in say 0.005 km, it is killed and the chase ends
#Speed of A,B,C,D  are given say 35,25,15 and 10 km/hr. The initial position are fixed. 
#It is assumed that A will always run in the direction of B and B straight towards C and 
#C straight towards D. D runs straight away form C in first case and towards A in the second case.
#xa and xb are the coordinates of A
#thab is the angle with direction ab
#dab is the distance between A and B
#va is the velocity of A

import math as mat
import matplotlib.pyplot as plt

XA = [];YA = [];XB = [];YB = [];XC = [];YC = [];XD = [];YD = []

xa = 10.0; ya = 10.0; xb = 30.0; yb = 10.0; xc = 30.0; yc = 30.0; xd = 10.0; yd = 30.0
thab = 0.0; thbc = 0.0; thcd = 0.0; thd = 0.0
va = 35.0; vb = 25.0; vc = 25; vd = 10
t = 0.0; delt = 0.001; i=0;
dab = ((xa-xb)**2 + (ya-yb)**2)**0.5
dbc = ((xb-xc)**2 + (yb-yc)**2)**0.5
dcd = ((xc-xd)**2 + (yc-yd)**2)**0.5

print("_____________________________________________________________")
print("{:^14}{:^14}{:^14}{:^14}{:^5}".format("A","B","C","D","T"))
print("{:^14}{:^14}{:^14}{:^14}{:^5}".format("________","________","________","________",""))
print("{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^2}".format("x","y","x","y","x","y","x","y",""))
print("_____________________________________________________________")

while(t<=1.70):
    xa = xa + va*delt*(xb-xa)/dab
    ya = ya + va*delt*(yb-ya)/dab
    xb = xb - vb*delt*(xb-xc)/dbc
    yb = ya + vb*delt*(yc-yb)/dbc
    xc = xc - vc*delt*(xc-xd)/dcd
    yc = yc - vc*delt*(yc-yd)/dcd
    #xd = xd
    xd = xd - vd*delt
    yd = yd - vd*delt
    dab = ((xa-xb)**2 + (ya-yb)**2)**0.5
    dbc = ((xb-xc)**2 + (yb-yc)**2)**0.5
    dcd = ((xc-xd)**2 + (yc-yd)**2)**0.5
    print("{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}".format(round(xa,2),round(ya,2),round(xb,2),round(yb,2),round(xc,2),round(yc,2),round(xd,2),round(yd,2),round(t,2)))
    t = t + delt

    if(dab <=0.005):
        t = 4.0; print("B killed, chase ends")
        plt.annotate('A killed B', xy=(xa,ya), xytext=(xa+2, ya-5),arrowprops=dict(facecolor='blue', shrink=0.05))
    if(dbc<=0.005):
        t = 4.0; print("C killed, chase ends")
        plt.annotate('B killed C', xy=(xb,yb), xytext=(xb+2, yb-5),arrowprops=dict(facecolor='blue', shrink=0.05))
    if(dcd<=0.005):
       t = 4.0; print("D killed, chase ends")
       plt.annotate('C killed D', xy=(xc,yc), xytext=(xc+2, yc-5),arrowprops=dict(facecolor='blue', shrink=0.05))

    XA.append(xa); YA.append(ya); XB.append(xb); YB.append(yb); XC.append(xc); YC.append(yc); XD.append(xd); YD.append(yd);
    if(t<=0.001):
        plt.plot(XA,YA,color = 'green', label = 'A')
        plt.plot(XB,YB,color = 'blue', label = 'B')
        plt.plot(XC,YC,color = 'red', label = 'C')
        plt.plot(XD,YD,color = 'black', label = 'D')
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Simulation of Serial Chase")
        plt.legend()
    else:
        plt.plot(XA,YA,color = 'green')
        plt.plot(XB,YB,color = 'blue')
        plt.plot(XC,YC,color = 'red')
        plt.plot(XD,YD,color = 'black')

    
    i=i+1
    if(i%100==0):
        plt.pause(0.0000001)

print("_____________________________________________________________")

plt.show()