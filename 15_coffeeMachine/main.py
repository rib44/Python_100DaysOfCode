import sys

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


money = 0


def check_ingredients(drink):
    """Returns
        true: drink can be made
        false: drink cannot be made
    """

    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}.")
            return False  # drink cannot be made

    return True  # drink can be made


def get_cash():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    cash_in = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    return cash_in


def check_transaction(cash_out):
    if cash_out < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


def deduct_resources(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]


def report(money):
    pass
    # TODO: print the report
    for ingredient in resources:
        print(f"{ingredient}: {resources[ingredient]}")
    print(f"Money: {money}")


def main():
    global money

    # TODO: 1. get user input: espresso/latte/cappuccino and off/report
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # menu of options for the coffee machine
    if choice == "off":
        sys.exit(1)
    elif choice == "report":
        report(money)
    else:
        # TODO: 2. check if there are sufficient resources, else return
        enough_ingredients = check_ingredients(choice)
        if not enough_ingredients:
            return

        # TODO: 3. process coins, find money inserted
        cash_in = get_cash()  # asks user for money
        cost = MENU[choice]["cost"]
        cash_out = cash_in - cost

        # TODO: 4. check transaction success:
        #   success: add money to profit, deduct the needed resources, return the change if change != 0 (2 decimal)
        #   failure: print-> money refunded
        enough_cash = check_transaction(cash_out)

        # failure
        if not enough_cash:
            return

        # success
        money += cost
        deduct_resources(choice)
        print(f"Here is ${cash_out:.2f} in change.")

        # TODO: 5. print the final message while serving it
        print(f"Here is your {choice} ☕. Enjoy!")


if __name__ == "__main__":
    while True:
        main()

