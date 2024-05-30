from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    machine_on = True

    items = Menu()
    maker = CoffeeMaker()
    cost = MoneyMachine()

    while machine_on:
        choice = input(f"What would you like? ({items.get_items()}): ").lower()

        if choice == "off":
            machine_on = False
        elif choice == "report":
            maker.report()
            cost.report()
        else:
            drink = items.find_drink(choice)  # MenuItem object
            if drink and maker.is_resource_sufficient(drink) and cost.make_payment(drink.cost):
                maker.make_coffee(drink)


if __name__ == "__main__":
    main()
