import datetime

today = datetime.date.today()

print(f"today's date is {today}")

holiday = datetime.date(2021, 12, 25)
delta = holiday - today

print(f"just {delta.days} days until the holidays.")