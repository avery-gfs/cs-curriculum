import random

n = random.randrange(1, 101)
guesses = 0

while True:
    guess = int(input("Enter a guess: "))
    guesses += 1

    if guess < n:
        print("Too low")
    elif guess > n:
        print("Too high")
    else:
        print("Correct!")
        print(f"Guesses: {guesses}")
        break
