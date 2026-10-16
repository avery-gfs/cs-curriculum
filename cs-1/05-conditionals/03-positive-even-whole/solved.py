n = float(input("Enter a number: "))

# Print "Positive" if `n` greater than or equal to 0.
# Print "Even" if `n` is even.
# Print "Whole" if `n` is a whole number.
#
# For numbers that satisfy multiple conditions, print all relavant messages

if n >= 0:
    print("Positive")

if n % 2 == 0:
    print("Even")

if round(n) == n:
    print("Whole")
