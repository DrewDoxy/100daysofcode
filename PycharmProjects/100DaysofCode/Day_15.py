MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def create_report():
    """Prints a report to display the resources left in the machine"""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")


def check_payment():
    """Returns the total amount of money from the coins the user inputted."""
    total = int(input("How many pennies? ")) * 0.01
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many quarters? ")) * 0.25
    total += float(total)
    resources["money"] = total
    return total


def check_resources(order_ingredients):
    """Checks that resources are sufficient against the recipe and tells the user if there aren't enough."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def transaction_check(money_received, drink_cost):
    """Return true if transaction is successful, return False if not."""
    if money_received < drink_cost:
        print("You're too poor to afford this drink.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here's your change: ${change}")
        global profit
        profit += drink_cost
        return True


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


def main_loop():
    is_on = True
    while is_on:
        selection = input("What would you like? (espresso/latte/cappuccino) ").lower()
        if selection == "off":
            is_on = False
            break
        elif selection == "report":
            create_report()
            main_loop()
        else:
            drink = MENU[selection]
            if check_resources(drink['ingredients']):
                payment = check_payment()
                if transaction_check(payment, drink["cost"]):
                    make_coffee(selection, drink['ingredients'])
        more_coffee = input("Would you like to purchase a drink? Y/N ").lower()
        if more_coffee == "y":
            is_on = True
        else:
            is_on = False


main_loop()
