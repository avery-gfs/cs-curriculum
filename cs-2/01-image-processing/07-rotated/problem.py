# Rotate an image by 30 degrees around its central point

from PIL import Image
import math

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, (im.width, im.height))

# Your code goes here

# Save output image
output.save("rotated.png")
