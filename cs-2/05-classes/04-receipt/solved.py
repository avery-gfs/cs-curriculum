def test(result, expected):
    if result != expected:
        print("!!!!! Fail !!!!!\n")

    else:
        print("----- PASS: -----\n")

    print(result)
    print()


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"{self.name} ${self.total():.2f} ({self.quantity} x ${self.price:.2f})"


class Receipt:
    def __init__(self):
        self.items = []

    def addItem(self, name, price, quantity):
        self.items.append(Item(name, price, quantity))

    def updateQuantity(self, name, newQuantity):
        for item in self.items:
            if item.name == name:
                item.quantity = newQuantity

    def removeitem(self, name):
        newItems = []

        for item in self.items:
            if item.name != name:
                newItems.append(item)

        self.items = newItems

    def total(self):
        totalCost = 0

        for item in self.items:
            totalCost += item.total()

        return totalCost

    def __repr__(self):
        itemRows = ""

        for item in self.items:
            itemRows += f"{item}\n"

        return f"{itemRows}----------\ntotal: ${self.total():.2f}"


b = Item("bagel", 2.5, 2)

test(b.name, "bagel")
test(b.price, 2.5)
test(b.quantity, 2)
test(b.total(), 5)
test(str(b), "bagel $5.00 (2 x $2.50)")

c = Item("coffee", 3, 1)

test(str(c), "coffee $3.00 (1 x $3.00)")

receipt = Receipt()

receipt.addItem("juice", 5, 3)
receipt.addItem("salad", 10, 3)
receipt.addItem("brownie", 4, 1)

test(receipt.total(), 49)

test(
    str(receipt),
    """
juice $15.00 (3 x $5.00)
salad $30.00 (3 x $10.00)
brownie $4.00 (1 x $4.00)
----------
total: $49.00
""".strip(),
)

receipt.updateQuantity("brownie", 2)
receipt.removeitem("juice")
receipt.addItem("yogurt", 2, 1)

test(receipt.total(), 40)

test(
    str(receipt),
    """
salad $30.00 (3 x $10.00)
brownie $8.00 (2 x $4.00)
yogurt $2.00 (1 x $2.00)
----------
total: $40.00
""".strip(),
)
