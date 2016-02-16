try:
    file_name = 'steps.txt' #input()
    result_elements = {}
    x = 0
    y = 0
    found_step = False
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                line_elements = line.split()
                if len(line_elements) > 2:
                    raise ValueError()
                direction = line_elements[0]
                step = float(line_elements[1])
                x = x + step if direction == "right" else x
                x = x - step if direction == "left" else x
                y = y + step if direction == "up" else y
                y = y - step if direction == "down" else y
                if direction not in ["right", "left", "up", "down"]:
                    raise ValueError()
                found_step = True

    if found_step:
        print("X {:.3f}".format(x))
        print("Y {:.3f}".format(y))
    else:
        raise ValueError()
except:
    print("INVALID INPUT")