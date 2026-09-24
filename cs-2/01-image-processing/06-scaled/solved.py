# Scale an image to be twice as big

from PIL import Image

# Load input image
im = Image.open("bird.png")

scale = 2
scaledWidth = round(im.width * scale)
scaledHeight = round(im.height * scale)

# Make blank output image with the scaled width and height
output = Image.new(im.mode, (scaledWidth, scaledHeight))

for y in range(output.height):
    for x in range(output.width):
        (r, g, b) = im.getpixel((x // scale, y // scale))
        output.putpixel((x, y), (r, g, b))

# Save output image
output.save("scaled.png")
