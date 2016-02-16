import os

w = input()
h = input()
d = input()
file = input()

try:
    w = float(w)
    h = float(h)
    d = float(d)
    package_sizes = [w, h, d]
    package_sizes.sort()

    if not os.path.isfile(file):
        raise ValueError()
    else:
        with open(file, encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    line_elements = line.strip().split(',')
                    medicine_sizes = line_elements[1:4]
                    medicine_sizes.sort()
                    if float(medicine_sizes[0]) <= package_sizes[0] and \
                        float(medicine_sizes[1]) <= package_sizes[1] and \
                        float(medicine_sizes[2]) <= package_sizes[2]:
                        print(line_elements[0])

except:
    print('INVALID INPUT')