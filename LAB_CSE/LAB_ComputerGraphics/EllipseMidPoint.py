import matplotlib.pyplot as plt
import CartesianWindow as window
#import CartesianWindowP as window
#window.CWindow(240,460)

###only a,b ###########
def EllipseMidPoint(a,b):
    
    xcoordinate = []
    ycoordinate = []

    x=0
    y=b
    aa = a*a
    bb = b*b
    aa2 = aa*2
    bb2 = bb*2
    fx=0 #ini partial derivative
    fy=aa2*b #ini partial derivative
    p = bb - aa*b + 0.25*aa # initial decision parameter
    
    ##region-1 decision parameter p
    while(fx<fy): #|m|<1
        
        xcoordinate.append(x)
        ycoordinate.append(y)
        fx=fx+bb2
        x=x+1

        if(p<0):
            p_next=p+fx+bb
        else:
            y=y-1
            fy = fy - aa2
            p_next=p+fx+bb-fy

        # Iteration, di, di+1, (xi+1,yi+1)
        if x==1:
            print("{:^3}|  {:^7}| {:^6}|  {:^2},{:^2}".format('Iteration','pi','pi+1','(xi+1','yi+1)'))
            print("  {:^5}   {:^7}  {:^9}   {:^3}, {:^3}".format(0,p,p_next,0,b))
            print("  {:^5}   {:^7}  {:^9}   {:^3}, {:^3}".format(x,p,p_next,x,y))
        else:
            print("  {:^5}   {:^7}  {:^9}   {:^3}, {:^3}".format(x,p,p_next,x,y))

        p=p_next

    ##region-2 decision parameter q
    #set pixel at (xk,yk) where region-1 ends  
    xcoordinate.append(x)
    ycoordinate.append(y)
    q=bb*(x+0.5)*(x+0.5) + aa*(y-1)*(y-1) - aa*bb
    
    while (y>0): #stop at y=0
        y=y-1
        fy = fy - aa2
        if(q>=0):
            q=q-fy+aa
        else:
            x=x+1
            fx=fx+bb2
            q=q+fx-fy+aa

        xcoordinate.append(x)
        ycoordinate.append(y)
        

    negxcoordinate = [ -x for x in xcoordinate]
    negycoordinate = [ -y for y in ycoordinate]

    #Iterations:

    plt.scatter(xcoordinate,ycoordinate)
    plt.scatter(negxcoordinate,ycoordinate)
    plt.scatter(negxcoordinate,negycoordinate)
    plt.scatter(xcoordinate,negycoordinate)
    
    plt.grid(1)
    #plt.scatter(x, y, marker='s')
    plt.show()


def main():

    a,b = map(int,input("Enter rx ry : ").split(' ',2))
    print("Length of major and minor axis : {} {}".format(a,b))

    EllipseMidPoint(a,b)

main()

# ###with center###########
# def EllipseMidPoint(a,b,c):
    
#     xcoordinate = []
#     ycoordinate = []

#     xc,yc=c
#     x=0
#     y=b
#     aa = a*a
#     bb = b*b
#     aa2 = aa*2
#     bb2 = bb*2
#     fx=0 #ini partial derivative
#     fy=aa2*b #ini partial derivative
#     p = bb - aa*b + 0.25*aa # initial decision parameter
    
#     ##region-1 decision parameter p
#     while(fx<fy): #|m|<1
        
#         xcoordinate.append(x)
#         ycoordinate.append(y)
#         fx=fx+bb2
#         x=x+1

#         if(p<0):
#             p_next=p+fx+bb
#         else:
#             y=y-1
#             fy = fy - aa2
#             p_next=p+fx+bb-fy

#         # Iteration, di, di+1, (xi+1,yi+1)
#         if x==1:
#             print("{:^3}|  {:^7}| {:^6}|  {:^2},{:^2}".format('Iteration','pi','pi+1','(xi+1','yi+1)'))
#             print("  {:^5}   {:^7}  {:^9}   {:^3}, {:^3}".format(0,p,p_next,0,b))
#             print("  {:^5}   {:^7}  {:^9}   {:^3}, {:^3}".format(x,p,p_next,x,y))
#         else:
#             print("  {:^5}   {:^7}  {:^9}   {:^3}, {:^3}".format(x,p,p_next,x,y))

#         p=p_next

#     ##region-2 decision parameter q
#     #set pixel at (xk,yk) where region-1 ends  
#     xcoordinate.append(x)
#     ycoordinate.append(y)
#     q=bb*(x+0.5)*(x+0.5) + aa*(y-1)*(y-1) - aa*bb
    
#     while (y>0): #stop at y=0
#         y=y-1
#         fy = fy - aa2
#         if(q>=0):
#             q=q-fy+aa
#         else:
#             x=x+1
#             fx=fx+bb2
#             q=q+fx-fy+aa

#         xcoordinate.append(x)
#         ycoordinate.append(y)
        
#     negxcoordinate = [ -x for x in xcoordinate]
#     negycoordinate = [ -y for y in ycoordinate]

#     # Add the origin coordinates to the x and y values before plotting them
#     plt.scatter([x+xc for x in xcoordinate],[y+yc for y in ycoordinate])
#     plt.scatter([x+xc for x in negxcoordinate],[y+yc for y in ycoordinate])
#     plt.scatter([x+xc for x in negxcoordinate],[y+yc for y in negycoordinate])
#     plt.scatter([x+xc for x in xcoordinate],[y+yc for y in negycoordinate])
    
#     #plt.grid(1)
#     #plt.scatter(x, y, marker='s')
#     plt.show()


# def main():

#     a,b = map(int,input("Enter rx ry : ").split(' ',2))
#     print("Length of major and minor axis : {} {}".format(a,b))

#     xc,yc = map(int,input("Enter the arbitrary center (xc yc): ").split(' ',2))
#     c=xc,yc

#     EllipseMidPoint(a,b,c)

# main()

        
