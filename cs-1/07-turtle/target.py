import turtle

radius = 150
rings = 0

while radius > 0:
    if rings % 2 == 0:
        turtle.fillcolor("red")
    else:
        turtle.fillcolor("white")

    turtle.teleport(0, -radius)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    radius -= 30
    rings += 1

turtle.done()
