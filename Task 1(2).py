import datetime

utc = datetime.datetime.utcnow()
print("Время по Гринвичу:", utc)

local_time = datetime.datetime.now()
print("Местное время:", local_time)
