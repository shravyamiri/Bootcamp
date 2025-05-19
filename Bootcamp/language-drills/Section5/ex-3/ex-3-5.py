from datetime import datetime
import calendar

date = datetime(2024, 1, 1)
weekday_name = calendar.day_name[date.weekday()]
print("Day of the week:", weekday_name)
