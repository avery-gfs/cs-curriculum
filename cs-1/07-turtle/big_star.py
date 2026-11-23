import turtle

sides = 0
turtle.speed(40)
turtle.backward(100)

while sides < 72:
    turtle.forward(200)
    turtle.right(170)
    sides += 1

turtle.done()
