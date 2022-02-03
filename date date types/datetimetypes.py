from datetime import datetime, timedelta

current_date_and_time = datetime.now()
print(f"{current_date_and_time:%Y-%m-%d}")
print(f"{current_date_and_time:%b-%d-%Y}")
print(f"{current_date_and_time:%A}")
one_day = timedelta(days=1)
yesterday = current_date_and_time - one_day
print(f"{yesterday:%b-%d-%Y}")

print(f"day: {current_date_and_time.day}")
print(f"month: {current_date_and_time.month}")
print(f"year: {current_date_and_time.year}")
print(f"weekday: {current_date_and_time:%a}")
print(f"weekday: {current_date_and_time:%A}")
print(f"hours: {current_date_and_time.hour}")
print(f"minutes: {current_date_and_time.minute}")
print(f"seconds: {current_date_and_time.second}")

one_week = timedelta(weeks=1)
last_week = current_date_and_time - one_week
print(f"{last_week:%b-%d-%Y}")

