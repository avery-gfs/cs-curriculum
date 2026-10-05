# Write a program that calculates a final price from a given
# base cost and tax amount (percentage)
#
# Example:
#
# Enter price: 20
# Enter tax: 4
# Total: 20.8

price = float(input("Enter price: "))
tax = float(input("Enter tax: "))
total = price * (1 + tax / 100)
print(f"Total: {total}")
