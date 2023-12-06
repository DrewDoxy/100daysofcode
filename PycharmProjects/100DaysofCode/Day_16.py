from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
my_money = MoneyMachine()

coffee_maker.report()
my_money.report()


def main_loop():
    is_on = True
    while is_on:
        options = menu.get_items()
        selection = input(f"What would you like? {options} ")
        if selection == "off":
            is_on = False
        elif selection == "report":
            coffee_maker.report()
            my_money.report()
            main_loop()
        else:
            drink = menu.find_drink(selection)
            if coffee_maker.is_resource_sufficient(drink):
                if my_money.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


main_loop()
