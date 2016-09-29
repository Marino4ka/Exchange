def is_leap_baby(day,month,year):
	if day == 29 and month == 2:
		if year%100 == 0 and year%400 != 0 or year%4 != 0:
			status = False
		else:
			status = True
	else:
		status = False
	print (status)
	return status


def output(status,name):
	if status == True:
		print ("%s is one of an extremely rare species. He is a leap year baby!" % name)
	else:
		print ("There's nothing special about %s's birthday. He is not a leap year baby!" % name)