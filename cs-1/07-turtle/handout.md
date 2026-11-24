# Python Turtle API

## Starter Code

```py
import turtle

turtle.shape("turtle")  # Set cursor shape to turtle

# Your code goes here

turtle.done()
```

## Functions

### `turtle.forward(n)`

`turtle.forward(100)`

Move forward `n` pixels

### `turtle.backward(n)`

`turtle.backward(50)`

Move backward `n` pixels

### `turtle.right(angle)`

`turtle.right(90)`

Turn right by `angle` degrees

### `turtle.left(angle)`

`turtle.left(45)`

Turn left by `angle` degrees

### `turtle.circle(radius)`

`turtle.circle(50)`

Draw a circle

### `turtle.circle(radius, angle)`

`turtle.circle(50, 180)`

Draw an arc covering `angle` degrees of a circle

### `turtle.setheading(angle)`

`turtle.setheading(90)`

Face a direction (`0` east, `90` north, `180` west, `270` south)

### `turtle.home()`

`turtle.home()`

Move to the center `(0, 0)`, facing east

### `turtle.teleport(x, y)`

`turtle.teleport(-100, 50)`

Jump to `(x, y)` without drawing

### `turtle.goto(x, y)`

`turtle.goto(10, 90)`

Move to `(x, y)`, drawing a line on the way

### `turtle.penup()`

`turtle.penup()`

Stop drawing when moving

### `turtle.pendown()`

`turtle.pendown()`

Start drawing when moving

### `turtle.pensize(width)`

`turtle.pensize(5)`

Set line thickness

### `turtle.pencolor(color)`

`turtle.pencolor("red")`

Set line color

### `turtle.fillcolor(color)`

`turtle.fillcolor("yellow")`

Set fill color

### `turtle.begin_fill()`

`turtle.begin_fill()`

Start a shape to fill

### `turtle.end_fill()`

`turtle.end_fill()`

Fill the shape drawn since `begin_fill()`

### `turtle.speed(n)`

`turtle.speed(0)`

Set speed (`1` slowest, `10` fast, `0` instant)

### `turtle.bgcolor(color)`

`turtle.bgcolor("black")`

Set background color

### `turtle.hideturtle()`

`turtle.hideturtle()`

Hide the turtle (handy right before `turtle.done()`)

### `turtle.reset()`

`turtle.reset()`

Clear the drawing and send the turtle home

### `turtle.done()`

`turtle.done()`

Keep the window open (last line)
