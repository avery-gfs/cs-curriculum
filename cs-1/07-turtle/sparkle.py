import turtle

sides = 0
turtle.backward(40)

while sides < 12:
    turtle.forward(40)
    turtle.left(110)
    turtle.forward(40)
    turtle.right(140)
    sides += 1

turtle.done()
