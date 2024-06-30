class MenuItem:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", cost=2.5, water=200, milk=150, coffee=24),
            MenuItem(name="espresso", cost=1.5, water=50, milk=0, coffee=18),
            MenuItem(name="cappuccino", cost=3, water=250, milk=50, coffee=24)
        ]

        self.options = self.get_items()

    def display_menu(self):
        print("\n----- PY COFFEE MACHINE MENU -----")
        for item in self.menu:
            print(f"{item.name.capitalize()}: ${item.cost}")

    def get_items(self):
        """Retrieves menu items' names."""
        names = []
        for item in self.menu:
            names.append(item.name)
        return names

    def display_options(self):
        display = ""
        for option in self.options:
            display += f"{option}/"
        return display

    def find_drink(self, drink_name):
        """Return item by name, if it exists."""
        for item in self.menu:
            if item.name == drink_name:
                return item
        print("That item is not available.")


