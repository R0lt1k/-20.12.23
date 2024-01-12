import datetime

diff1 = datetime.timedelta(days=10, hours=3, minutes=30, seconds=15)
diff2 = datetime.timedelta(days=5, hours=2, minutes=15, seconds=45)

total_diff = diff1 + diff2    

days = total_diff.days
hours, remainder = divmod(total_diff.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print("Дни:", days)
print("Часы:", hours)
print("Минуты:", minutes)
print("Секунды:", seconds)
