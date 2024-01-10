import datetime

def all_sundays(year):
    sundays = []
    date = datetime.date(year, 1, 1)
    
    while date.year == year:
        if date.weekday() == 6:
            sundays.append(date)
        date += datetime.timedelta(days=1)
    
    return sundays

year = 2008
sundays = all_sundays(year)

for sunday in sundays:
    print(sunday.strftime("%Y-%m-%d"))
