import turtle

turtle.shape("turtle")
turtle.speed(0)


def edge(size):
    if size <= 8:
        turtle.forward(size)
    else:
        edge(size / 3)
        turtle.left(60)
        edge(size / 3)
        turtle.right(120)
        edge(size / 3)
        turtle.left(60)
        edge(size / 3)


turtle.teleport(-128, 64)
edge(256)
turtle.right(120)
edge(256)
turtle.right(120)
edge(256)

turtle.hideturtle()
turtle.done()
