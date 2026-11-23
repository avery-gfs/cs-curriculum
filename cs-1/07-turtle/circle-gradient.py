import turtle

turtle.shape("turtle")

turtle.speed(40)
turtle.pensize(2)

r = 0
shapes = 0

while shapes < 36:
    turtle.pencolor((r, 0, 1))
    turtle.circle(40)
    turtle.right(10)

    r += 1 / 36
    shapes += 1

turtle.hideturtle()
turtle.done()
