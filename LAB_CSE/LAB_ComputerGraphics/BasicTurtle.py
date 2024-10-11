import random
import time
from multiprocessing import Process
from turtle import Turtle,Screen
 
##Screen Shape and Speed
t = Turtle()
scrn = Screen()
t.shape('classic')
t.speed(5)

# ## Program: Endless Square Loop
# s=1;

# for i in range(50):

#     s=s+(i/5)
#     t.forward(s)
#     t.right(90)

#     s=s+(i/5)
#     t.forward(s)
#     t.right(90)

#     s=s+(i/5)
#     t.forward(s)
#     t.right(90)

#     s=s+(i/5)
#     t.forward(s)
#     t.right(90)

# ## Program: DashLline
# def dash_line(len, dash):
#     for i in range(len):
#         t.forward(dash)
#         t.penup()
#         t.forward(dash)
#         t.pendown()

# dash_line(20, 1)
# t.right(90)

# dash_line(20, 1)
# t.right(90)

# ## Program: Square
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# ## Program: Triangle
# for i in range(3):
#     t.forward(100)
#     t.right(120)

# ## Program: Hexagon
# for i in range(6):
#     t.right(60)
#     t.forward(100)

# ## Program: Star
# for i in range(5):
#     t.left(144)
#     t.forward(100)
# t.penup()
# t.setpos(-100,90)
# t.pendown()
# for i in range(6):
#     t.left(60)
#     t.forward(100)
#     t.right(120)
#     t.forward(100)

# ## Circle
# def Circle():
#     count = 0
#     while(count < 360):
#         t.forward(2)
#         t.left(1)
#         count = count + 1

# ## Program: Vibrate Circle
# def VibrateCircle(size):
#     scrn.bgcolor("black")
#     t.pencolor("red")
#     t.hideturtle()
#     a = 0.0
#     b = 0
#     t.speed(0)
#     t.penup()
#     t.goto(0, 200)
#     t.pendown()
#     while (True):
#         t.forward(a)
#         t.right(b)
#         a += size
#         b += 1
#         if b == 200:
#             break
# #VibrateCircle(0.8)
        

# ## Program: National Flag
# def rectangle(color):
#     t.begin_fill()
#     t.fillcolor(color)
#     for i in range(2):
#         t.forward(300)
#         t.right(90)
#         t.forward(200)
#         t.right(90)
#     t.end_fill()
# def circle(color):
#     t.begin_fill()
#     t.fillcolor(color)
#     t.circle(-70)
#     t.end_fill()

# t.penup()
# t.goto(0, -200)
# t.pendown()
# t.goto(0, 200)
# rectangle('green')
# t.goto(0, 170)
# t.color('green')
# t.forward(150)
# circle('red')

# ## Program: Analog Clock

# #inner circle
# x=0
# y=0
# t.home()
# t.write((x,y))
# y = -120
# t.penup()
# t.goto(x,y)
# t.pendown()
# t.circle(120)
# t.begin_fill()
# t.fillcolor('skyblue')

# #outter circle
# t.penup()
# t.home()
# y = -80
# t.goto(x,y)
# t.pendown()
# t.circle(80)
# t.end_fill()

# #hour writing
# t.penup()
# t.home()
# t.left(90)
# for i in range(1,13):
#     t.right(360/12)
#     t.forward(100)
#     t.write(i)
#     t.goto(0,0)

# def draw_hour_arm():
#     t.penup()
#     t.home()
#     t.right(180)
#     t.pendown()
#     t.pensize(3)
#     t.forward(60)

# def draw_minute_arm():
#     t.penup()
#     t.home()
#     t.right(270)
#     t.pendown()
#     t.pensize(2)
#     t.forward(80)

# def draw_second_arm():
#     t.pensize(1)
#     angle = 0
#     while True:
#         first_start = 1
#         if first_start == 1:
#             t.penup()
#             t.home()
#             t.left(90)
#             first_start = 2
#         t.right(angle)    
#         t.pendown()
#         t.forward(95)
#         time.sleep(1)
#         t.undo()
#         t.penup()
#         t.goto(0,0)
#         angle = angle + (360/60)
#         t.right(360/60)

# draw_hour_arm()
# draw_minute_arm()
# draw_second_arm()

# ## Program: A night sky with stars
# import random
# scrn.screensize(800,500,bg='black')
# t.hideturtle()

# def ranXY():
#     x=random.randint(-400,250)
#     y=random.randint(-400,250)
#     return x,y

# def ranColor():
#     scrn.colormode(255)
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return r,g,b

# def moonMoving(xs,ys,xe,ye,color='black'):
#     t.pencolor(color)
#     t.speed(0.5)
#     t.goto(xs,ys)
#     for i in range(ye):
#         t.goto(xe,200-i)
#         t.pencolor('black')
#         t.begin_fill()
#         t.fillcolor('white')
#         t.circle(50)
#         t.end_fill()

# def moonVanishing(vanish,ii=0.0,):
#     t.speed(0.4)
#     t.pencolor('black')
#     t.penup()
#     t.goto(120,120)
#     t.left(95)
    
#     for i in range(180):
#         ii=ii+vanish
#         t.begin_fill()
#         t.fillcolor('black')
#         t.circle(35.0+ii)
#         t.end_fill()

# def star(stsize):
#     t.speed(0.5)
#     stsize = random.randint(3,stsize)
#     r,g,b=ranColor()
#     x,y=ranXY()
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.pencolor(r,g,b)
#     t.begin_fill()
#     t.fillcolor(r,g,b)
#     for i in range(5):
#         t.forward(stsize)
#         t.right(144)
#     t.end_fill()

# def bloomingStars():
#     for i in range(100):
#         star(11)
#         if (i==13):
#             moonMoving(0,250,0,150,'black')
#         elif(i==20):
#             moonVanishing(0.2)
# def titleNight():
#     for i in range(2):
#         t.showturtle()
#         t.speed(2)
#         t.goto(-125-i,-145-i)
#         t.pencolor('white')
#         t.write('A Night Sky with Turtle.py',font=("Arial", 16, "normal"),move=True)

# bloomingStars()
# titleNight()

# if __name__ == '__main__':
#     p1=Process(target=moon())
#     p2=Process(target=bloomingStars())
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()


        

# ## Program: Cube
# def square(sidelen):
#     for i in range(4):
#         t.forward(sidelen)
#         t.left(90)

# def cube(angle,sidelen):
#     square(sidelen)
#     t.left(angle)
#     t.forward(sidelen)
#     t.right(angle)
#     square(sidelen)#2 square done
#     t.left(90)
#     t.forward(sidelen)
#     t.left(90+angle)
#     t.forward(sidelen)
#     t.right(180+angle)
#     t.forward(sidelen)
#     t.left(angle)
#     t.forward(sidelen)
#     t.right(90+angle)
#     t.forward(sidelen)
#     t.right(90-angle)
#     t.forward(sidelen)

# cube(120,80)


#t.mainloop()  
scrn.exitonclick()
