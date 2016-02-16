import csv
import iso8601

try:
    file_name = 'sales.csv' #input()
    data = {}
    with open(file_name, encoding='utf-8') as f:
        lines = csv.reader(f, dialect='excel')
        for line in lines:
            if len(line) > 5:
                raise ValueError()

            product_key = line[0]
            country = line[1]
            city = line[2]
            sale_date = iso8601.parse_date(line[3])
            amount = float(line[4])

            key = city.lower() + "|" + country
            if key in data:
                data[key].append(product_key)
            else:
                data[key] = [product_key]

    found_unique_sales = False

    if not data:
        raise ValueError()

    for key in sorted(data.keys()):
        products_in_city = data[key]
        unique_sales = []
        for product in products_in_city:
            cities_with_sale = [key for key, products in data.items() if product in products]
            if len(cities_with_sale) == 1:
                unique_sales.append(product)

        key_elements = key.split('|')
        city = key_elements[0]
        unique_sales = set(unique_sales)
        if unique_sales:
            print("{},{}".format(city.title(), ",".join(sorted(unique_sales))))
            found_unique_sales = True

    if not found_unique_sales:
        print("NO UNIQUE SALES")
except:
    print("INVALID INPUT")
