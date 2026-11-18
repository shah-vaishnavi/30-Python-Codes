import datetime

today = datetime.datetime.now()

print("Current Date and Time:", today)

print("Day:", today.day)

print("Month:", today.month)

print("Year:", today.year)

date1 = datetime.date(2026, 1, 1)

date2 = datetime.date(2026, 12, 31)

difference = date2 - date1

print("Difference Between Dates:", difference.days, "days")