import turtle

turtle.teleport(-200, 0)
steps = 0

while steps < 20:
    if steps % 2 == 0:
        turtle.pendown()
    else:
        turtle.penup()

    turtle.forward(20)
    steps += 1

turtle.done()
