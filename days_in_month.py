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
    	days == 0
    else:
    	year1 += 1
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


#print(days_in_months1(2000, 1))
print(days_in_months2(2000, 3))
