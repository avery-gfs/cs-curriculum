age = float(input("Enter age: "))

# Print "Youth discount" for users aged below 18.
# Print "Senior discount" for users aged 65 or above.
# Print "No discount" for all other users.

if age < 18:
    print("Youth discount")

elif age >= 65:
    print("Senior discount")

else:
    print("No discount")
