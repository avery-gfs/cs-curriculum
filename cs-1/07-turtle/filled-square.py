import turtle

turtle.shape("turtle")

turtle.fillcolor("orange")
turtle.begin_fill()

sides = 0

while sides < 4:
    turtle.forward(100)
    turtle.left(90)
    sides += 1

turtle.end_fill()

turtle.hideturtle()
turtle.done()
