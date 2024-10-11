import matplotlib.pyplot as plt
#import CartesianWindow as window
#import CartesianWindowP as window

#window.CWindow(10,20)

def LINEDDA(sp,ep):
    
    xcoordinate = []
    ycoordinate = []

    x0,y0=sp
    xe,ye=ep

    dy = ye-y0
    dx = xe-x0
    m = dy/dx
    
    x=x0
    y=y0

    xcoordinate.append(x)
    ycoordinate.append(y)

    if(abs(m)<=1):
        # Iteration, di, di+1, (xi+1,yi+1)
        print("|m| = {:^2} | {:^3} | {:^2},{:^2}".format(abs(m),'Iteration','(xi+1','yi+1)'))
        i=0
        while(x!=xe):
            print("           {:^11}  {:^3} , {:^3}".format(i,x,y))
            x=x+1
            y=y+m
            xcoordinate.append(x)
            ycoordinate.append(y)
            i+=1
    else:
        # Iteration, di, di+1, (xi+1,yi+1)
        print("|m| = {:^2} | {:^3} | {:^2},{:^2}".format(abs(m),'Iteration','(xi+1','yi+1)'))
        i=0
        while(y!=ye):
            print("           {:^11}  {:^3} , {:^3}".format(i,x,y))
            x=x+(1/m)
            y=y+1
            xcoordinate.append(x)
            ycoordinate.append(y)
            i+=1

    plt.scatter(xcoordinate,ycoordinate)
    #plt.scatter(x, y)
    plt.show()


def main():

    x0,y0 = map(int,input("Enter start point (x0 y0): ").split(' ',2))
    xe,ye = map(int,input("Enter finishing point (xe ye): ").split(' ',2))

    sp=x0,y0
    ep=xe,ye

    LINEDDA(sp,ep)

main()

        
