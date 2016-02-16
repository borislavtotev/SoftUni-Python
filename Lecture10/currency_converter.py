import requests

currency = input("Въведете валута: ")
amount = input("Въведете сума: ")

try:
    amount = float(amount)
    if currency == "BGN":
        print("Равностойност в BGN: {:.2f}".format(amount))
    else:
        response = requests.get("http://api.fixer.io/latest", timeout=30, params={'symbols': 'BGN', 'base': currency})
        if 'error' in response:
            print("Невалидна валута!")
        else:
            course_json = response.json()
            course = course_json['rates']['BGN']
            print("Равностойност в BGN: {:.2f}".format(amount * course))
except FloatingPointError:
    print("Невалидна сума:")
except:
    print("Неочаквана грешка!")

