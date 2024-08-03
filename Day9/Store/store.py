# store.py

class ShoppingCart:

    def __init__(self):
        self.items = {}
        self.total = 0

    def add_item(self, item, price):
        self.items[item] = price
        self.total += price

    def apply_discount(self, code):
        if code == 'DISCOUNT10':
            self.total *= 0.9

cart=ShoppingCart()

print(cart.items)
cart.add_item('tool box',29.99)
print(cart.items)
cart.apply_discount('DISCOUNT10')
print(cart.total)
