from .base import Figure
from .simple import Circle


class Rectangle(Figure):

    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height

    def draw(self, turtle):
        left = self.center_x - self.width / 2
        top = self.center_y + self.height / 2

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)  # point the turtle down
        sides = [self.height, self.width, self.height, self.width]
        for side in sides:
            turtle.forward(side)
            turtle.left(90)


class Pie(Figure):

    def __init__(self, radius, arg_degrees, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.arg_degrees = arg_degrees

    def draw(self, turtle):
        turtle.begin_fill()
        turtle.color(self.color)
        turtle.goto(self.center_x, self.center_y - self.radius)  # From docs: The center is radius units left of the turtle;
        turtle.pendown()
        turtle.circle(self.radius, self.arg_degrees)
        turtle.goto(self.center_x, self.center_y)
        turtle.end_fill()


class RegularPoligon(Circle):

    def __init__(self, num_sides, **kwargs):
        super().__init__(**kwargs)
        self.num_sides = num_sides

    def draw(self, turtle):
        super().move_pen(turtle)
        turtle.circle(self.radius, 360, self.num_sides)
