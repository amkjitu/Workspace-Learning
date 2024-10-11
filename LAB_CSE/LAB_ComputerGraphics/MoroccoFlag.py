# from turtle import *

# # def star(stsize):
# #     t.speed(0.5)
# #     stsize = random.randint(3,stsize)
# #     r,g,b=ranColor()
# #     x,y=ranXY()
# #     t.penup()
# #     t.goto(x,y)
# #     t.pendown()
# #     t.pencolor(r,g,b)
# #     t.begin_fill()
# #     t.fillcolor(r,g,b)
# #     for i in range(5):
# #         t.forward(stsize)
# #         t.right(144)
# #     t.end_fill()

# # Initialize the screen
# screen = Screen()
# # setup the screen
# screen.setup(600, 450)
# # Change the position of the cursor
# setpos(-200, -100)
# # change the pen size, color, speed, title
# pensize(4)
# fillcolor('red')
# title("Morocco Flag")
# # speed(0)
# # Initial Variables
# n1 = 450
# n2 = 300
# # Create a box of the flag
# begin_fill()
# for i in range(2):
#     fd(n1)
#     left(90)
#     fd(n2)
#     left(90)
# end_fill()
# colors = ['red','green','blue','yellow','black']
# # Change the position to the middle of the BOX
# up(); setpos(-30, 30); down()
# color('green')
# # Coordinates of the star on the flag
# seth_fd = [(60, 100), (-60, 100), (150, 120), (0, 110), (-150, 120)]
# # Draw the star
# i=0
# for s, f in seth_fd:
#     begin_fill()
    
#     fillcolor(colors[i])
#     seth(s)
#     end_fill()
#     fd(f)
#     i=i+1


# # write text
# up(); setpos(-65, -150); down()
# write("Morocco Won", font="normal 20 bold")

# # hide the turtle
# hideturtle()
# # static screen
# done()

# # Import the turtle module
# import turtle
# import math
# # Create a turtle object
# t = turtle.Turtle()

# # Set the speed and the pen size
# t.speed(0)
# t.pensize(4)

# # Define a function to draw a filled triangle
# def draw_triangle(x, y, size, color):
#   # Move the turtle to the given position
#   t.penup()
#   t.goto(x, y)
#   t.pendown()
  
#   # Set the fill color and start filling
#   t.fillcolor(color)
#   t.begin_fill()
  
#   # Draw the three sides of the triangle
#   for i in range(3):
#     t.forward(size)
#     t.left(120)
  
#   # End filling
#   t.end_fill()

# # Define a list of colors for the star sides
# colors = ['red', 'orange', 'yellow', 'green', 'blue']

# # Draw the five sides of the star with different colors
# for i in range(5):
#   # Calculate the angle and the distance for each side
#   angle = i * 72 - 18
#   distance = 100
  
#   # Convert angle from degrees to radians
#   angle = angle * 3.14 / 180
  
#   # Calculate the x and y coordinates for each side
#   x = distance * math.cos(angle)
#   y = -distance * math.sin(angle)
  
#   # Draw each side with a different color
#   draw_triangle(x, y, distance, colors[i])

# # Hide the turtle
# t.hideturtle()

# # Keep the window open until the user clicks on it
# turtle.done()


import turtle

def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_jordanian_flag():
    turtle.speed(15)
    width, height = 600, 400

    # Draw the black stripe
    turtle.penup()
    turtle.goto(-width/2, height/6)
    turtle.pendown()
    draw_rectangle("black", width, height/3)

    # Draw the white stripe
    turtle.penup()
    turtle.goto(-width/2, height/2)
    turtle.pendown()
    draw_rectangle("white", width, height/3)

    # Draw the green stripe
    turtle.penup()
    turtle.goto(-width/2, -height/6)
    turtle.pendown()
    draw_rectangle("green", width, height/3)

    # Draw the red triangle
    turtle.penup()
    turtle.goto(-width/2, -height)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.goto(-width/2, -height/6)
    turtle.goto(width/2 - height/6, 1)
    turtle.goto(-width/2, height/6)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    draw_jordanian_flag()
