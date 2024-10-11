import random as rand
import matplotlib.pyplot as plt
import numpy as np

I = ((5**4)/4)-((2**4)/4)

drops = 100

squareXY = [(2,0),(5,0),(5,125),(2,125),(2,0)]
sx = []
sy = []
for i in squareXY:
    sx.append(i[0])
    sy.append(i[1])

def area_polygon(xy):
   x = []
   y = []
   for p in xy:
      x.append(p[0])
      y.append(p[1])

   ar = 0
   for index in range(len(xy)-1):
      ar += (x[index]*y[index+1])-(y[index]*x[index+1])
   return abs(ar/2)

point = []
x = []
y = []
pointsInside = 0
pointsOutside = 0

for i in range(drops): # while(True):
    randx = rand.uniform(2,5)
    randy  = rand.uniform(2,125)
    point.append((randx ,randy))

x = []
y = []
for i in point:
    x.append(i[0])
    y.append(i[1])

plt.scatter(x,y,color = 'red')

for i in point:
    if(i[1] <= i[0]**3):
        pointsInside += 1
    else:
        pointsOutside += 1

print("I = {}".format(I))
ApproxI = (pointsInside/drops)*area_polygon(squareXY)
print("Approx I = {}".format(ApproxI))


XY = []
for i in range(2,5):
        for j in range(11):
            x = i+(j/10)
            XY.append((x,x**3))

#XY = []
#for i in range(2,5+1):
#    XY.append((i,i**3))


X = []
Y = []
for i in XY:
    X.append(i[0])
    Y.append(i[1])

plt.plot(X, Y, color='black')
plt.title("Integration of y = x^3(Approx.) = {:.3f}".format(ApproxI))
plt.plot(sx,sy)
plt.xlabel("x")
plt.ylabel("f(x)=x^3")
plt.show()