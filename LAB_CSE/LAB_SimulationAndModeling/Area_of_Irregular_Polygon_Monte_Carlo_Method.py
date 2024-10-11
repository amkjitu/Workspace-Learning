import random as rand
import turtle as tt
import matplotlib.pyplot as plt


'''
#zip method
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y) #this is a list of tuple
'''

'''
#Generates random numbers from 2 upto 9
#No Floating numbers and random numbers can be duplicateed
Num1 = rand.randint(2,9) #randint(from,upto)
#Generates random numbers from 2 upto 9
#With Floating numbers and no duplication
Num2 = rand.uniform(2,9) #randint(from,upto)
'''

'''
#Return the area of the polygon
def polygon_area(points):  
    """
    Return the area of the polygon whose vertices are given by the sequence points.
    """
    area = 0
    q = points[-1]
    for p in points:  
        area += p[0] * q[1] - p[1] * q[0]
        q = p
    return area / 2

def find_area_perim(array):
    a = 0
    p = 0
    ox,oy = array[0]
    for x,y in array[1:]:
        a += (x*oy-y*ox)
        p += abs((x-ox)+(y-oy)*1j)
        ox,oy = x,y
    return a/2,p
'''

###Method1: In this code many operationshave occured
#1. Orientation
#2. Line Intersection
#3. A point inside or outside a polygon
#4. joto guli random point ache check korbo je seta ki irregular shape er vitore kina
#then area of irregular shape =  (no. of point inside the irregular shape/no. of point inside the know shape) x area of know shape


'''
def point_inside_outside(polygon,point):

    INT_MAX = 10000
    def onSegment(p:tuple, q:tuple, r:tuple) -> bool:
     
        if ((q[0] <= max(p[0], r[0])) &
            (q[0] >= min(p[0], r[0])) &
            (q[1] <= max(p[1], r[1])) &
            (q[1] >= min(p[1], r[1]))):
            return True
         
        return False
 
    # To find orientation of ordered triplet (p, q, r).
    # The function returns following values
    # 0 --> p, q and r are colinear
    # 1 --> Clockwise
    # 2 --> Counterclockwise
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



#print(rand.randint(1,100))
randomXY = []
X=[]
Y=[]
for number in range(10000):
    #XY = rand.randint(2,9),rand.randint(2,9)
    XY = rand.uniform(2,9),rand.uniform(2,9)
    randomXY.append(XY)
    #print(XY)
for points in randomXY:
    X.append(points[0])
    Y.append(points[1])

print(randomXY)
#plt.plot(X,Y)
plt.scatter(X,Y,c='red')
#plt.show()



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
polygon_xy = [(3,3),(3,5),(6,8),(8,8),(6,6),(7,3),(3,3)]

area_of_square = area_polygon(square_xy)
area_of_polygon = area_polygon(polygon_xy)

print("Area of square: {}".format(area_of_square))
print("Area of polygon: {}".format(area_of_polygon))

def area_of_irregular_shape():
   count_inside_point = 0
   count_outside_point = 0
   for points in randomXY:
       if(point_inside_outside(polygon_xy,points)):
           count_inside_point += 1
       else:
           count_outside_point += 1
   print("points inside the irregular shape = %d" %count_inside_point)
   print("points outside the irregular shape = %d" %count_outside_point)
   return (count_inside_point/len(randomXY))*area_of_square

area_of_irregular_shape_approx = area_of_irregular_shape()


SX = [2,9,9,2,2]
SY = [2,2,9,9,2]
Y = []
XY = [(3,3),(3,5),(6,8),(8,8),(6,6),(7,3),(3,3)]
X= []
for point in XY:
        X.append(point[0])
        Y.append(point[1])
#print(X)
#print(Y)

plt.plot(SX,SY, c='green', label = 'Area of Known Square = %d' %area_of_square)
plt.plot(X,Y, label = 'Area of Irregular Shape = %0.3f' %area_of_irregular_shape_approx)
plt.title('Total %d drops  Acquracy = %0.3f percent' %(len(randomXY), (area_of_irregular_shape_approx/area_of_polygon)*100))

plt.scatter(X,Y)
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.legend()
plt.show()
#Method1 Ends
'''



###Method2: In this code the many operations occured
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

    #print('Denominator = %f' %(denominator))
    #print('A1 = %f, B1 = %f, C1 = %f' %(A1, B1, C1))
    #print('A2 = %f, B2 = %f, C2 = %f' %(A2, B2, C2))

    #print('intersectX = %f intersectY = %f' %(intersectX,intersectY))
    #print('p0[0] = %f p0[1] = %f p1[0] = %f p1[1] = %f' %(p0[0],p0[1],p1[0],p1[1]))
    #print('p2[0] = %f p2[1] = %f p3[0] = %f p3[1] = %f' %(p2[0],p2[1],p3[0],p3[1]))

    #return True
    #return  intersectX, intersectY

 
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
irregular_figure_xy =  [(3,3),(3,5),(6,8),(8,8),(6,6),(7,3),(3,3)]

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

#Method2 Ends




'''
###Method2[Raw Copy from article]
##Point Class
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

##Line Intersect
def line_intersect(p0,p1,p2,p3):
    A1 = p1.y - p0.y
    B1 = p0.x - p1.x
    C1 = A1*p0.x + B1*p0.y

    A2 = p3.y - p2.y
    B2 = p2.x - p3.x
    C2 = A2*p2.x + B2*p3.y

    denominator = A1*B2 - A2*B1

   #Colinear and parallel
    if(denominator == 0):
      return None

    x = (B2*C1 - B1*C2)/denominator
    y = (A1*C2 - A2*C1)/denominator

    return x,y

##LineSagment Intersect
def lineSegment_intersect(p0,p1,p2,p3):
    A1 = p1.y - p0.y
    B1 = p0.x - p1.x
    C1 = A1*p0.x + B1*p0.y

    A2 = p3.y - p2.y
    B2 = p2.x - p3.x
    C2 = A2*p2.x + B2*p3.y

    denominator = A1*B2 - A2*B1

    #Colinear and parallel
    if(denominator== 0):
        #return None
        return False

    intersectX = (B2*C1 - B1*C2)/denominator
    intersectY = (A1*C2 - A2*C1)/denominator

    #Checking isIntersectin extended portion of the segment
    rx0 = (intersectX - p0.x)/(p1.x - p0.x)
    ry0 = (intersectY - p0.y)/(p1.y - p0.y)
    rx1 = (intersectX - p2.x)/(p3.x - p2.x)
    ry1 = (intersectY - p2.y)/(p3.y - p2.y)
    
    if( ((rx0 >= 0 and rx0 <= 1) or (ry0 >= 0 and ry0 <= 1)) and ((rx1 >= 0 and rx1 <= 1) or (ry1 >= 0 and ry1 <= 1)) ):
        x = intersectX
        y = intersectY
        #return x,y
        return True

p0 = Point(2,2) 
p1 = Point(7,7) 
p2 = Point(6,1) 
p3 = Point(3,5)

#print(line_intersect(p0,p1,p2,p3))
#print(lineSegment_intersect(p0,p1,p2,p3))



# Returns true if the point p lies inside the polygon[] with n vertices
def is_inside_polygon(points:list, p:tuple) -> bool:
      INT_MAX = 10000
      n = len(points)
     
      # There must be at least 3 vertices in polygon
      if n < 3:
         return False
         
      # Create a point for line segment from p to infinite
      extreme = (INT_MAX, p.y)
      count = i = 0
     
      while True:
         next = (i + 1) % n      
         # Check if the line segment from 'p' to 'extreme' intersects with the line segment from 'polygon[i]' to 'polygon[next]'
         if lineSegment_intersect(points[i], points[next], p, extreme):     
               count += 1
         
      # Return true if count is odd, false otherwise
      return (count % 2 == 1)

#poly_xy = [Point(2,2) ,Point(4,2), Point(4,4), Point(2,4), Point(2,2)]
#poin = Point(3,3)

#print(is_inside_polygon(poly_xy, poin))

'''