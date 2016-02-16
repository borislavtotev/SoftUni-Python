import turtle
i = 10
k = 0
for k in range(1000):
    if k % 10 == 0:
        turtle.degrees(180)
    else:
        turtle.degrees(90)

    turtle.left(i % 25)
    turtle.forward(25)

