# Template
#
# When operating a used car, remember: never <verb> the engine if the car is <adjective>.
# Before driving, make sure the gas tank is free of <plural noun>.
# Used cars perform best when driven between <number> and <number> miles per hour.
# Always keep a large supply of <substance> in your car for passengers to enjoy.
#
# Inputs
#
# verb: cook
# adjective: spicy
# plural noun: frogs
# number: 2
# number: 200
# substance: rice pudding
#
# Result
#
# When operating a used car, remember: never cook the engine if the car is spicy.
# Before driving, make sure the gas tank is free of frogs.
# Used cars perform best when driven between 2 and 200 miles per hour.
# Always keep a large supply of rice pudding in your car for passengers to enjoy.

verb = input("verb: ")
adj = input("adjective: ")
plur = input("plural noun: ")
num1 = input("number: ")
num2 = input("number: ")
sub = input("substance: ")

print(
    f"When operating a used car, remember: never {verb} the engine if the car is {adj}."
)
print(f"Before driving, make sure the gas tank is free of {plur}.")
print(f"Used cars perform best when driven between {num1} and {num2} miles per hour.")
print(f"Always keep a large supply of {sub} in your car for passengers to enjoy.")
