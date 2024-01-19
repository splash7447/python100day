from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

keep_service = True

while keep_service:
    choice = menu.get_items()
    guest_order = input(f"What would you like? ({choice}): ")
    if guest_order == "off":
        keep_service = False
    elif guest_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(guest_order)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
