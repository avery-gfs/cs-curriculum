| Function                       | Meaning                                                          | Example                      |
| ------------------------------ | ---------------------------------------------------------------- | ---------------------------- |
| `turtle.shape(name)`           | Change how the turtle looks (`"turtle"`, `"arrow"`, `"circle"`)  | `turtle.shape("turtle")`     |
| `turtle.forward(n)`            | Move forward `n` pixels                                          | `turtle.forward(100)`        |
| `turtle.backward(n)`           | Move backward `n` pixels                                         | `turtle.backward(50)`        |
| `turtle.right(angle)`          | Turn right by `angle` degrees                                    | `turtle.right(90)`           |
| `turtle.left(angle)`           | Turn left by `angle` degrees                                     | `turtle.left(45)`            |
| `turtle.circle(radius)`        | Draw a circle                                                    | `turtle.circle(50)`          |
| `turtle.circle(radius, angle)` | Draw an arc covering `angle` degrees of a circle                 | `turtle.circle(50, 180)`     |
| `turtle.setheading(angle)`     | Face a direction (`0` east, `90` north, `180` west, `270` south) | `turtle.setheading(90)`      |
| `turtle.home()`                | Move to the center `(0, 0)`, facing east                         | `turtle.home()`              |
| `turtle.teleport(x, y)`        | Jump to `(x, y)` without drawing                                 | `turtle.teleport(-100, 50)`  |
| `turtle.goto(x, y)`            | Move to `(x, y)`, drawing a line on the way                      | `turtle.goto(10, 90)`        |
| `turtle.penup()`               | Stop drawing when moving                                         | `turtle.penup()`             |
| `turtle.pendown()`             | Start drawing when moving                                        | `turtle.pendown()`           |
| `turtle.pensize(width)`        | Set line thickness                                               | `turtle.pensize(5)`          |
| `turtle.pencolor(color)`       | Set line color                                                   | `turtle.pencolor("red")`     |
| `turtle.fillcolor(color)`      | Set fill color                                                   | `turtle.fillcolor("yellow")` |
| `turtle.begin_fill()`          | Start a shape to fill                                            | `turtle.begin_fill()`        |
| `turtle.end_fill()`            | Fill the shape drawn since `begin_fill()`                        | `turtle.end_fill()`          |
| `turtle.speed(n)`              | Set speed (`1` slowest, `10` fast, `0` instant)                  | `turtle.speed(0)`            |
| `turtle.bgcolor(color)`        | Set background color                                             | `turtle.bgcolor("black")`    |
| `turtle.hideturtle()`          | Hide the turtle (handy right before `turtle.done()`)             | `turtle.hideturtle()`        |
| `turtle.reset()`               | Clear the drawing and send the turtle home                       | `turtle.reset()`             |
| `turtle.done()`                | Keep the window open (last line)                                 | `turtle.done()`              |
