def year_type(year):
    leap = 366
    standart = 365
    if year%100 == 0 and year%400 != 0 or year%4 != 0:
        year_type = standart
    else:
        year_type = leap
    return year_type
 
def days_in_years(year1,year2):
    days = year_type(year1)
    while year1 < year2:
        year1 = year1 + 1
        days_in_that_year = year_type(year1)
        days = days + days_in_that_year
    return days

def days_in_months1(year1,month1):
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month1 = month1 + 1 # for counting from the next month
    if year_type(year1) == 366 and daysOfMonths[month1 - 1] == 1:
        days = 29
    else:
        days = daysOfMonths[month1 - 1]
    while month1 != 12:
        month1 = month1 + 1
        days = days + daysOfMonths[month1 - 1]
    return days

def days_in_months2(year2,month2):
	daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	month2 = month2 - 1 # for counting untill the previous month
	if year_type(year2) == 366 and daysOfMonths[month2 - 1] == 1:
		days = 29
    else:
        days = daysOfMonths[month2 - 1]
    while month2 != 0:
    	month2 = month2 - 1
        days = days + daysOfMonths[month2 - 1]
    return days

def days_in_days1(year1,month1,day1):
	daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if year_type(year1) == 366 and daysOfMonths[month1 - 1] == 1:
        days = 29
    else:
        days = daysOfMonths[month1 - 1]
    days_in_days1 = days - day1
    return days_in_days1

def days_in_days2(day2):
	days_in_days2 = day2
	return day2


