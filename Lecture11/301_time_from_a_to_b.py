import os

file_name = input()

try:
    if not os.path.isfile(file_name):
        raise ValueError()
    else:
        with open(file_name) as f:
            time_sum = 0
            for line in f:
                line = line.strip()
                if line:
                    line_elements = line.split(',')
                    current_time = (float(line_elements[1])-float(line_elements[0]) + 1) / float(line_elements[2])
                    time_sum += current_time

        print("{:.2f}".format(time_sum))
except:
    print("INVALID DATA")