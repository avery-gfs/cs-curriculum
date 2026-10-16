import random

move = input("Enter a move (rock, paper, or scissors): ")

# Print "Positive" if `n` greater than or equal to 0.
# Print "Even" if `n` is even.
# Print "Whole" if `n` is a whole number.
#
# For numbers that satisfy multiple conditions, print all relavant messages

computerMove = random.choice(["rock", "paper", "scissors"])

print(f"Computer's move: {computerMove}")

if move == "rock":
    if computerMove == "rock":
        print("You tie!")

    elif computerMove == "paper":
        print("You lose!")

    elif computerMove == "scissors":
        print("You win!")

elif move == "paper":
    if computerMove == "rock":
        print("You win!")

    elif computerMove == "paper":
        print("You tie!")

    elif computerMove == "scissors":
        print("You lose!")

elif move == "scissors":
    if computerMove == "rock":
        print("You lose!")

    elif computerMove == "paper":
        print("You win!")

    elif computerMove == "scissors":
        print("You tie!")

else:
    print("Invalid move")
