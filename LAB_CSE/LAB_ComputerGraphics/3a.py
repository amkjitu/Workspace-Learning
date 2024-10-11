# ###with center#########      
# def CircleMidPoint(r,c):
    
#     xcoordinate = []
#     ycoordinate = []

#     d = 1 - r

#     xc,yc=c

#     x=0
#     y=r
    
#     #90 to 45 
#     while(x<=y):
#         xcoordinate.append(x) 
#         ycoordinate.append(y)

#         if(d<0):
#             d_next = d + (2*x) + 3
#         else:
#             d_next = d + 2*(x-y) + 5
#             y=y-1

#         # Iteration, di, di+1, (xi+1,yi+1)
#         if x==0:
#             print("{:^3}|  {:^3}| {:^3}|  {:^2},{:^2}".format('Iteration','di','di+1','(xi+1','yi+1)'))
#         print("  {:^5}   {:^5}  {:^5}   {:^3}, {:^3}".format(x,d,d_next,x+xc,y+yc))
    
#         x=x+1
#         d=d_next

#     negxcoordinate = [ -x for x in xcoordinate]
#     negycoordinate = [ -y for y in ycoordinate]

#     # Add the origin coordinates to the x and y values before plotting them
#     plt.scatter([x+xc for x in xcoordinate],[y+yc for y in ycoordinate])
#     plt.scatter([x+xc for x in negxcoordinate],[y+yc for y in ycoordinate])
#     plt.scatter([x+xc for x in negxcoordinate],[y+yc for y in negycoordinate])
#     plt.scatter([x+xc for x in xcoordinate],[y+yc for y in negycoordinate])
    
#     plt.scatter([y+xc for y in ycoordinate],[x+yc for x in xcoordinate])
#     plt.scatter([y+xc for y in negycoordinate],[x+yc for x in xcoordinate])
#     plt.scatter([y+xc for y in negycoordinate],[x+yc for x in negxcoordinate])
#     plt.scatter([y+xc for y in ycoordinate],[x+yc for x in negxcoordinate])
    
#     #plt.grid(1)
#     #plt.scatter(x, y, marker='s')
#     plt.show()


# def main():

#     r = int(input("Enter the radius of the circle: "))

#     xc,yc = map(int,input("Enter the arbitrary center (xc yc): ").split(' ',2))
#     c=xc,yc

#     CircleMidPoint(r,c)

# main()
