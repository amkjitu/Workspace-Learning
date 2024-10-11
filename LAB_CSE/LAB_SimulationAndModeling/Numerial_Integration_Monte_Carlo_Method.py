#Sir jevabe bolsen
import random as rand
import matplotlib.pyplot as plt
import numpy as np

print("Formula for integration x^n = x^(n+1)/(n+1)")
print("------------------------------------------------")
print("I = x^3 in range [2-5]")
print("[x^4/4] in range 2 to 5")
I = ((5**4)/4)-((2**4)/4)
print("Result = {}".format(I))
print("------------------------------------------------")

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
drops = 0
#for i in range(drops):
while(True):
    drops += 1
    randx = rand.uniform(2,5)
    randy  = rand.uniform(2,125)

    if(randy <=randx**3):
        pointsInside += 1
        if pointsInside == 1:
            plt.scatter(randx,randy,color = 'red', label = "Inside")
        else:
            plt.scatter(randx,randy,color = 'red')  
    else:
        pointsOutside += 1
        if pointsOutside == 1:
            plt.scatter(randx,randy,color = 'green', label = "Outside")
        else:
            plt.scatter(randx,randy,color = 'green')

    print("points inside {}".format(pointsInside))
    print("points total {}".format(drops))
    print("I = {}".format(I))
    ApproxI = (pointsInside/drops)*area_polygon(squareXY)
    print("Approx I = {}".format(ApproxI))
    if(abs(I-ApproxI) <= 0.005):
        print("Acquracy 100%")
        break


XY = []
for i in range(2,5):
        for j in range(11):
            x = i+(j/10)
            XY.append((x,x**3))
#print(XY)

X = []
Y = []
for i in XY:
    X.append(i[0])
    Y.append(i[1])

#print(X)
#print(Y)

plt.plot(X, Y, color='black', alpha=0.75, linestyle='solid', linewidth=4.5, label='f(x) = x^3 curve')
#plt.scatter(X,Y)

shx = [0,0]
shy = [0,0]
for i in range(len(X)-1):
    shx[0] = X[i]
    shx[1] = X[i+1]
    shy[0] = Y[i]
    shy[1] = 0
    plt.plot(shx, shy, color='black', alpha=0.40, linestyle='dashed', linewidth=4.5)

plt.title("Total {} drops, Integration of y = x^3(Approx.) = {:.5f} \nTrue Result = {}, Acquracy = {:.2f} %".format(drops, ApproxI, I, (ApproxI/I)*100))
plt.plot(sx,sy, label = "Ractangle", linewidth=3)
plt.xlabel("x")
plt.ylabel("f(x)=x^3")
plt.legend()
plt.show()
















'''
#Boi er instruction onujaye
import random as rand
import matplotlib.pyplot as plt
import numpy as np

print("Formula for integration x^n = x^(n+1)/(n+1)")
print("------------------------------------------------")
print("I = x^3 in range [2-5]")
print("[x^4/4] in range 2 to 5")
I = ((5**4)/4)-((2**4)/4)
print("Result = {}".format(I))
print("------------------------------------------------")

drops = int(input("Enter Drops: "))

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

print("Area {}".format(area_polygon(squareXY)))

#ApproxI = (pointsInside/drops)*area_polygon(squareXY)
#print("Approximate Intergration = {}".format(ApproxI))

point = []
x = []
y = []
pointsInside = 0
pointsOutside = 0

for i in range(drops):
    randx = rand.uniform(2,5)
    randy  = rand.uniform(2,125)
    point.append((randx ,randy))
    #print(point)

x = []
y = []
for i in point:
    x.append(i[0])
    y.append(i[1])

#pointsInside = 0
#pointsOutside = 0


for i in point:
    if(i[1] <= i[0]**3):
        pointsInside += 1
        if pointsInside == 1:
            plt.scatter(i[0],i[1],color = 'red', label = "Inside")
        else:
            plt.scatter(i[0],i[1],color = 'red')  
    else:
        pointsOutside += 1
        if pointsOutside == 1:
            plt.scatter(i[0],i[1],color = 'green', label = "Outside")
        else:
            plt.scatter(i[0],i[1],color = 'green')

print("points inside {}".format(pointsInside))
print("points total {}".format(drops))
print("I = {}".format(I))
ApproxI = (pointsInside/drops)*area_polygon(squareXY)
print("Approx I = {}".format(ApproxI))


XY = []
for i in range(2,5):
        for j in range(11):
            x = i+(j/10)
            XY.append((x,x**3))
print(XY)

X = []
Y = []
for i in XY:
    X.append(i[0])
    Y.append(i[1])

print(X)
print(Y)

#plt.plot(X, Y, label= "y = x^3 curve")
#plt.plot(X, Y, color='green', marker='o', linestyle='solid', linewidth=5, markersize=12)
plt.plot(X, Y, color='black', alpha=0.75, linestyle='solid', linewidth=4.5, label='f(x) = x^3 curve')
#plt.scatter(X,Y)

shx = [0,0]
shy = [0,0]
for i in range(len(X)-1):
    shx[0] = X[i]
    shx[1] = X[i+1]
    shy[0] = Y[i]
    shy[1] = 0
    plt.plot(shx, shy, color='black', alpha=0.40, linestyle = 'dashed', linewidth=4.5)


plt.title("Total {} drops, Integration of y = x^3(Approx.) = {:.3f} \nAcquracy = {:.2f} %".format(drops, ApproxI, (ApproxI/I)*100))
plt.plot(sx,sy, label = "Ractangle")
plt.xlabel("x")
plt.ylabel("f(x)=x^3")
plt.legend()
plt.show()
'''

