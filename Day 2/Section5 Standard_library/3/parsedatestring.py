from datetime import datetime

date_str = "2024-01-01"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed datetime object:", parsed_date)
