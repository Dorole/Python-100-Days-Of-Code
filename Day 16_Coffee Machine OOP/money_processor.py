class MoneyProcessor:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def receive_coins(self):
        print("\nInsert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return round(self.money_received, 2)

    def calculate_change(self, cost):
        return round(self.money_received - cost, 2)

    def process_payment(self, cost):
        self.receive_coins()

        while self.money_received < cost:
            if input(f"\nYou have inserted ${round(self.money_received, 2)} out "
                     f"of ${cost}. Insert more? (Y/N) ").lower() == "y":
                self.receive_coins()
            else:
                print(f"\nNot enough money paid. Returning ${self.money_received}")
                self.money_received = 0
                break

        if self.money_received == 0:
            return False
        elif self.money_received > cost:
            change = self.calculate_change(cost)
            print(f"\nYou paid ${self.money_received}. Returning change: ${change}")

        self.profit += cost
        self.money_received = 0
        return True
