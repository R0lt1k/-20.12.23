import calendar

year = int(input("Введите год: "))
month = int(input("Введите месяц: "))

cal = calendar.HTMLCalendar()
html = cal.formatmonth(year, month)

with open("calendar.html", "w") as file:
    file.write(html)
    print("HTML-календарь создан.")
