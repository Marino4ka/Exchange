
def year_type(year):
    leap = 366
    standart = 365
    if year%100 == 0 and year%400 != 0 or year%4 != 0: 
        year_type = standart
    else:
        year_type = leap
    return year_type

print(year_type(2004))


