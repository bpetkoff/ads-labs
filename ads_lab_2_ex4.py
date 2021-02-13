import time
import random

# This is a list of random, shuffled numbers
numbers_list = list(range(1, 1000000))
random.shuffle(numbers_list)
# print(numbers_list)

# Task 4 - Top three lucky numbers

def top_three(input):
    start = time.time()
    top_three = []
    while len(top_three)<=4:
        top_number = input[0]
        for number in input:
            if number > top_number:
                top_number = number
        top_three.append(top_number)
        input.remove(top_number)
    print("Time take is: ", time.time()-start, " seconds")
    return top_three


print(top_three(numbers_list))
