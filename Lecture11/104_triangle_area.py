import math

a = input()
b = input()
c = input()

try:
    a = float(a)
    b = float(b)
    c = float(c)

    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print("{:.2f}".format(s))
except:
    print("INVALID INPUT")