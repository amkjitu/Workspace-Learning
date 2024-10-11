import random as rand
import matplotlib.pyplot as plt

PI = 3.14159
#Square
squareXY = [(0,0),(1,0),(1,1),(0,1),(0,0)]
sx = []
sy = []
for i in squareXY:
    sx.append(i[0])
    sy.append(i[1])   
    plt.plot(sx, sy)

cx = []
cy = []

##Circle
for i in range(11):
    x = (1 - (i/10)**2)**0.5
    y = (1 - x**2)**0.5
    cx.append(x)
    cy.append(y)
    plt.plot(cx, cy)

drops = 0
pointsInside = 0
pointsOutside = 0
while(1):
    drops += 1
    randx = rand.uniform(0,1)
    randy = rand.uniform(0,1)
    
    if(randx**2 + randy**2 <= 1):
       pointsInside += 1

    Estimated_PI = (pointsInside/drops)*4
    Error = (PI-Estimated_PI)
    plt.scatter(randx,randy,color = 'blue')

    if(drops >= 100 and Error <= 0.001):
        break

 
plt.title("Value of PI = {:.5f} [approx.] ".format(Estimated_PI))
Estimated_PI = (pointsInside/drops)*4

print("Estimate Value of PI = {}".format(Estimated_PI))

plt.show()
