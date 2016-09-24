def print_abacus(value):
    string = '|00000*****|'
    len_number = len(str(value))
    while len_number != 10:
        len_number = len_number + 1
        print string
    else:
        while len_number != 0:
            len_number = len_number - 1
            number_value = int(str(value)[len_number])
            print string[0:number_value] + '   ' + string[number_value:]

