
# Task 4 - Top three lucky numbers

def top_three(input):
    with open("{}.txt".format(input), "r") as f:
        numbers = f.read()
    list_numbers = numbers.split('\n')
    top_three = []
    while len(top_three)<=2:
        top_number = list_numbers[0]
        for number in list_numbers:
            if int(number) > int(top_number):
                top_number = number
        top_three.append(top_number)
        list_numbers.remove(top_number)
    return top_three

print(top_three("lucky ids"))
