import turtle
g = 134
l = 120

print("Please add the number of operations:")
number_of_operations = input()
i = 0
while i < number_of_operations:
    turtle.left(g)
    turtle.forward(l)
    i += 1
