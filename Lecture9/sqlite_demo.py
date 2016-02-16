import sys
import os
import csv
import sqlite3

from product import Product
from sale import Sale

def main():
    product_catalog = load_product_catalog('./catalog.csv')
    sales = load_sells('./sales-example.csv')

    print(product_catalog)
    print(sales)

    db_filname = "sales-example.db"

    with sqlite3.connect(db_filname, isolation_level=None) as connection:
        create_tables(connection)
        load_catalog_into_db(product_catalog, connection)
        load_sale_into_db(sales, connection)

        city_name = input("Въведете име на град: ")
        current_city_sales = sales_by_city(city_name, connection)

        if current_city_sales:
            print(current_city_sales)
        else:
            print("Няма продажби в {}".format(city_name))


def sales_by_city(city_name, connection):
    cursor = connection.cursor()
    cursor.execute('select * from sale where city_name = ? order by sale_timestamp', [city_name])
    results = cursor.fetchall()
    return results


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        create table if not exists sale (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_key varchar(200) NOT NULL,
            country varchar(3),
            city_name varchar(60),
            sale_timestamp TEXT,
            price NUMERIC
        );
    """)

    cursor.execute("""
        create table if not exists catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_key varchar(200),
            category varchar(200)
        );
    """)


def load_catalog_into_db(product_catalog, connection):
    cursor = connection.cursor()
    for product in product_catalog.values():
        cursor.execute("insert into catalog (item_key, category) values (?, ?)", [product.id, product.category])
        print("{} inserted".format(product.category))


def load_sale_into_db(sales, connection):
    cursor = connection.cursor()
    for sale in sales:
        cursor.execute("""
            insert into sale (item_key, country, city_name, sale_timestamp, price) values(?, ?, ?, ?, ?)""",
                       [sale.product_id, sale.country, sale.city, sale.sell_datetime.isoformat(), sale.price])

        print("{} imported.".format(sale.city))


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