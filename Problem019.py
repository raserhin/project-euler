"""
You are given the following information, but you may prefer to do some research for yourself.

  1 Jan 1900 was a Monday.
  Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from time import time

months = [ 31, # January
           28, # February
           31, # March
           30, # April
           31, # May
           30, # June
           31, # July
           31, # August
           30, # September
           31, # October
           30, # November
           31 # December
        ] 

def sundays(lo_year, hi_year):
    day_count = 0
    sunday_count = 0

    for year in range(lo_year,hi_year+1):
        for month, days in enumerate(months):
            day_count += days
            if year % 4 == 0 and month == 1 and year % 400 != 0:
                day_count += 1
            if day_count % 7 == 0:
                sunday_count += 1
    return sunday_count

start_time = time()
result = sundays(1901, 2000)
final_time = time()

print(result)