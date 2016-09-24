def print_abacus(value):
    answer = ''
    string = '|00000*****|'
    len_number = len(str(value))
    while len_number != 10:
        len_number = len_number + 1
        answer += (string[0:-1] + '   ' + string[-1] + '\n')
    len_number = len(str(value))
    n = 0
    while n != len_number:
        n = n + 1
        number_value = int(str(value)[n - 1]) 
        answer += (string[0:-number_value] + '   ' + string[-number_value:]+ '\n')
    print (answer)

print_abacus(234)
        