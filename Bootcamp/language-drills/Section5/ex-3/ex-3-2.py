from datetime import datetime, timedelta

today = datetime.now()
next_week = today + timedelta(days=7)
print("Today:", today)
print("7 days later:", next_week)
