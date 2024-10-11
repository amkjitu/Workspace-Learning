import turtle

def draw_rectangle(color, width, height):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_sun():
    turtle.pensize(2)
    turtle.color("yellow")
    turtle.penup()
    turtle.goto(0, 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.pensize(4)
    for _ in range(16):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(_ * 22.5)
        turtle.pendown()
        turtle.forward(70)

def draw_argentina_flag():
    screen = turtle.Screen()
    screen.setup(600, 400)
    turtle.speed(0)

    # Draw the light blue rectangle (top stripe)
    turtle.penup()
    turtle.goto(-300, 133.33)
    turtle.pendown()
    draw_rectangle("#74ACDF", 600, 133.33)

    # Draw the white rectangle (middle stripe)
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()
    draw_rectangle("white", 600, 133.33)

    # Draw the light blue rectangle (bottom stripe)
    turtle.penup()
    turtle.goto(-300, -133.33)
    turtle.pendown()
    draw_rectangle("#74ACDF", 600, 133.33)

    # Draw the sun in the middle stripe
    draw_sun()

    turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_argentina_flag()
