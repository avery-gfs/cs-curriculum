# Generate a wave using text characters.
#
# See

import math
import time

n = 0

while True:
    padding = round(20 + 20 * math.sin(n)) * " "
    print(f"{padding}*")
    n += 0.2
    time.sleep(0.05)
