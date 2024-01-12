import datetime

date1 = datetime.date(2020, 1, 1)
date2 = datetime.date(2020, 12, 31)

delta = date2 - date1
print("Количество дней:", delta.days)
