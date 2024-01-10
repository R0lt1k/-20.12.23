import datetime

def first_monday(year, week):
    first_day = datetime.date(year, 1, 1)

    starting_weekday = first_day.weekday()

    days_to_add = 0 if starting_weekday == 0 else 7 - starting_weekday

    first_monday = first_day + datetime.timedelta(days=days_to_add)

    target_date = first_monday + datetime.timedelta(weeks=week-1)

    return target_date

year = int(input("Введите год: "))
week = int(input("Введите номер недели: "))

result = first_monday(year, week)

print(f"Дата первого понедельника {week} недели {year} года: {result}")
