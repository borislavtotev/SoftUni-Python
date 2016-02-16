import turtle
print('Line Lenght:')
lenght = input()

print('Rotate degrees:')
degrees = input()

while True:
    turtle.left(int(degrees))
    turtle.forward(int(lenght))

