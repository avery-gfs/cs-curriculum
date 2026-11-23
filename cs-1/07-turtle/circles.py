import turtle

turtle.shape("turtle")

r = 0
turtle.speed(40)
turtle.pensize(2)
shapes = 0

while shapes < 36:
    turtle.pencolor((r, 0, 1))
    turtle.circle(40)
    turtle.right(10)

    r = (r + 0.03) % 1

    shapes += 1

turtle.hideturtle()
turtle.done()
