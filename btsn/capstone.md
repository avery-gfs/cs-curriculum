# CS Capstone

Software Engineering Lab

Avery Nortonsmith

anortonsmith@germantownfriends.org

## Why Study CS?

Because it teaches us how to solve complex problems. There are many tasks we as
humans are able to solve intuitively, while still struggling to describe our
solutions formally. Computer science gives us tools to be precise about our
approaches to problem solving, and thus expand our ability to tackle complexity.

Because our lives are heavily shaped by technology. Ideally, technology should
be something that empowers us as individuals, rather than something that
controls us. Learning how software works, how it is created, and how to change
it allows us maintain our agency in a software driven world, where decisions
about software are decisions about the world we are creating.

## Structure

- Short lessons on advanced topics
- Large scale, student-designed projects
- Practice using real-world software development practices
- Emphasis on technical presentation

## Topics

- Version control
- Technical writing
- Testing and collaboration
- Databases
- Large language models
- Networking
- Public speaking and presentation
- Serialization
- Regular Expressions
- APIs

## Sample Project

```py
from simple_graphics import *

# Create shapes
rect = Rect(50, 50, 100, 100, color="blue")
circle = Circle(200, 200, radius=50, color="red")

# Define event handlers
@on_click(rect)
def on_rect_click():
    print("Rectangle clicked!")

@on_press("space")
def on_space_press():
    print("Space pressed!")

# Run the window
run(width=400, height=400, caption="My Graphics App")
```
