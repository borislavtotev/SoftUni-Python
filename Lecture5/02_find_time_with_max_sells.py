import csv
from pprint import pprint

from datetime import datetime

sells_by_day = {}
sells_by_hour = {}

with open('./sales.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        str_date = str(row[0])
        sell_date_time = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
        sell_date = sell_date_time.strftime("%Y-%m-%d")
        sell_sum = float(row[1])
        if sell_date in sells_by_day:
            sells_by_day[sell_date] += sell_sum
        else:
            sells_by_day[sell_date] = sell_sum

        sell_hour = sell_date_time.hour
        if sell_hour in sells_by_hour:
            sells_by_hour[sell_hour] += sell_sum
        else:
            sells_by_hour[sell_hour] = sell_hour

#pprint(sells_by_day)
max_sells_day = max(sells_by_day, key=sells_by_day.get)
print("The day with maximum sells is {}. Total sells this day are for {:2f}".format(max_sells_day, sells_by_day[max_sells_day]))

#pprint(sells_by_hour)
max_sells_hour = max(sells_by_hour, key=sells_by_hour.get)
print("The hour with maximum sells is {}. Total sells this hour are for {:2f}".format(max_sells_hour, sells_by_hour[max_sells_hour]))