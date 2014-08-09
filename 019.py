"""
Project Euler Problem #19
==========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

start = (1, 1, 1901)

def leapYear(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False

# Can be trivially modified to return day of week (weekday variable)
def firstSundays(day, month, year):
    weekday = 2
    firstSundays = 0
    d, m, y = start
    while (d != day or m != month or y != year):
        d += 1
        weekday += 1

        if weekday > 7:
            weekday = 1

        incrementMonth = False

        if m == 2:
            if leapYear(y) and d > 29:
                incrementMonth = True
            elif not leapYear(y) and d > 28:
                incrementMonth = True
        elif (m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
            incrementMonth = True
        elif d > 31:
            incrementMonth = True

        if incrementMonth:
            d = 1
            m += 1

        if m > 12:
            m = 1
            y += 1

        if weekday == 7 and d == 1:
            firstSundays += 1

    #return weekday
    return firstSundays

print firstSundays(31,12,2000)
