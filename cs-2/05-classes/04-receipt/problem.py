def test(result, expected):
    if result != expected:
        print("!!!!! Invalid result !!!!!\n")

    else:
        print("----- Ok: -----\n")

    print(result)
    print()


class Item:
    def __init__(self, name, price, quantity):
        # Save name, price, and quantity as fields on the item
        pass

    def total(self):
        # Return the cost of this item: price times quantity
        pass

    def __repr__(self):
        # Return a string like: bagel 5.00 ($2 x $2.50)
        # (name, total, then quantity and price in parentheses)
        pass


class Receipt:
    def __init__(self):
        # List of Item objects (items on the receipt)
        self.items = []

    def addItem(self, name, price, quantity):
        # Make a new Item object with the given name, price, and quantity
        # and add it to the receipt
        pass

    def updateQuantity(self, name, newQuantity):
        # Find the item with a matching name, set its quantity to newQuantity
        pass

    def removeitem(self, name):
        # Remove the item with a matching name from the receipt
        pass

    def total(self):
        # Return the total cost of every item on the receipt added together
        pass

    def __repr__(self):
        # Return one line per item, then a divider and the receipt total:
        #
        # salad 30.00 ($3 x $10.00)
        # yogurt 2.00 ($1 x $2.00)
        # ----------
        # total: $32.00
        pass


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
