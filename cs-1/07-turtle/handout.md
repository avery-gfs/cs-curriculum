# Python Turtle API

## Starter Code

```py
import turtle

turtle.shape("turtle")

# Your code goes here

turtle.done()
```

`turtle.shape("turtle")` sets the cursor to a turtle icon. `turtle.done()` keeps
the image open once the drawing is finished.

## Functions

### `turtle.forward(n)`

Example: `turtle.forward(100)`

Move forward `n` pixels.

### `turtle.backward(n)`

Example: `turtle.backward(50)`

Move backward `n` pixels.

### `turtle.right(angle)`

Example: `turtle.right(90)`

Turn right by `angle` degrees.

### `turtle.left(angle)`

Example: `turtle.left(45)`

Turn left by `angle` degrees.

### `turtle.circle(radius)`

Example: `turtle.circle(50)`

Draw a circle to the left of the turtle. Use positive `radius` to draw
counter-clockwise, negative `radius` to draw clockwise.

### `turtle.circle(radius, angle)`

Example: `turtle.circle(50, 180)`

Draw an arc covering `angle` degrees of a circle. Use positive `radius` to draw
counter-clockwise, negative `radius` to draw clockwise.

### `turtle.setheading(angle)`

Example: `turtle.setheading(90)`

Face a direction (`0` east, `90` north, `180` west, `270` south).

### `turtle.teleport(x, y)`

Example: `turtle.teleport(-100, 50)`

Jump to `(x, y)` without drawing.

### `turtle.goto(x, y)`

Example: `turtle.goto(10, 90)`

Move to `(x, y)`, drawing a line on the way.

### `turtle.penup()`

Example: `turtle.penup()`

Stop drawing when moving.

### `turtle.pendown()`

Example: `turtle.pendown()`

Start drawing when moving.

### `turtle.pensize(width)`

Example: `turtle.pensize(5)`

Set line thickness.

### `turtle.pencolor(color)`

Example: `turtle.pencolor("red")`

Set line color.

### `turtle.fillcolor(color)`

Example: `turtle.fillcolor("yellow")`

Set fill color.

### `turtle.begin_fill()`

Example: `turtle.begin_fill()`

Start a shape to fill.

### `turtle.end_fill()`

Example: `turtle.end_fill()`

Fill the shape drawn since `begin_fill()`.

### `turtle.speed(n)`

Example: `turtle.speed(0)`

Set speed (`1` slowest, `10` fast, `0` instant).

### `turtle.bgcolor(color)`

Example: `turtle.bgcolor("black")`

Set background color.

### `turtle.hideturtle()`

Example: `turtle.hideturtle()`

Hide the turtle (handy right before `turtle.done()`).

### `turtle.reset()`

Example: `turtle.reset()`

Clear the drawing and send the turtle home.
