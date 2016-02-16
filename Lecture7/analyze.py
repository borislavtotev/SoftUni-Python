import sys
import os
import csv
import operator
from pprint import pprint

from product import Product
from sale import Sale

def main():
    if len(sys.argv) < 3:
        print("You need to add catalog as first argument and sales as second in csv format!")
        return 1

    #try:
    product_catalog = load_product_catalog(sys.argv[1])
    sales = load_sells(sys.argv[2])

    print("Обобщение:\n-----------------------------")
    print("\tОбщ брой продажби: {}".format(len(sales)))

    sell_sum = sum(float(sale.price) for sale in sales)
    print("\tОбщо сума продажби: {:.2f} €".format(sell_sum))

    avg_sell = sell_sum / len(sales)
    print("\tСредна цена на продажба: {:.6f} €".format(avg_sell))

    sell_with_min_datetime = min(sales, key=lambda s: s.sell_datetime)
    print("\tНачало на период на данните: {}".format(sell_with_min_datetime.sell_datetime))
    sell_with_max_datetime = max(sales, key=lambda s: s.sell_datetime)
    print("\tКрай на период на данните: {}".format(sell_with_max_datetime.sell_datetime))

    sales_by_category = {}
    sales_by_city = {}
    sales_by_datetime = {}

    for sale in sales:
        sale_category = product_catalog[sale.product_id].category
        if sale_category in sales_by_category:
            sales_by_category[sale_category] += sale.price
        else:
            sales_by_category[sale_category] = sale.price

        if sale.city in sales_by_city:
            sales_by_city[sale.city] += sale.price
        else:
            sales_by_city[sale.city] = sale.price

        sale_date = sale.sell_datetime.strftime("%Y-%m-%d %H:00")
        if sale_date in sales_by_datetime:
            sales_by_datetime[sale_date] += sale.price
        else:
            sales_by_datetime[sale_date] = sale.price

    sorted_products_by_category = sorted(sales_by_category.items(), key=operator.itemgetter(1), reverse=True)
    print("Сума на продажби по категории (top 5)")
    print("-----------------------------")
    print_top_five(sorted_products_by_category)

    sorted_products_by_city = sorted(sales_by_city.items(), key=operator.itemgetter(1), reverse=True)
    print("Сума на продажби по градове (top 5)")
    print("-----------------------------")
    print_top_five(sorted_products_by_city)

    sorted_products_by_datetime = sorted(sales_by_datetime.items(), key=operator.itemgetter(1), reverse=True)
    print("Часове с най-голяма сума продажби (top 5)")
    print("-----------------------------")
    print_top_five(sorted_products_by_datetime)


def print_top_five(elements):
    max_price = elements[0][1]
    for key, value in elements[:5]:
        print("\t{} : ".format(key) + "*" * int(30 / (max_price / value)) + " {:.2f} €".format(value))


def load_product_catalog(file):
    if os.access(file, os.R_OK) and os.path.isfile(file):
        products = {}
        with open(file) as f:
            lines = csv.reader(f, dialect='excel')
            for line in lines:
                id = line[0]
                product = Product(*line)
                products[id] = product

        return products
    else:
        raise ValueError("Inaccessible file '{}'".format(file))


def load_sells(file):
    if os.access(file, os.R_OK) and os.path.isfile(file):
        sales = []
        with open(file) as f:
            lines = csv.reader(f, dialect='excel')
            for line in lines:
                sale = Sale(*line)
                sales.append(sale)

        return sales
    else:
        raise ValueError("Inaccessible file '{}'".format(file))


if __name__ == "__main__":
    sys.exit(main())

