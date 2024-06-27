import menu

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

OFF_KEY = "off"
REPORT_KEY = "report"


def get_user_choice():
    user_choice = input("\nWhat would you like? ").lower()
    while user_choice not in menu.MENU.keys() and user_choice not in [OFF_KEY, REPORT_KEY]:
        user_choice = input("\nInvalid choice. What would you like? ").lower()

    return user_choice


def has_resources(drink):
    recipe_ingredients = menu.MENU[drink]["ingredients"]
    for ingredient in recipe_ingredients:
        if recipe_ingredients[ingredient] > resources[ingredient]:
            print(f"\nNot enough {ingredient} in the machine.")
            return False
    return True


def receive_coins(price):
    total = 0

    while total < price:
        print("\nInsert coins.")
        total += int(input("How many quarters: ")) * 0.25
        total += int(input("How many dimes: ")) * 0.1
        total += int(input("How many nickles: ")) * 0.05
        total += int(input("How many pennies: ")) * 0.01

        if total < price:
            if input(f"\nYou have inserted ${round(total, 2)} out of ${price}. Insert more? (Y/N) ").lower() == "y":
                continue
            else:
                break

    return round(total, 2)


def calculate_change(money_received, price):
    return money_received - price


def process_payment(drink):
    price = menu.get_price(drink)
    money_received = receive_coins(price)

    if money_received > price:
        change = calculate_change(money_received, price)
        print(f"\nYou paid ${money_received}. Returning change: ${change}")
        return money_received - change
    elif price > money_received:
        print(f"\nNot enough money paid. Returning ${money_received}")
        return 0
    else:
        # print(f"\nThank you for your payment of ${money_received}")
        return money_received


def make_coffee(drink):
    recipe_ingredients = menu.MENU[drink]["ingredients"]
    for ingredient in recipe_ingredients:
        resources[ingredient] -= recipe_ingredients[ingredient]


def print_report(money):
    print("\nMACHINE REPORT:")

    units = {
        'water': 'ml',
        'milk': 'ml',
        'coffee': 'g'
    }

    for ingredient in resources:
        print(f"{ingredient.capitalize()}: {resources[ingredient]} {units[ingredient]}")

    print(f"Money: ${money}")


def prompt_for_rerun():
    if input("\nWould you like another coffee? (Y/N) ").lower() == "y":
        return True
    else:
        print("\nGoodbye!")
        return False


def run_machine():
    is_on = True
    money_in_machine = 0

    print("PY COFFEE MACHINE MENU:\n")
    menu.print_menu()

    while is_on:
        choice = get_user_choice()

        if choice == OFF_KEY:
            print("\nSwitching off. Bye!")
            is_on = False
        elif choice == REPORT_KEY:
            print_report(money_in_machine)
        else:
            if has_resources(choice):
                payment = round(process_payment(choice), 2)
                if payment != 0:
                    money_in_machine += payment
                    make_coffee(choice)
                    print(f"\nHere's your {choice}! Enjoy! ☕")
                    if not prompt_for_rerun():
                        break
                else:
                    print("\nGoodbye!")
                    break
            else:
                print(f"Cannot make {choice}.")
                if not prompt_for_rerun():
                    break

