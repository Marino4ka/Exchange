def year_type(year):
    leap = 366
    standart = 365
    if year%100 == 0 and year%400 != 0 or year%4 != 0: 
        year_type = standart
    else:
        year_type = leap
    return year_type
 
def days_in_years(year1, year2):
    if year1 == year2 or year2 - year1 == 1:
        days = 0
    else:
        year1 += 1
        days = year_type(year1)
    while year1 < year2 - 1:
        year1 += 1
        days_in_that_year = year_type(year1)
        days += days_in_that_year
    return days

def days_in_months1(year1, month1):
    if month1 == 12:
        days = 0
    else:
        daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month1 = month1 + 1
        if year_type(year1) == 366 and daysOfMonths[month1 - 1] == 28: 
            days = 29
        else:
            days = daysOfMonths[month1 - 1]
        while month1 != 12:
            month1 = month1 + 1
            days = days + daysOfMonths[month1 - 1]
    return days

def days_in_months2(year2, month2):
    if month2 == 1:
        days = 0
    else:
        daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month2 = month2 - 1
        if year_type(year2) == 366 and daysOfMonths[month2 - 1] == 28:
            days = 29
        else:
            days = daysOfMonths[month2 - 1]
        while month2 != 1:
            month2 = month2 - 1
            days = days + daysOfMonths[month2 - 1]
    return days

def days_in_days1(year1, month1, day1):
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year_type(year1) == 366 and daysOfMonths[month1 - 1] == 28:
        days = 29
    else:
        days = daysOfMonths[month1 - 1]
    days_in_days1 = days - day1
    return days_in_days1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	if year1 == year2:
		return days_in_years(year1, year2) + days_in_months1(year1, month1) + days_in_months2(year2, month2) + days_in_days1(year1, month1, day1) + day2 - year_type(year1) 
	if year2 - year1 == 1:
		return days_in_years(year1, year2) + days_in_months1(year1, month1) + days_in_months2(year2, month2) + days_in_days1(year1, month1, day1) + day2 - year_type(year1) + year_type(year2)
	result = days_in_years(year1, year2) + days_in_months1(year1, month1) + days_in_months2(year2, month2) + days_in_days1(year1, month1, day1) + day2
	return result

#test_cases = [((2012,1,1,2012,2,28), 58), 
                  #((2012,1,1,2012,3,1), 60),
                  #((2011,6,30,2012,6,30), 366),
                  #((2011,1,1,2012,8,8), 585 ),
                  #((1900,1,1,1999,12,31), 36523)]

print(daysBetweenDates(2012,1,1,2012,2,28))
print(daysBetweenDates(2012,1,1,2012,3,1))
print(daysBetweenDates(2011,6,30,2012,6,30))
print(daysBetweenDates(2011,1,1,2012,8,8))
print(daysBetweenDates(1900,1,1,1999,12,31))

#print(daysBetweenDates(2012,1,1,2012,2,28))