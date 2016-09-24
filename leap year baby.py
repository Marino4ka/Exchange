def is_leap_baby(day,month,year):
   if day == 29 and month == 2 and year%100 != 0 and year%400 == 0 or year%4 == 0:
   		status = True
   else:
   		status = False
   		return status


# The function 'output' prints one of two statements based on whether 
# the is_leap_baby function returned True or False.

#def output(status,name):
    #if status:
        #print "%s is one of an extremely rare species. He is a leap year baby!" % name
    #else:
        #print "There's nothing special about %s's birthday. He is not a leap year baby!" % name

is_leap_baby(day,month,year)