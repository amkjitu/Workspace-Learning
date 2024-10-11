# ### 1. Drawing a right-angle
# import turtle    # importing the module
# trtl = turtle.Turtle()    #making a turtle object of Turtle class for drawing
# screen=turtle.Screen()    #making a canvas for drawing
# screen.setup(400,300)    #choosing the screen size
# screen.bgcolor('black')    #making canvas black
# trtl.pencolor('red')    #making colour of the pen red
# trtl.pensize(5)    #choosing the size of pen nib
# trtl.speed(1)    #choosing the speed of drawing
# trtl.shape('turtle')   #choosing the shape of pen nib
# trtl.forward(150)    #drawing a line of 200 pixels
# trtl.right(90)    #asking turtle to turn 90 degrees
# trtl.forward(150)    #drawing a line of 200 pixels
# trtl.penup()    # preparing for moving pen without drawing
# trtl.setpos(-140,-120)    # making the new position of the turtle
# trtl.pendown()   # bringing the pen down for drawing again
# trtl.pencolor('green')    # choosin the pen colour as green
# trtl.write('Vivax Solutions', font=("Arial", 20, "bold"))    # chosing the font
# trtl.penup()
# #trtl.ht()    # hiding the turtle from the screen

### Drawing Multiple Squares
import turtle
vivax=turtle.Turtle()
def Multiple_Squares(length, colour):
  vivax.pencolor(colour)
  vivax.pensize(4)
  vivax.forward(length)
  vivax.right(90)
  vivax.forward(length)
  vivax.right(90)
  vivax.forward(length)
  vivax.right(90)
  vivax.forward(length)
  vivax.right(90)
  vivax.setheading(360)
  vivax.ht()
for i in range(50,110,10):
  Multiple_Squares(i,"red")

# ### Creating a Graph Paper

# import turtle
# trtl=turtle.Turtle()
# scrn=turtle.Screen()
# trtl.speed(10)
# for i in range(0,400,20):
#     trtl.pencolor('lightgrey')
#     trtl.penup()
#     trtl.setpos(-200+i,-200)
#     if i==0:
#         trtl.left(90)
#         trtl.pendown()
#         trtl.forward(400)
#         trtl.backward(400)
# for i in range(0,400,20):
#     trtl.pencolor('lightgrey')
#     trtl.penup()
#     trtl.setpos(-200,-200+i)
#     if i==0:
#         trtl.right(90)
#         trtl.pendown()
#         trtl.forward(400)
#         trtl.backward(400)
# trtl.penup()
# trtl.home()
# trtl.pendown()
# trtl.pencolor('black')
# trtl.backward(200)
# trtl.forward(400)
# trtl.backward(200)
# trtl.left(90)
# trtl.forward(200)
# trtl.backward(400)
# trtl.penup()
# trtl.setpos(5,5)
# trtl.pendown()
# trtl.write(0)
# trtl.penup()
# trtl.setpos(190,5)
# trtl.pendown()
# trtl.write("x")
# trtl.penup()
# trtl.setpos(5,190)
# trtl.pendown()
# trtl.write("y")
# trtl.penup()
# trtl.setpos(80,-180)
# trtl.pendown()
# trtl.write("Vivax Solutions")
# #trtl.ht()

#t.exitonclick()