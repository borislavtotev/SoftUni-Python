prices = []

while True:
    price = input('Please add new price:')
    if price == 'stop':
        break

    prices.append(float(price))

if len(prices) < 4:
    print('You can\'t calculate avg price with less than 4 prices')

max_value = max(prices)
min_value = min(prices)

if min_value == max_value:
    print("It can't calculate the avg price, because all values are the same!")
else:
    while max_value in prices:
        prices.remove(max_value)

    while min_value in prices:
        prices.remove(min_value)

    #print(prices)

    if len(prices) > 0:
        avg_value = sum(prices) / len(prices)
        print("Max price: " + str(max_value))
        print("Min price: " + str(min_value))
        print("Average price: {0:.2f}".format(avg_value))
    else:
        print("Can\'t calculate avg price, because there are only max and min prices!")

