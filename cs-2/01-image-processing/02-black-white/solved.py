# Convert an image to black and white

from PIL import Image

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, (im.width, im.height))

for y in range(im.height):
    for x in range(im.width):
        (r, g, b) = im.getpixel((x, y))

        l = round(0.2126 * r + 0.7152 * g + 0.0722 * b)

        if l < 105:
            (r, g, b) = (0, 0, 0)
        else:
            (r, g, b) = (255, 255, 255)

        output.putpixel((x, y), (r, g, b))

# Save output image
output.save("black-white.png")
