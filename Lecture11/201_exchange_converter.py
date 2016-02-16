exchange_file = input()
amount_file = input()

exchange_rates = {}
with open(exchange_file, encoding='utf-8') as ef:
    for line in ef:
        if line.strip():
            line_elements = line.split()
            exchange_rates[line_elements[0]] = line_elements[1]

with open(amount_file, encoding='utf-8') as af:
    for line in af:
        if line.strip():
            line_elements = line.split()
            currency = line_elements[1]
            amount_in_bgn = float(line_elements[0]) / float(exchange_rates[currency])
            print('{:.2f}'.format(amount_in_bgn))

