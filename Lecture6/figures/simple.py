from .base import Figure


class Circle(Figure):

    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

    def draw(self, turtle):
        self.move_pen(turtle)
        turtle.circle(self.radius)

    def move_pen(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x, self.center_y - self.radius)  # From docs: The center is radius units left of the turtle;
        turtle.pendown()
        turtle.color(self.color)


class Square(Figure):

    def __init__(self, side, **kwargs):
        super().__init__(**kwargs)
        self.side = side

    def draw(self, turtle):
        half_side = self.side / 2
        left = self.center_x - half_side
        top = self.center_y + half_side

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)  # point the turtle down
        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)