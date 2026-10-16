totalSeconds = int(input("Enter a duration in seconds: "))

seconds = totalSeconds % 60
minutes = totalSeconds // 60 % 60
hours = totalSeconds // (60 * 60) % 24
days = totalSeconds // (60 * 60 * 24)

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
