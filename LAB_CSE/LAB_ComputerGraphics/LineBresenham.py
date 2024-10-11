import matplotlib.pyplot as plt
#import CartesianWindow as window
#import CartesianWindowP as window

#window.CWindow(10,20)

def LINEBresenham(sp,ep):
    
    xcoordinate = []
    ycoordinate = []

    x0,y0=sp
    xe,ye=ep

    dy = ye-y0
    dx = xe-x0
    m = dy/dx

    dT = 2*(dy-dx)
    dS = 2*dy
    d = 2*dy - dx

    print(m)
    x=x0
    y=y0

    while(x!=xe):
        if(d>=0):
            xcoordinate.append(x)
            ycoordinate.append(y)
            y=y+1
            d=d+(2*dy)-(2*dx);  
        else:
            xcoordinate.append(x)
            ycoordinate.append(y)
            d=d+(2*dy) 
        x=x+1

    #Iterations:

    plt.scatter(xcoordinate,ycoordinate)
    #plt.scatter(x, y)
    plt.show()


def main():

    x0,y0 = map(int,input("Enter x0 y0: ").split(' ',2))
    print("{} {}".format(x0,y0))

    xe,ye = map(int,input("Enter xe ye: ").split(' ',2))
    print("{} {}".format(xe,ye))

    sp=x0,y0
    ep=xe,ye

    LINEBresenham(sp,ep)

main()

        
