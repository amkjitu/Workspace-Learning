import turtle

def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def draw_graph_paper(size, rows, columns):
    turtle.speed(0)
    turtle.hideturtle()

    cell_width = size / columns
    cell_height = size / rows

    # Draw horizontal lines
    for i in range(rows + 1):
        y = i * cell_height - size / 2
        draw_line(-size / 2, y, size / 2, y)

    # Draw vertical lines
    for i in range(columns + 1):
        x = i * cell_width - size / 2
        draw_line(x, -size / 2, x, size / 2)

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Graph Paper")
    screen.setup(width=600, height=600)
    screen.bgcolor("white")

    draw_graph_paper(400, 20, 20)

    turtle.done()
