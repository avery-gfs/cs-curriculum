totalSeconds = int(input("Enter a duration in seconds: "))

seconds = totalSeconds % 60
minutes = totalSeconds // 60 % 60
hours = totalSeconds // (60 * 60) % 24
days = totalSeconds // (60 * 60 * 24)

# Calculate the days, hours, minutes, and seconds in the total
# number of seconds entered by the user. Print these values,
# omitting zero values, with correct pluralization.
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
# Enter a duration in seconds: 7205
#
# 2 hours
# 5 seconds
