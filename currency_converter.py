import requests
import json

# Importing API for security. (You can get your own API from https://exchangeratesapi.io)
# Go to READ ME for detailed information.

from api import access_key

# Listing our currencies.
currencies = ["USD", "AUD", "CAD", "PLN", "MXN", "TRY", "JPY"]

# Getting current currency information from exchangeratesapi.io.

link = requests.get(access_key)

# Changing JSON data to dictionary. 

link = json.loads(link.text)


def currency_calc():
    
    # Getting the desired currency. (And making sure that we have that currency in our list.)

    currency = str(input("Enter the currency you want to convert: "))
    if currency not in currencies:
        quit("Enter valid currency.")
    
    # Getting the amount of money user wants to convert.

    money = input("Enter the amount of money you want to convert: ")

    # Making sure he enters numbers.

    try:
        int(money)
    except:
        ValueError("Enter valid value.")
    
    # Calculating intended money.

    multiplier = link["rates"] [currency]
    multiplier = float(multiplier)

    # Printing out the informations.

    new_money = int(money) * multiplier
    print(f"{money} EUR = {new_money} {currency}")

currency_calc()