totalSeconds = int(input("Enter a duration in seconds: "))

seconds = totalSeconds % 60
minutes = totalSeconds // 60 % 60
hours = totalSeconds // (60 * 60) % 24
days = totalSeconds // (60 * 60 * 24)

# Calculate the days, hours, minutes, and seconds in the total
# number of seconds entered by the user. Print these values,
# omitting zero values, with correct pluralization
#
# Examples:
#
# Enter a duration in seconds: 1234561
#
# 14 days
# 6 hours
# 56 minutes
# 1 second
#
# Enter a duration in seconds: 3605
#
# 1 hour
# 5 seconds

if days == 1:
    print("1 day")

elif days > 0:
    print(f"{days} days")

if hours == 1:
    print("1 hour")

elif hours > 0:
    print(f"{hours} hours")

if minutes == 1:
    print("1 minute")

elif minutes > 0:
    print(f"{minutes} minutes")

if seconds == 1:
    print("1 second")

elif seconds > 0:
    print(f"{seconds} seconds")

# Or, using a function
#
# def showUnits(n, name):
#     if n >= 2:
#         print(f"{n} {name}s")
#     elif n == 1:
#         print(f"{n} {name}")
#
# showUnits(days, "day")
# showUnits(hours, "hour")
# showUnits(minutes, "minute")
# showUnits(seconds, "second")
