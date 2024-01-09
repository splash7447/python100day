from memu import MENU


income = 0
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resource(order):
    for item in order:
        if order[item] > resource[item]:
            print(f"Sorry there is not enough{item}")
            return False
    return True


def print_resource():
    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}g")


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


def trade(money, drink_price):
    if money > drink_price:
        change = round(money - drink_price, 2)
        print(f"Here is ${change} in change.")
        global income
        income += drink_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def drink_make(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resource[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


keep_service = True


while keep_service:
    guest_order = input("What would you like? (espresso/latte/cappuccino): ")
    if guest_order == "off":
        keep_service = False
    elif guest_order == "report":
        print_resource()
    else:
        drink = MENU[guest_order]
        if check_resource(drink["ingredients"]):
            payment = process_coins()
            if trade(payment, drink["cost"]):
                drink_make(guest_order, drink["ingredients"])