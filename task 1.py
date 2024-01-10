import datetime

def get_week_number(year, month, day):
    date = datetime.date(year, month, day)
    week_number = date.isocalendar()[1]
    return week_number

year = 2022
month = 12
day = 31
week_number = get_week_number(year, month, day)
print(f"Номер недели для {day}.{month}.{year}: {week_number}")
