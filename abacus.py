def print_abacus(value):
	first_position = value[0]
	while value < 9:
		value = value[+1]
		abacus = value*'*'
	return abacus

print (print_abacus(0))
print (print_abacus(12345678))
print (print_abacus(1337))

#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |