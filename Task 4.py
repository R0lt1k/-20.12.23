from datetime import datetime, timedelta

date_string = input("Введите исходную дату (в формате дд.мм.гггг): ")
date = datetime.strptime(date_string, "%d.%m.%Y")

years = int(input("Введите количество лет для добавления: "))

new_date = date + timedelta(days=years*365)

print("Новая дата:", new_date.strftime("%d.%m.%Y"))
