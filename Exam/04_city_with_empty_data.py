import csv
import iso8601
from datetime import date

try:
    file_name = 'city-temperature-data.csv' #input()
    cities = set()
    data = {}
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                line_elements = line.split(',')
                date_string = str(line_elements[0])
                date_elements = date_string.split('-')
                dt = date(int(date_elements[0]), int(date_elements[1]), int(date_elements[2]))
                city = line_elements[1]
                cities.add(city)
                temperature = float(line_elements[2])
                if dt in data:
                    data[dt].append(city)
                else:
                    data[dt] = [city]

    found_empty_cities = False
    if not cities:
        raise ValueError()

    for date in sorted(data.keys()):
        missing_cities = []
        current_cities = set(data[date])
        # missing_cities = cities.difference(current_cities)
        missing_cities = [city for city in cities if city not in current_cities]
        if missing_cities:
            print("{},{}".format(date.isoformat(), ",".join(sorted(missing_cities))))
            found_empty_cities = True

    if not found_empty_cities:
        print("ALL DATA AVAILABLE")
except:
    print("INVALID INPUT")
