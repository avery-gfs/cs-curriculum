import turtle

turtle.pensize(4)
sides = 0

while sides < 6:
    if sides % 2 == 0:
        turtle.pencolor("red")
    else:
        turtle.pencolor("blue")

    turtle.forward(100)
    turtle.left(60)
    sides += 1

turtle.done()
