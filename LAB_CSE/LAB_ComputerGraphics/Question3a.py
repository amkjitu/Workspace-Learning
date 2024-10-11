# # Import the graphics library
# from graphics import *

# def DDAAlgo(x1, y1, x2, y2, win):

#     x0,y0 = x1, y1
#     xe,ye = x2, y2

#     dy = ye-y0
#     dx = xe-x0
#     if dx == 0:
#         dx=1000
#     m = dy/dx
    
#     x=x0
#     y=y0

#     if(abs(m)<=1):
#         # Iteration, di, di+1, (xi+1,yi+1)
#         print("|m| = {:^2} | {:^3} | {:^2},{:^2}".format(abs(m),'Iteration','(xi+1','yi+1)'))
#         i=0
#         while(x!=xe):
#             print("           {:^11}  {:^3} , {:^3}".format(i,x,y))
#             x=x+1
#             y=y+m
#             i+=1
#             p = Point(x, y)
#             p.draw(win)
#     else:
#         # Iteration, di, di+1, (xi+1,yi+1)
#         print("|m| = {:^2} | {:^3} | {:^2},{:^2}".format(abs(m),'Iteration','(xi+1','yi+1)'))
#         i=0
#         while(y!=ye):
#             print("           {:^11}  {:^3} , {:^3}".format(i,x,y))
#             x=x+(1/m)
#             y=y+1
#             i+=1
#             p = Point(x, y)
#             p.draw(win)


# def main():
    
#     w,h = map(int,input("Enter Screen (weight height): ").split(' ',2))
#     x1,y1 = map(int,input("Enter P1 (x1 y1): ").split(' ',2))
#     x2,y2 = map(int,input("Enter P2 (x2 y2): ").split(' ',2))

#     win = GraphWin("Rectangle",w,h)

#     x3 = x2
#     y3 = y1
#     x4 = x1
#     y4 = y2

#     DDAAlgo(x1, y1, x3, y3, win)
#     DDAAlgo(x3, y3, x2, y2, win)
#     DDAAlgo(x2, y2, x4, y4, win)
#     DDAAlgo(x4, y4, x1, y1, win)

#     win.getMouse()
#     win.close()


#-----------------------------#


from graphics import *

def DDAAlgo(x1, y1, x2, y2, win):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    xi = dx / steps
    yi = dy / steps

    x = x1
    y = y1

    for i in range(steps + 1):
        
        xint = round(x)
        yint = round(y)

        p = Point(xint, yint)

        p.draw(win)

        x += xi
        y += yi

def main():
    
    w,h = map(int,input("Enter Screen (weight height): ").split(' ',2))
    x1,y1 = map(int,input("Enter P1 (x1 y1): ").split(' ',2))
    x2,y2 = map(int,input("Enter P2 (x2 y2): ").split(' ',2))

    win = GraphWin("-",w,h)

    x3 = x2
    y3 = y1
    x4 = x1
    y4 = y2

    DDAAlgo(x1, y1, x3, y3, win)
    DDAAlgo(x3, y3, x2, y2, win)
    DDAAlgo(x1, y1, x2, y2, win)
    DDAAlgo(x2, y2, x4, y4, win)
    DDAAlgo(x4, y4, x1, y1, win)

    win.getMouse()
    win.close()

main()

#-----------------------------#

# import matplotlib.pyplot as plt

# def dda_algorithm(x1, y1, x2, y2):
#     points = []
#     dx = x2 - x1
#     dy = y2 - y1
#     steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
#     x_increment = dx / steps
#     y_increment = dy / steps
#     x, y = x1, y1

#     for _ in range(steps):
#         points.append((round(x), round(y)))
#         x += x_increment
#         y += y_increment

#     return points

# def draw_rectangle(x1, y1, x2, y2, resolution_x, resolution_y):
#     # Limit points within display resolution
#     x1 = max(0, min(x1, resolution_x - 1))
#     x2 = max(0, min(x2, resolution_x - 1))
#     y1 = max(0, min(y1, resolution_y - 1))
#     y2 = max(0, min(y2, resolution_y - 1))

#     # Find the diagonal endpoints
#     diagonal_points = dda_algorithm(x1, y1, x2, y2)

#     # Calculate other two corners of the rectangle
#     x3, y3 = x1, y2
#     x4, y4 = x2, y1

#     # Draw lines to form the rectangle
#     points1 = dda_algorithm(x1, y1, x3, y3)
#     points2 = dda_algorithm(x1, y1, x4, y4)
#     points3 = dda_algorithm(x2, y2, x3, y3)
#     points4 = dda_algorithm(x2, y2, x4, y4)

#     # Combine all points to get the rectangle
#     rectangle_points = set(diagonal_points + points1 + points2 + points3 + points4)

#     return rectangle_points

# def main():
#     # Display resolutions
#     resolution_x = 1280
#     resolution_y = 720

#     # Diagonal endpoints
#     x1, y1 = 5, 7
#     x2, y2 = 700, 600

#     # Draw the rectangle
#     rectangle_points = draw_rectangle(x1, y1, x2, y2, resolution_x, resolution_y)

#     # Extract x and y coordinates from the points
#     x_coords, y_coords = zip(*rectangle_points)

#     # Plot the rectangle
#     plt.scatter(x_coords, y_coords, c='b')
#     plt.xlim(0, resolution_x - 1)
#     plt.ylim(0, resolution_y - 1)
#     plt.gca().set_aspect('equal', adjustable='box')
#     plt.show()

# if __name__ == "__main__":
#     main()