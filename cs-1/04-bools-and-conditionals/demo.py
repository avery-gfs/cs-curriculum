import os
import subprocess


def get_choice(count):
    while True:
        try:
            choice = int(input("\nEnter choice: "))

            if choice >= 1 and choice <= count:
                command = "cls" if os.name == "nt" else "clear"
                subprocess.run(command, shell=True)
                return choice

        except (ValueError, TypeError):
            pass

        print("Invalid choice")


print("You are at school on a pleasant Thursday morning")
print("You find yourself in Quaker meeting")
print("You feel very tired, but you CANNOT go to sleep")
print("You have the urge to speak")
print()
print("Choices:")
print()
print("1) Tell a story")
print("2) Sing a song")
print("3) Make a speech ")

choice = get_choice(3)

if choice == 1:
    print(
        "You decide to tell a story about the time you on vacation in France, and you were feeling really sick,"
    )
    print(
        "and you went to an art museum and you accidentally threw up on the Mona Lisa."
    )
    print(
        "Luckily there was glass in front of the painting so it didn’t get messed up."
    )
    print(
        "The French government was upset with you but they gave you some free healthcare and sent you on your way."
    )
    print()
    print(
        "You realize halfway through that your story doesn’t really have a connection to Quaker values."
    )
    print()
    print("GAME OVER")

if choice == 2:
    print(
        "You decide to tell a story about the time you on vacation in France, and you were feeling really sick,"
    )
    print(
        "and you went to an art museum and you accidentally threw up on the Mona Lisa."
    )
    print(
        "Luckily there was glass in front of the painting so it didn’t get messed up."
    )
    print(
        "The French government was upset with you but they gave you some free healthcare and sent you on your way."
    )
    print()
    print(
        "You realize halfway through that your story doesn’t really have a connection to Quaker values."
    )
    print()
    print("GAME OVER")
