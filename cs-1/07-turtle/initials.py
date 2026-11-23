import turtle

turtle.pencolor("blue")
turtle.pensize(4)

turtle.teleport(-100, 0)
turtle.left(70)
turtle.forward(100)
turtle.right(140)
turtle.forward(100)
turtle.setheading(0)
turtle.teleport(-100, 0)
turtle.left(70)
turtle.forward(50)
turtle.setheading(0)
turtle.forward(35)

turtle.penup()
turtle.goto(10, 0)
turtle.setheading(90)
turtle.pendown()
turtle.forward(100)
turtle.right(160)
turtle.forward(110)
turtle.setheading(90)
turtle.forward(100)

turtle.done()
