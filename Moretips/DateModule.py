import datetime

print(f"\n datetime.datetime.today():  {datetime.datetime.today()}")


today_date = datetime.datetime.today()
print(
    f"\n Year: {today_date.year} \n Month: {today_date.month} \n Day: {today_date.day}")

print(
    f"\n Hour: {today_date.hour} \n Minute: {today_date.minute} \n Second: {today_date.second}")

# set the time
some_date = datetime.datetime(2019, 5, 27)
print(some_date)
some_date = datetime.datetime(2019, 5, 27, 9, 5, 25)
print(some_date)
print(f"some_date.date(): {some_date.date()}")
print(f"some_date.time(): {some_date.time()}")

day = some_date
print(f"day: {day}")

day = day + datetime.timedelta(days=90)
print(f"day plus 90 {day}")

print(f"day: {day}, plus 3 weeks: {day+datetime.timedelta(weeks=3)} ")

print(f"day: {day}, plus 48 hours: {day+datetime.timedelta(hours=48)} ")

