import turtle

turtle.shape("turtle")
turtle.pensize(3)

sides = 0
turtle.fillcolor("yellow")
turtle.begin_fill()

while sides < 4:
    turtle.left(90)
    turtle.forward(100)
    sides += 1

turtle.end_fill()

turtle.teleport(-20, 80)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.setheading(135)
turtle.circle(8)
turtle.end_fill()

turtle.teleport(-50, 50)
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.setheading(135)
turtle.circle(20)
turtle.end_fill()

turtle.teleport(10, 90)
turtle.fillcolor("pink")
turtle.begin_fill()
turtle.setheading(-90)
turtle.forward(50)
turtle.left(135)
turtle.forward(30)
turtle.goto(10, 90)
turtle.end_fill()

turtle.teleport(-10, 110)
turtle.setheading(135)
turtle.forward(40)
turtle.backward(40)
turtle.left(22.5)
turtle.forward(40)
turtle.backward(40)
turtle.left(22.5)
turtle.forward(40)
turtle.backward(40)

turtle.hideturtle()
turtle.done()
