lines = ["^"]

for i in range(5):
    pad = " " * (2**i)
    top = [pad + l + pad for l in lines]
    bottom = [l + " " + l for l in lines]
    lines = top + bottom

for line in lines:
    print(line)
