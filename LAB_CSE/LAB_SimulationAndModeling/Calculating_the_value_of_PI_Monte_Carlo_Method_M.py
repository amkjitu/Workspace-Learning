import random as rand
import matplotlib.pyplot as plt

#quation of the circle,  x2 + y2 = r2
#area of the circle = PI x r2
#for a unit circle, r = 1 so area = PI
#area of a quadrant = (PI x r2)/4 = PI/4
#points inside a quadrant x2 + y2 <= 1 and x,y >= 0

plt.figure(figsize=(6,6))
plt.xlim(0,1.5)
plt.ylim(0,1.5)

PI = 3.14159
#Square
squareXY = [(0,0),(1,0),(1,1),(0,1),(0,0)]
sx = []
sy = []
for i in squareXY:
    sx.append(i[0])
    sy.append(i[1])
    if squareXY.index(i) == 3:
        #print("Ract")
        plt.plot(sx, sy, label = "Unit Square", linewidth=3, color = 'yellow')
    else:
        plt.plot(sx, sy, linewidth=3, color = 'yellow')
    plt.pause(0.5)


cx = []
cy = []

#x2 + y2 = 1
# x2 = 1-y2
# x = root(1-y2)
# y2 = 1 - x2
# y = root(1-x2)

##Circle Draw
for i in range(101):
    x = (1 - (i/100)**2)**0.5
    y = (1 - x**2)**0.5
    print(x,y)

    cx.append(x)
    cy.append(y)
    if(i==1):
        plt.plot(cx, cy, label = "1/4 of a unit circle", linewidth=3, color = 'red')
    else:
        plt.plot(cx, cy, linewidth=3, color = 'red')

    plt.pause(0.0001)

# PI / 4 = (inside/all) x square
# PI = (inside/all) x square x 4

drops = 0
pointsInside = 0
pointsOutside = 0
while(1):
    drops += 1
    randx = rand.uniform(0,1)
    randy = rand.uniform(0,1)
    
    if(randx**2 + randy**2 <= 1):

        pointsInside += 1
        if(pointsInside == 1):
            plt.scatter(randx,randy,color = 'green', label = 'Inside the circle')
        else: 
            plt.scatter(randx,randy,color = 'green')

        if(drops%70 == 0): plt.pause(0.000001)

    else:

        pointsOutside += 1
        if(pointsOutside == 1):
            plt.scatter(randx,randy,color = 'blue', label = 'Outside the circle')
        else:
             plt.scatter(randx,randy,color = 'blue')

        #plt.pause(0.000001)
    
    Estimated_PI = (pointsInside/drops)*4
    Error = (PI-Estimated_PI)

    plt.title("Total {} drops, Value of PI = {:.5f} [approx.]  \nTrue Result = {}, Acquracy = {:.2f} %".format(drops, Estimated_PI, PI, (Estimated_PI/PI)*100))
    plt.legend()

    if(drops >= 100 and Error <= 0.0001):
        break

print("inside {}, outside {}".format(pointsInside,pointsOutside)) 
Estimated_PI = (pointsInside/drops)*4
print("Estimate Value of PI = {}".format(Estimated_PI))



plt.show()
