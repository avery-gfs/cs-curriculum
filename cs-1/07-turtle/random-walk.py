import turtle
import random

turtle.shape("turtle")

turtle.speed(0)
steps = 0

while steps < 300:
    heading = random.choice([0, 90, 180, 270])
    turtle.setheading(heading)
    turtle.forward(15)
    steps += 1

turtle.hideturtle()
turtle.done()
