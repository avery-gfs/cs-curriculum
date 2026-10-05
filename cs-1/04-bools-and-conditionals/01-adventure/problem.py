intro = """
You are at school on a pleasant Thursday morning.
You find yourself in Quaker meeting.
You feel very tired, but you CANNOT go to sleep.
You have the urge to speak.

Choices:

Tell a story (story)
Sing a song (song)
Make a speech (speech) 
"""

story = """
You decide to tell a story about the time you on vacation in France, and you
were feeling really sick, and you went to an art museum and you accidentally
threw up on the Mona Lisa. Luckily there was glass in front of the painting
so it didn't get messed up. The French government was upset with you but they
gave you some free healthcare and sent you on your way.

You realize halfway through that your story doesn't really have a connection
to Quaker worship. The meeting begins to boo your message.

GAME OVER
"""

speech = """
You speak about the importance of tik tok content for the minds of teenagers.
About the cruelty of depriving students of a constant stream of inane videos.
The meeting is moved by your argument, and gives you a standing ovation. You
set your sights towards bigger goals.

Choices:

Join the debate team (debate)
Star in the school play (play)
"""

debate = """
You join the debate team. It's surprisingly fun! After a week of intensive
prep, you head to Harvard for the national speech and debate tournament.
"""

play = """
You join the school play. It's The Wizard of Oz. You get cast as the leading
role. After two months of rehearsal, you're ready to perform. But you realize
you can't remember how your character's name is spelled!

Choices

Dorthy (dorthy)
Dorothy (dorothy)
"""

song = """
You decide to sing the song "Single Ladies" by Beyonce

You do your best rendition of the song, (along with the dance)

The rest of the meeting sits in shocked silence

You see Behnaz get up and walk towards you

Choices:

Run (run)
Hide (hide)
"""

run = """
You dash out of the meetinghouse, run into the cafeteria, up the stairs and
onto the indoor track. Behnaz is chasing you. You both do laps around the
track, with Behnaz slowly gaining on you. After 20 laps, your legs give out,
and Behnaz is upon you.

GAME OVER
"""

hide = """
You dash out of the meetinghouse and into a nearby shrub. It's warm in the
shrub, and you feel safe. Drift into a peaceful sleep.

When you awake, it's night. Campus is deserted.

Choices:

Walk to center city (walk)
Watch a movie in Yarnall (movie)
"""

print(intro)
choice = input("Enter choice: ")

if choice == "story":
    print(story)

elif choice == "song":
    print(song)
    choice = input("Enter choice: ")

    if choice == "run":
        print(run)

    else:
        print(hide)

else:
    print(speech)
    choice = input("Enter choice: ")

    if choice == "debate":
        print(debate)

    else:
        print(play)
