
from datetime import date

date_1 = date(2017, 10, 20)
date_2 = date(2021, 1, 31)
date_3 = date(2015, 8, 5)

# Не удаляйте код дальше, он нужен для проверки

format = "%d %B %Y"

print(date_1.strftime(format))
print(date_2.strftime(format))
print(date_3.strftime(format))


