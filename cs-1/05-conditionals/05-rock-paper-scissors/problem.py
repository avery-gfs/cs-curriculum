import random

move = input("Enter a move (rock, paper, or scissors): ")

computerMove = random.choice(["rock", "paper", "scissors"])

print(f"Computer's move: {computerMove}")

# Print "You win!", "You lose!" or "You tie!" for a rock-paper-scissors
# game depending on the user's input and the computer's random move
