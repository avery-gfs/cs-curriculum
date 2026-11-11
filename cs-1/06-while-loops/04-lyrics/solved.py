# Print the lyrics to "99 Bottles of Beer". Use "bottle" instead of "bottles"
# when there is only 1 left.
#
# Example:
#
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.
#
# 98 bottles of beer on the wall, 98 bottles of beer.
# Take one down, pass it around, 97 bottles of beer on the wall.
#
# ...
#
# 2 bottles of beer on the wall, 2 bottles of beer.
# Take one down, pass it around, 1 bottle of beer on the wall.
#
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down, pass it around, 0 bottles of beer on the wall.

bottles = 99

while bottles > 0:
    if bottles == 1:
        before = "1 bottle"
    else:
        before = f"{bottles} bottles"

    bottles -= 1

    if bottles == 1:
        after = "1 bottle"
    else:
        after = f"{bottles} bottles"

    print(f"{before} of beer on the wall, {before} of beer.")
    print(f"Take one down, pass it around, {after} of beer on the wall.")
    print()
