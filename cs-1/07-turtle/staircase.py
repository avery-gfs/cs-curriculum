import turtle

turtle.teleport(-150, -150)
steps = 0

while steps < 6:
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(50)
    steps += 1

turtle.done()
