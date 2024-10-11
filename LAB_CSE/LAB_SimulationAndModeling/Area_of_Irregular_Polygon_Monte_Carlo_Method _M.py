import random as rand
import matplotlib.pyplot as plt

###In this code the many operations occured
#1. LineSagment Intersection
#2. A point inside or outside a polygon
#3. joto guli random point ache check korbo je seta ki irregular share er vitore kina
#then area of irregular shape =  (no. of point inside the irregular shape/no. of point inside the know shape) x area of know shape

##LineSagment Intersect1
def lineSegment_intersect(p0,p1,p2,p3):
    A1 = p1[1] - p0[1]
    B1 = p0[0] - p1[0]
    C1 = A1*p0[0] + B1*p0[1]

    A2 = p3[1] - p2[1]
    B2 = p2[0] - p3[0]
    C2 = A2*p2[0] + B2*p2[1]

    denominator = A1*B2 - A2*B1

    #Colinear and parallel
    if(denominator == 0):
        #return None
        return False

    intersectX = (B2*C1 - B1*C2)/denominator
    intersectY = (A1*C2 - A2*C1)/denominator

    x_y = (intersectX,intersectY)

 
    #Checking isIntersectin extended portion of the segment
    if p1[0] != p0[0]:
        rx0 = (intersectX - p0[0])/(p1[0] - p0[0]) #(4,0), (4,4)
    else: 
        #rx0 = (intersectX - p0[0])
        rx0 = 2
    if p1[1] != p0[1]:
        ry0 = (intersectY - p0[1])/(p1[1] - p0[1])
    else:
        #ry0 = (intersectY - p0[1])
        ry0 = 2
    if p3[0] != p2[0]:
        rx1 = (intersectX - p2[0])/(p3[0] - p2[0])
    else:
        #rx1 = (intersectX - p2[0])
        rx1 = 2
    if p3[1] != p2[1]:
        ry1 = (intersectY - p2[1])/(p3[1] - p2[1])
    else:
        #ry1 = (intersectY - p2[1])
        ry1 = 2
    
    if( ((rx0 >= 0 and rx0 <= 1) or (ry0 >= 0 and ry0 <= 1)) and ((rx1 >= 0 and rx1 <= 1) or (ry1 >= 0 and ry1 <= 1)) ):
        x = intersectX
        y = intersectY
        #return x,y
        return True
    else: 
       return False

##Returns true if the point p lies inside the polygon[] with n vertices
def is_inside_polygon(points:list, p:tuple) -> bool:
      INT_MAX = 1000
      n = len(points)
     
      # There must be at least 3 vertices in polygon
      if n < 3:
         return False
         
      # Create a point for line segment from p to infinite
      extreme = (INT_MAX, p[1])
      count = i = 0
      #print("Entered")
      while True:
         next = (i + 1) % n
         #print("count = {}, i = {}, next = {}".format(count,i,next))
         #[(0,0) ,(4,0), (4,4), (0,4)]
         # Check if the line segment from 'p' to 'extreme' intersects with the line segment from 'polygon[i]' to 'polygon[next]'
         if lineSegment_intersect(points[i], points[next], p, extreme):     
            count += 1
            #print("line intersect korlo : count = {} point({} and point{} ched kore point{} and point{} ke)".format(count,points[i],points[next],p,extreme))
         i = next
         if (i == 0):
            break
      #print("Return er age count er value = {}".format(count))
      # Return true if count is odd, false otherwise
      return (count % 2 == 1)

def random_Point_inside_known_figure(noOfPoints,lLimit,uLimit):
    xy = []
    x = []
    y = []
    for point in range(noOfPoints):
        x_y = rand.uniform(lLimit,uLimit),rand.uniform(lLimit,uLimit)
        xy.append(x_y)
    for point in xy:
        x.append(point[0])
        y.append(point[1])
    return xy,x,y

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

def points_inside_the_irregular_figure(irregular_figure_xy,rand_xy):
    pointsInside = 0;
    for point in rand_xy:
        if(is_inside_polygon(irregular_figure_xy, point)):
            plt.scatter(point[0],point[1],c='red')
            #print(point)
            pointsInside += 1
        else:
            plt.scatter(point[0],point[1],c='blue')
    return pointsInside


##Ashol Function
rand_xy,x,y = random_Point_inside_known_figure(noOfPoints = 800, lLimit = 0, uLimit = 10)

regular_figure_xy =  [(0,0),(10,0),(10,10),(0,10),(0,0)]
#regular_figure_xy =  [(2,2),(9,0),(9,9),(0,9),(2,2)]
#irregular_figure_xy =  [(3,3),(3,5),(6,8),(8,8),(6,6),(7,3),(3,3)]
irregular_figure_xy =  [(1,0),(2,2),(10,3),(9,9),(5,6),(2,10),(0,4),(1,4),(1,2),(1,1),(1,0)]

area_regular = area_polygon(regular_figure_xy)
area_irregular = area_polygon(irregular_figure_xy)

print("Area of the Square = {}".format(area_regular))
print("Area of the Irregular Figure = {}".format(area_irregular))

points_inside_irregular = points_inside_the_irregular_figure(irregular_figure_xy,rand_xy)
points_inside_regular = len(rand_xy)
print("Irregular er vitore {} points".format(points_inside_irregular))
print("Regular er vitore {} points".format(points_inside_regular))

area_irregular_approx = (points_inside_irregular/points_inside_regular)*area_regular
print("Approximate Area of the Irregular Figure = {}".format(area_irregular_approx))

Rx = []
Ry = []
for point in regular_figure_xy:
    Rx.append(point[0])
    Ry.append(point[1])

plt.plot(Rx, Ry, c='green',linewidth=4, label = 'Area of Regular Shape = %d' %area_regular)

Irx = []
Iry = []
for point in irregular_figure_xy:
    Irx.append(point[0])
    Iry.append(point[1])

plt.plot(Irx,Iry, c='yellow',linewidth=3, label = 'Area of Irregular Shape = %d' %area_irregular)

plt.title("Total {} drops, Area of Irregular Shape(Approx.) = {:.2f} \nAcquracy = {:.2f} %".format(len(rand_xy), area_irregular_approx, (area_irregular_approx/area_irregular)*100))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()   

##Ends - Jitu