import os

product_code = input()
file_name = input()

price_by_city = {}
try:
    if not os.path.isfile(file_name):
        raise ValueError()

    with open(file_name) as f:
        for line in f:
            line = line.strip()
            line = line.replace('"', "")
            if line:
                line_elements = line.split(',')
                if line_elements[0] == product_code:
                    price_by_city[float(line_elements[4])] = line_elements[2]

    sorted_prices_by_city = sorted(price_by_city.items())
    print(sorted_prices_by_city[0][1])
except:
    print("INVALID DATA")
