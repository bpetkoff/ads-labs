
# Task 5 - find the duplucated number

def dublicates_detector(input):

    with open("{}.txt".format(input), "r") as f:
        numbers = f.read()
    list_numbers = numbers.split('\n')
    doubles_list = []
    while len(list_numbers) > 0:
        check_number = list_numbers.pop(0)
        if check_number in list_numbers:
            doubles_list.append(check_number)
    return doubles_list

print(dublicates_detector("lucky ids"))
