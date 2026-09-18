# Example input:
#
# velocity (m/s): 10
# acceleration (m/s²): 2
# time (s): 8
#
# Example output:
#
# distance at time 8.0s: 144.0m

v = float(input("velocity (m/s): "))
a = float(input("acceleration (m/s²): "))
t = float(input("time (s): "))

distance = v * t + 0.5 * a * t**2

print(f"distance at time {t}s: {distance}m")
