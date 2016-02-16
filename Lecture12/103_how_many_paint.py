import math

METRAS_PER_FLAKON = 1.76

try:
    w = float(input())
    h = float(input())

    result = math.ceil(w * h / METRAS_PER_FLAKON)
    print(result)
except:
    print("INVALID DATA")

