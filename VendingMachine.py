import stockpile

choice = input("What would you like? Type: espresso/latte/cappuccino ")


def resume():
    global choice
    choice = input("What would you like? Type: espresso/latte/cappuccino ")


def espresso():
    if stockpile.resources["water"] < stockpile.beverages["espresso"]["ingredients"]["water"] or stockpile.resources["coffee"] < stockpile.beverages["espresso"]["ingredients"]["coffee"]:
        print("Sorry, there is not enough ingredients. The machine needs maintenance")
    else:
        stockpile.resources["water"] -= stockpile.beverages["espresso"]["ingredients"]["water"]
        stockpile.resources["coffee"] -= stockpile.beverages["espresso"]["ingredients"]["coffee"]
        print("Here's your espresso")


def latte():
    if stockpile.resources["water"] < stockpile.beverages["latte"]["ingredients"]["water"] or stockpile.resources["coffee"] < stockpile.beverages["latte"]["ingredients"]["coffee"] or stockpile.resources["milk"] < stockpile.beverages["latte"]["ingredients"]["milk"]:
        print("Sorry, there is not enough ingredients. The machine needs maintenance")
    else:
        stockpile.resources["water"] -= stockpile.beverages["latte"]["ingredients"]["water"]
        stockpile.resources["coffee"] -= stockpile.beverages["latte"]["ingredients"]["coffee"]
        stockpile.resources["milk"] -= stockpile.beverages["latte"]["ingredients"]["milk"]
        print("Here's your latte")


def cappuccino():
    if stockpile.resources["water"] < stockpile.beverages["cappuccino"]["ingredients"]["water"] or stockpile.resources["coffee"] < stockpile.beverages["cappuccino"]["ingredients"]["coffee"] or stockpile.resources["milk"] < stockpile.beverages["cappuccino"]["ingredients"]["milk"]:
        print("Sorry, there is not enough ingredients. The machine needs maintenance")
    else:
        stockpile.resources["water"] -= stockpile.beverages["cappuccino"]["ingredients"]["water"]
        stockpile.resources["coffee"] -= stockpile.beverages["cappuccino"]["ingredients"]["coffee"]
        stockpile.resources["milk"] -= stockpile.beverages["cappuccino"]["ingredients"]["milk"]
        print("Here's your cappuccino")


while True:
    if choice == "off":
        print("The machine has been turned off")
        print(f"Current stock is: {stockpile.resources}")
        break
    elif choice == "espresso":
        espresso()
        resume()
    elif choice == "latte":
        latte()
        resume()
    elif choice == "cappuccino":
        cappuccino()
        resume()
