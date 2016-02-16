import math

try:
    litres = 2 #float(input())
    if litres <=0:
        raise ValueError()
    file_name = 'containers.txt' #input()
    found_bidons = []
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                line_elements = line.split(",")
                if len(line_elements) > 3:
                    raise ValueError()
                bidon_name = line_elements[0]
                r = float(line_elements[1]) / 10
                h = float(line_elements[2]) / 10
                if r <= 0 or h <= 0:
                    raise ValueError()
                obem = math.pi * r * r * h

                if obem >= litres:
                    found_bidons.append((obem, bidon_name))

    if not found_bidons:
        print("NO SUITABLE CONTAINER")
    else:
        result_bidon = min(found_bidons)
        print("{}".format(result_bidon[1]))
except:
    print("INVALID INPUT")