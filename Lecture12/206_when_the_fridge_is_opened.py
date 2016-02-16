try:
    file_name = input()
    with open(file_name, encoding='utf-8') as f:
        previous_temp = None
        for line in f:
            line = line.strip()
            if line:
                line_elements = line.split(',')
                if previous_temp is None:
                    previous_temp = float(line_elements[1])
                    continue

                if (float(line_elements[1]) - previous_temp) > 4:
                    print(line_elements[0])

                previous_temp = float(line_elements[1])
except:
    print("INVALID INPUT")