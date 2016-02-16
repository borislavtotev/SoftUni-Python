import math

try:
    list_area = 0.8 #float(input())
    h = 1.23#float(input())
    w = 0.78#float(input())
    d = 0.5#float(input())

    area = 2*(h * w + h * d + w * d) * 1.098
    result = area / list_area
    result = math.ceil(result)
    print(result)
except:
    print("INVALID INPUT")