from menu import Menu
from coffee_maker import CoffeeMaker
from money_processor import MoneyProcessor

menu = Menu()
coffee_maker = CoffeeMaker()
money_processor = MoneyProcessor()

OFF_KEY = "off"
REPORT_KEY = "report"


def get_user_choice():
    user_choice = ""
    while user_choice not in menu.options and user_choice not in [OFF_KEY, REPORT_KEY]:
        if user_choice != "":
            print("Please input a valid option.")
        user_choice = input(f"\nWhat would you like? ({menu.display_options()}) ").lower()
    return user_choice


def run():
    is_on = True
    menu.display_menu()

    while is_on:
        choice = get_user_choice()

        if choice == OFF_KEY:
            is_on = False
        elif choice == REPORT_KEY:
            coffee_maker.report()
            money_processor.report()
        else:
            order = menu.find_drink(choice)
            if coffee_maker.has_resources(order) and money_processor.process_payment(order.cost):
                coffee_maker.make_coffee(order)
            else:
                print("\nGoodbye!")
                break


# ------------------------------ PROGRAM ------------------------------
run()

