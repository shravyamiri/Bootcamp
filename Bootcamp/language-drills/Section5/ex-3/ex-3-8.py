from datetime import datetime, timedelta

now = datetime.now()
rounded = now.replace(minute=0, second=0, microsecond=0)

# Round up if minutes >= 30
if now.minute >= 30:
    rounded += timedelta(hours=1)

print("Original time:", now)
print("Rounded to nearest hour:", rounded)
