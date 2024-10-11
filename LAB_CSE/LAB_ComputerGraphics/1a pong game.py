import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=2)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=2)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Function to move paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)

# Function to move paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)

# Function to move paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)

# Function to move paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Score variables
score_a = 0
score_b = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundary checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Paddle collision
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.color("blue")
        ball.dx *= -1
    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.color("red")
        ball.dx *= -1

    # Score update
    if ball.xcor() > 390:
        score_a += 1
        score_display.clear()
        score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                            font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        score_display.clear()
        score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                            font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1