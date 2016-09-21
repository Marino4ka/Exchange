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

print(days_in_years(1999, 2001))