genders = ('infant', 'kid', 'men', 'unisex', 'woman')
prices = {}

with open("./catalog_full.csv") as f:
    for line in f:
        line_elements = line.split(',')
        current_gender = line_elements[-2].lower()
        price = float(line_elements[-1])

        if current_gender in genders:
            if current_gender not in prices:
                prices[current_gender] = []
            prices[current_gender].append(price)


for gender, current_prices in prices.items():
    if len(current_prices) != 0:
        avg_price = sum(current_prices) / len(current_prices)
        print("Avg price for {} is {:.2f}".format(gender, avg_price))
