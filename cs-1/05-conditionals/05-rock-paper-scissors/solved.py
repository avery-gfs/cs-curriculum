import random

move = input("Enter a move (rock, paper, or scissors): ")

computerMove = random.choice(["rock", "paper", "scissors"])

print(f"Computer's move: {computerMove}")

# Print "You win!", "You lose!" or "You tie!" for a rock-paper-scissors
# game depending on the user's input and the computer's random move

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
