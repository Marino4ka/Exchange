def nextDay(year, month, day):
    if day == 30:
        if month == 12:
            year = year + 1
            month = 1
            day = 1
        else:
            year = year
            month = month + 1
            day = 1
    else:
        year = year
        month = month
        day = day + 1
    return year, month, day
