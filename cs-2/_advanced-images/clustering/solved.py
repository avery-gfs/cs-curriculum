from PIL import Image
import math
import random

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, im.size)

# Calculate color distance between two colors
# https://en.wikipedia.org/wiki/Color_difference


def distance(c1, c2):
    (r1, g1, b1) = c1
    (r2, g2, b2) = c2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)


class Cluster:
    def __init__(self, color):
        (r, g, b) = color
        self.sumR = r
        self.sumG = g
        self.sumB = b
        self.count = 1

    def getRGB(self):
        return (
            round(self.sumR / self.count),
            round(self.sumG / self.count),
            round(self.sumB / self.count),
        )

    def distance(self, color):
        return distance(self.getRGB(), color)

    def absorb(self, color):
        (r, g, b) = color
        self.sumR += r
        self.sumG += g
        self.sumB += b
        self.count += 1


def makePalette(im):
    numClusters = 10
    numSamples = 1000
    clusters = []

    for _ in range(numClusters):
        y = random.randrange(0, im.height)
        x = random.randrange(0, im.width)
        color = im.getpixel((x, y))
        clusters.append(Cluster(color))

    for _ in range(numSamples):
        y = random.randrange(0, im.height)
        x = random.randrange(0, im.width)
        color = im.getpixel((x, y))

        closest = None
        minDist = None

        for cluster in clusters:
            dist = cluster.distance(color)

            if minDist == None or dist < minDist:
                minDist = dist
                closest = cluster

        closest.absorb(color)

    return [cluster.getRGB() for cluster in clusters]


def applyPalette(im, palette, outputName):
    for y in range(im.height):
        for x in range(im.width):
            imgColor = im.getpixel((x, y))

            bestColor = None
            minDist = None

            # Look through the colors in palette, and find
            # the one that is closest to the current pixel color
            for paletteColor in palette:
                dist = distance(imgColor, paletteColor)

                if minDist == None or dist < minDist:
                    minDist = dist
                    bestColor = paletteColor

            # Use this closest palette color in the output image
            output.putpixel((x, y), bestColor)

    # Save output image
    output.save(outputName)


palette = makePalette(im)
applyPalette(im, palette, "clustering.png")
