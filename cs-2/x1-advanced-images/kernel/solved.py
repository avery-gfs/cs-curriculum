from PIL import Image

# Load input image
im = Image.open("dali.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, im.size)

# https://en.wikipedia.org/wiki/Kernel_(image_processing)
# https://setosa.io/ev/image-kernels/


def processKernel(im, kernel, outputName):
    for y in range(1, im.height - 1):
        for x in range(1, im.width - 1):
            newR = 0
            newG = 0
            newB = 0

            for ky in [-1, 0, 1]:
                for kx in [-1, 0, 1]:
                    factor = kernel[ky + 1][kx + 1]
                    (r, g, b) = im.getpixel((x + kx, y + ky))

                    newR += r * factor
                    newG += g * factor
                    newB += b * factor

            output.putpixel((x, y), (round(newR), round(newG), round(newB)))

    output.save(outputName)


sharpen = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
]

processKernel(im, sharpen, "kernel-sharpen.png")

edge = [
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0],
]

processKernel(im, edge, "kernel-edge.png")

blur = [
    [1 / 9, 1 / 9, 1 / 9],
    [1 / 9, 1 / 9, 1 / 9],
    [1 / 9, 1 / 9, 1 / 9],
]

processKernel(im, blur, "kernel-blur.png")
