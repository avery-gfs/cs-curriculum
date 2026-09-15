# Scale an image to be twice as big

from PIL import Image

# Load input image
im = Image.open("bird.png")

scale = 2
scaledWidth = round(im.width * scale)
scaledHeight = round(im.height * scale)

# Make blank output image with the scaled width and height
output = Image.new(im.mode, (scaledWidth, scaledHeight))

# ------------------------------------------------------------
# This code copies over the pixels in their original positions
# You will need to modify it

for y in range(im.height):
    for x in range(im.width):
        (r, g, b) = im.getpixel((x, y))
        output.putpixel((x, y), (r, g, b))

# ------------------------------------------------------------

# Save output image
output.save("scaled.png")
