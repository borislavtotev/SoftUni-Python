import iso8601
from datetime import datetime, timezone


class Sale:
    def __init__(self, product_id, country, city, sell_datetime, price):
        self.product_id = product_id
        self.country = country
        self.city = city
        self.sell_datetime = iso8601.parse_date(sell_datetime)
        self.sell_datetime = self.sell_datetime.astimezone(timezone.utc)
        self.price = float(price)
