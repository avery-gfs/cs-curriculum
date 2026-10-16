import random

move = input("Enter a move (rock, paper, or scissors): ")

computerMove = random.choice(["rock", "paper", "scissors"])

print(f"Computer's move: {computerMove}")

# Print "You win!", "Invalid move. You lose!" or "You tie!" for a rock-paper-scissors
# game depending on the user's input and the computer's random move. Print
# "Invalid move. You lose!" for invalid user move inputs
#
# Examples:
#
# Enter a move (rock, paper, or scissors): paper
# Computer's move: rock
# You win!
#
# Enter a move (rock, paper, or scissors): rock
# Computer's move: paper
# You lose!
#
# Enter a move (rock, paper, or scissors): towel
# Computer's move: rock
# Invalid move. You lose!
