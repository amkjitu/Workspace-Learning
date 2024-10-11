from graphics import *

def bresLine(x1,y1,x2,y2):

    x1 = int(input("Enter the Starting point of x: "))
    y1 = int(input("Enter the Starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    win = GraphWin("LineDrawing", 500, 500)
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx
    print(f"x = {x}, y = {y}")

    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        print(f"x = {x}, y = {y}")

        pix = Point(x,y)
        pix.draw(win)
        
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

def bresLine(r=50,x=0):
    win = GraphWin("LineDrawing", 800, 600)
    y = r 
    d = 3 - 2*r;
    while (x <= y):
        #pix = Point(x,y)
        #pix.draw(win)
        win.plotPixel(x,y)
        
        if (d < 0):
            d = d + 4*x + 6;
        else: 
            d = d + 4*(x-y)+10;
            y=y-1
        x=x+1
        
    win.getMouse() # Pause to view result
    win.close()  



def main():
   
    bresLine()
    

if __name__ == "__main__":
    main()
