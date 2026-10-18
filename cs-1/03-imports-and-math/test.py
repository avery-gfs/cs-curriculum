import time
import random

# Generate two random integers, `a` and `b` where `a` is
# between `2` and `10`, and `b` is between `2` and `100`, inclusive
#
# Display the two numbers. Wait 5 seconds. Then display their product (`a * b`)
#
# Example:
#
# 6 x 27
# <wait 5 seconds>
# 162

a = random.randint(2, 10)
b = random.randint(2, 100)

print(f"{a} x {b}")

time.sleep(5)

print(a * b)
