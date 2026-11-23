import turtle

sides = 7
count = 0

while count < sides:
    turtle.forward(80)
    turtle.left(360 / sides)
    count += 1

turtle.done()
