import turtle

turtle.shape("turtle")

sides = 0
turtle.fillcolor("blue")
turtle.begin_fill()

while sides < 3:
    turtle.forward(150)
    turtle.left(120)
    sides += 1

turtle.end_fill()

turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
