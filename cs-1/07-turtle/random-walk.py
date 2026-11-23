import turtle
import random

turtle.shape("turtle")
turtle.speed(0)

steps = 0

while steps < 300:
    heading = random.randint(0, 360)
    turtle.setheading(heading)

    color = random.choice([
        "purple",
        "green",
        "red",
        "blue",
        "orange",
    ])

    turtle.pencolor(color)

    turtle.forward(15)
    steps += 1

turtle.hideturtle()
turtle.done()
