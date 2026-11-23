import turtle

sides = 0
turtle.speed(40)
turtle.backward(100)

while sides < 24:
    turtle.forward(200)
    turtle.right(165)
    sides += 1

turtle.done()
