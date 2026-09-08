# Convert an image to grayscale

from PIL import Image

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, (im.width, im.height))

for y in range(im.height):
    for x in range(im.width):
        (r, g, b) = im.getpixel((x, y))

        l = round((r + g + b) / 3)
        r = l
        g = l
        b = l

        output.putpixel((x, y), (r, g, b))

# Save output image
output.save("grayscale.png")
