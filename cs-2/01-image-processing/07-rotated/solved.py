# Rotate an image by 30 degrees around its central point

from PIL import Image
import math

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, (im.width, im.height))

cy = im.height / 2
cx = im.width / 2

for y in range(im.height):
    for x in range(im.width):
        dist = math.hypot(x - cx, y - cy)
        angle = math.atan2(y - cy, x - cx)
        angle -= math.pi / 6
        ry = round(cy + dist * math.sin(angle))
        rx = round(cx + dist * math.cos(angle))

        if rx >= 0 and rx < im.width and ry >= 0 and ry < im.height:
            (r, g, b) = im.getpixel((rx, ry))
            output.putpixel((x, y), (r, g, b))

# Save output image
output.save("rotated.png")
