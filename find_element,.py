# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

def find_element(list, element):
    position = 0
    if list[-1] == element:
        position = len(list) - 1
    else: #if list[-1] != element
        if list[0] == element:
                position = 0
        else: #if list[0] != element
            for e in list:
                if e == element:
                    position = position + 1
                else: #if e!= element
                    position = -1
    return position
    
# variant cherz index:
def find_element(list, element):
    if element in list:
        return list.index(element)
    else:
        return -1
    return position

print find_element(['flower','petal', 'tree', 'gras'],'petal')


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1