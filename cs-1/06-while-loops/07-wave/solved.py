# Generate a sine wave using text characters.
#
# See https://github.com/avery-gfs/cs-curriculum/blob/public/assets/wave.gif

import math
import time

n = 0

while True:
    padding = round(20 + 20 * math.sin(n)) * " "
    print(f"{padding}*")
    n += 0.2
    time.sleep(0.05)
