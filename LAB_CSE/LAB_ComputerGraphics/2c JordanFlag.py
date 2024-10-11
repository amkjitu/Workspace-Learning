import turtle
from  turtle import*
speed(0.5)
setup(800,495)

penup()
goto(-400, 250)
pendown()

color("black")
begin_fill()
forward(800)
right(90)
forward(165)
right(90)
forward(800)
end_fill()

color("white")
begin_fill()
left(180)
forward(800)
right(90)
forward(165)
right(90)
forward(800)
end_fill()

color("green")
begin_fill()
left(180)
forward(800)
right(90)
forward(165)
right(90)
forward(800)
end_fill()


penup()
goto(-400, 250)
pendown()
color("#CE1126")
begin_fill()
goto(-250, 0)
goto(-400, -250)
goto(-400, 1000)
end_fill()


penup()
goto(-300, 9)
pendown()
color("white")
begin_fill()
for _ in range(7):
    forward(80)
    right(180 - 180 / 7)
end_fill()

turtle.mainloop()




hideturtle()

