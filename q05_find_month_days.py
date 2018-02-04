# Finding the number of days in a month
from calendar import monthrange 

year = int(input("Enter year: "))
month = int(input("Enter month: "))

monthrange(year, month)

print(monthrange(year,month))
