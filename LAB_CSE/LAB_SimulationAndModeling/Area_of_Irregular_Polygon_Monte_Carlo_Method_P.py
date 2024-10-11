import random as rand
import matplotlib.pyplot as plt

def point_inside_outside(polygon,point):

    INT_MAX = 10000
    def onSegment(p:tuple, q:tuple, r:tuple) -> bool:
     
        if ((q[0] <= max(p[0], r[0])) &
            (q[0] >= min(p[0], r[0])) &
            (q[1] <= max(p[1], r[1])) &
            (q[1] >= min(p[1], r[1]))):
            return True
         
        return False
 
    def orientation(p:tuple, q:tuple, r:tuple) -> int:
        val = (((q[1] - p[1]) *(r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1])))
         
        if (val > 0):     # Clockwise orientation
            return 1
        elif (val < 0): # Counterclockwise orientation
            return 2
        else:                # Colinear orientation
            return 0
 
    def doIntersect(p1, q1, p2, q2):
     
        # Find the four orientations needed for general and special cases
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)
 
        # General case
        if (o1 != o2) and (o3 != o4):
            return True
     
        # Special Cases
        # p1, q1 and p2 are colinear and p2 lies on segment p1q1
        if (o1 == 0) and (onSegment(p1, p2, q1)):
            return True
 
        # p1, q1 and p2 are colinear and q2 lies on segment p1q1
        if (o2 == 0) and (onSegment(p1, q2, q1)):
            return True
 
        # p2, q2 and p1 are colinear and p1 lies on segment p2q2
        if (o3 == 0) and (onSegment(p2, p1, q2)):
            return True
 
        # p2, q2 and q1 are colinear and q1 lies on segment p2q2
        if (o4 == 0) and (onSegment(p2, q1, q2)):
            return True
 
        return False
 
    # Returns true if the point p lies inside the polygon[] with n vertices
    def is_inside_polygon(points:list, p:tuple) -> bool:
     
        n = len(points)
     
        # There must be at least 3 vertices in polygon
        if n < 3:
            return False
         
        # Create a point for line segment from p to infinite
        extreme = (INT_MAX, p[1])
        count = i = 0
     
        while True:
            next = (i + 1) % n
         
            # Check if the line segment from 'p' to  'extreme' intersects with the line segment from 'polygon[i]' to 'polygon[next]'
            if (doIntersect(points[i], points[next], p, extreme)):
                             
                # If the point 'p' is colinear with line 
                # segment 'i-next', then check if it lies 
                # on segment. If it lies, return true, otherwise false
                if orientation(points[i], p, points[next]) == 0:
                    return onSegment(points[i], p, points[next])
                    
                count += 1
             
            i = next
         
            if (i == 0):
                break
         
        # Return true if count is odd, false otherwise
        return (count % 2 == 1)
    return is_inside_polygon(points = polygon, p = point)


randomXY = []
X=[]
Y=[]
for number in range(1000):
    #XY = rand.randint(2,9),rand.randint(2,9)
    XY = rand.uniform(2,9),rand.uniform(2,9)
    randomXY.append(XY)

for points in randomXY:
    X.append(points[0])
    Y.append(points[1])

plt.scatter(X,Y,c='red')

def area_polygon(point):
   x = []
   y = []
   for p in point:
       x.append(p[0])
       y.append(p[1])

       ar = 0
   for index in range(len(point)-1):
       ar += (x[index]*y[index+1])-(y[index]*x[index+1])
   return abs(ar/2)

square_xy = [(2,2),(9,2),(9,9),(2,9),(2,2)]
#polygon_xy = [(3,3),(3,5),(6,8),(8,8),(6,6),(7,3),(3,3)]

polygon_xy = []
inixy = [(3,3)]
halfxy1 = []
halfxy2 = []
rxry = []

for i in range(10):
    xy = rand.uniform(3,9),rand.uniform(3,9)
    rxry.append(xy)

for i in rxry[:5]:
    xy = rand.uniform(3,9),rand.uniform(3,9)
    halfxy1.append(xy)
halfxy1.sort(key=lambda x: x[1])

for i in rxry[5:]:
    xy = rand.uniform(3,9),rand.uniform(3,9)
    halfxy2.append(xy)
halfxy2.sort(key=lambda x: x[1], reverse=True)

polygon_xy = inixy + halfxy1 + halfxy2 + inixy

print(polygon_xy)


area_of_square = area_polygon(square_xy)
area_of_polygon = area_polygon(polygon_xy)

def area_of_irregular_shape():
   count_inside_point = 0
   count_outside_point = 0
   for points in randomXY:
       if(point_inside_outside(polygon_xy,points)):
           count_inside_point += 1
       else:
           count_outside_point += 1
   return (count_inside_point/len(randomXY))*area_of_square #f = m/n*a

area_of_irregular_shape_approx = area_of_irregular_shape()


SX = [2,9,9,2,2]
SY = [2,2,9,9,2]
Y = []
XY = [(3,3),(3,5),(6,8),(8,8),(6,6),(7,3),(3,3)]
X= []
for point in polygon_xy:
        X.append(point[0])
        Y.append(point[1])

plt.plot(SX,SY, c='green')
plt.plot(X,Y,)
plt.title('Approx Area= %d' %(area_of_irregular_shape_approx))

plt.scatter(X,Y)
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.show()