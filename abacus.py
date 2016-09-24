def print_abacus(value):
    answer = ''
    string = '|00000*****|'
    len_number = len(str(value))
    while len_number != 10:
        len_number = len_number + 1
        answer += (string[0:-1] + '   ' + string[-1] + '\n')
    len_number = len(str(value))
    new_value = str(value)[::-1]
    while len_number != 0:
        len_number = len_number - 1
        number_value = int(str(new_value)[len_number]) + 1
        answer += (string[0:-number_value] + '   ' + string[-number_value:]+ '\n')
    print (answer)

print_abacus(123)