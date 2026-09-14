import random

n = random.randrange(0, 101)

while True:
    guess = int(input("Enter a guess: "))

    if guess < n:
        print("Too low")
    elif guess > n:
        print("Too high")
    else:
        print("Correct!")
        break
