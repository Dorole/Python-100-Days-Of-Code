class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        """Prints a report of all resources."""
        units = {
            'water': 'ml',
            'milk': 'ml',
            'coffee': 'g'
        }

        for resource in self.resources:
            value = self.resources[resource]
            print(f"{resource.capitalize()}: {value} {units[resource]}")

    def has_resources(self, order):
        """Returns True if order can be made.
        'order' param expects a MenuItem"""
        for ingredient in order.ingredients:
            if order.ingredients[ingredient] > self.resources[ingredient]:
                print(f"\nNot enough {ingredient} in the machine.")
                return False
        return True

    def make_coffee(self, order):
        """Deducts required ingredients from the resources.
        'order' param expects a MenuItem."""
        for ingredient in order.ingredients:
            self.resources[ingredient] -= order.ingredients[ingredient]
        print(f"\nHere's your {order.name}! Enjoy! ☕")
