import math as mat
import matplotlib.pyplot as plt

Time = []
for i in range(0,16):
    Time.append(i)

xb = [100,100,120,129,140,149,158,168,179,188,198,209,219,226,234,24]
yb = [0,3,6,10,15,20,26,32,37,34,30,27,23,19,16,14]

Speed = int(input("Enter the speed: "))
MinimumDistance = int(input("Enter minimum distance to kill: "))
xf = [0]
yf = [50]

#xf[0] = 0
#yf[0] = 50
dist = []

print("\n_________________________________________________________________________________________________")
print("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Time", "xb(t)", "yb(t)", "xf(t)", "yf(t)", "dist(t)","sinTheta","cosTheta","xf(t+1)","yf(t+1)"))
print("__________________________________________________________________________________________________")

for i in Time[1:] :
    #print(i-1)
    #print(xb[i-1])

    dif_of_yb_yf = (yb[i-1]-yf[i-1])
    dif_of_yb_yf = round(dif_of_yb_yf,2)

    dif_of_xb_xf = (xb[i-1]-xf[i-1])
    dif_of_xb_xf = round(dif_of_xb_xf,2)

    dis = mat.sqrt(dif_of_yb_yf**2 + dif_of_xb_xf**2)
    dis = round(dis,2)
    dist.append(dis)

    sinTheta = (dif_of_yb_yf/dist[i-1])
    sinTheta = round(sinTheta,2)

    cosTheta = (dif_of_xb_xf/dist[i-1])
    cosTheta = round(cosTheta,2)

    x = xf[i-1]+(Speed*cosTheta)
    x = round(x,2) 
    xf.append(x)

    y = yf[i-1]+(Speed*sinTheta)
    y = round(y,2)
    yf.append(y)

    print("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format(i-1,xb[i-1], yb[i-1], xf[i-1], yf[i-1], dist[i-1],sinTheta,cosTheta,xf[i],yf[i]))
    if(dist[i-1] <= MinimumDistance): 
        print("Killed")
        break

    #print(dist[i-1], sinTheta, cosTheta, xf[i], yf[i])
    if(i==len(Time)-1):
       
        dif_of_yb_yf = (yb[i]-yf[i])
        dif_of_yb_yf = round(dif_of_yb_yf,2)

        dif_of_xb_xf = (xb[i]-xf[i])
        dif_of_xb_xf = round(dif_of_xb_xf,2)

        dis = mat.sqrt(dif_of_yb_yf**2 + dif_of_xb_xf**2)
        dis = round(dis,2)
        dist.append(dis)

        sinTheta = (dif_of_yb_yf/dist[i])
        sinTheta = round(sinTheta,2)

        cosTheta = (dif_of_xb_xf/dist[i])
        cosTheta = round(cosTheta,2)

        x = xf[i]+(Speed*cosTheta)
        x = round(x,2) 
        xf.append(x)

        y = yf[i]+(Speed*sinTheta)
        y = round(y,2)
        yf.append(y)

        print("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format(i,xb[i], yb[i], xf[i], yf[i], dist[i],sinTheta,cosTheta,xf[i],yf[i]))
