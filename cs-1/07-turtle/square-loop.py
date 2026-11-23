import turtle

turtle.shape("turtle")

turtle.pencolor("purple")

sides = 0

while sides < 4:
    turtle.forward(100)
    turtle.left(90)
    sides += 1

turtle.hideturtle()
turtle.done()
