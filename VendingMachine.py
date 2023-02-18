import stockpile

choice = input("What would you like? Type: espresso/latte/cappuccino ")


def espresso():
    stockpile.resources["water"] -= stockpile.beverages["espresso"]["ingredients"]["water"]
    stockpile.resources["coffee"] -= stockpile.beverages["espresso"]["ingredients"]["coffee"]
    print("Here's your espresso")


def latte():
    stockpile.resources["water"] -= stockpile.beverages["latte"]["ingredients"]["water"]
    stockpile.resources["coffee"] -= stockpile.beverages["latte"]["ingredients"]["coffee"]
    stockpile.resources["milk"] -= stockpile.beverages["latte"]["ingredients"]["milk"]
    print("Here's your latte")


def cappuccino():
    stockpile.resources["water"] -= stockpile.beverages["cappuccino"]["ingredients"]["water"]
    stockpile.resources["coffee"] -= stockpile.beverages["cappuccino"]["ingredients"]["coffee"]
    stockpile.resources["milk"] -= stockpile.beverages["cappuccino"]["ingredients"]["milk"]
    print("Here's your cappuccino")


while True:
    if choice == "off":
        print("The machine has been turned off")
        print(stockpile.resources)
        break
    elif choice == "espresso":
        espresso()
        print(stockpile.resources)
        break
    elif choice == "latte":
        latte()
        print(stockpile.resources)
        break
    elif choice == "cappuccino":
        cappuccino()
        print(stockpile.resources)
        break
