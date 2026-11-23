import turtle

turtle.teleport(-250, 0)
squares = 0

while squares < 5:
    sides = 0

    while sides < 4:
        turtle.forward(60)
        turtle.left(90)
        sides += 1

    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    squares += 1

turtle.done()
