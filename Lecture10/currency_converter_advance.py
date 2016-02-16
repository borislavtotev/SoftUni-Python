from datetime import datetime
import requests

currency_date_str = input("Въведете дата: ")
currency = input("Въведете валута: ")
amount = input("Въведете сума: ")
new_currency = input("Въведете валута, към която да се конвертира: ")

try:
    amount = float(amount)
    try:
        currency_date = datetime.strptime(currency_date_str, "%Y-%M-%d")
        if currency == "BGN":
            print("Равностойност в BGN: {:.2f}".format(amount))
        else:
            response = requests.get("http://api.fixer.io/latest", timeout=30, params={
                'symbols': new_currency,
                'base': currency,
                'date': currency_date_str})
            if 'error' in response:
                print("Невалидна валута!")
            else:
                course_json = response.json()
                course = course_json['rates'][new_currency]
                print("Равностойност в {}: {:.2f}".format(new_currency, amount * course))
    except ValueError:
        print("Невалиден формат на датата")

except FloatingPointError:
    print("Невалидна сума:")
except:
    print("Неочаквана грешка!")

