import turtle

side = 20
fill_cell = True

for row in range(1, 8):
    for cell_number in range(8):
        if cell_number != 0:
            fill_cell = fill_cell ^ True

        if fill_cell:
            turtle.begin_fill()

        for j in range(4):
            turtle.forward(side)
            turtle.left(90)

        if fill_cell:
            turtle.end_fill()

        turtle.forward(side)

    turtle.penup()
    turtle.goto(0, -side * row)
    turtle.pendown()

turtle.exitonclick()
