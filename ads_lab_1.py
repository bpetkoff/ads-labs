import time
import random

# # Task 1 - this is the function for finding the min and max
#
# def minmax(input):
#     t1 = time.time()
#     i = input[0]
#     s = input[0]
#     for number in input:
#         if number < i:
#             i = number
#         elif number > s:
#             s = number
#     print(i, s)
#     t2 = time.time()
#     print("The time taken is ", t2-t1, " seconds")
#
#
# minmax([3, 6, 7, -5, 89, 12])



#  Task 2 - this is the function with the staircase algorithm
def staircase(input):
    t1 = time.time()
    if input>0:
        for j in range(input):
            for k in range(j, input-1):
                print(" ", end='')
            for i in range(j+1):
                print("#", end='')
            print()
    t2 = time.time()
    print("The time taken is ", t2-t1, " seconds")

staircase(25)


#
# # Task 3 - Lucky numbers
# #
# chosen_number = input("Please enter your number: ")
#
# with open("lucky ids.txt", "r") as f:
#     numbers = f.read()
# list_numbers = numbers.split('\n')
# if chosen_number in list_numbers:
#     print("Yes - your id is listed")
# else:
#     print("No - your id is NOT listed")
#
# Task 4 - Top three lucky numbers
#
# def top_three(input):
#     with open("{}.txt".format(input), "r") as f:
#         numbers = f.read()
#     list_numbers = numbers.split('\n')
#     top_three = []
#     while len(top_three)<=2:
#         top_number = list_numbers[0]
#         for number in list_numbers:
#             if int(number) > int(top_number):
#                 top_number = number
#         top_three.append(top_number)
#         list_numbers.remove(top_number)
#     return top_three
#
# print(top_three("lucky ids"))
# #
#
#
# # Task 5 - find the duplucated number
#
# def dublicates_detector(input):
#
#     with open("{}.txt".format(input), "r") as f:
#         numbers = f.read()
#     list_numbers = numbers.split('\n')
#     doubles_list = []
#     while len(list_numbers) > 0:
#         check_number = list_numbers.pop(0)
#         if check_number in list_numbers:
#             doubles_list.append(check_number)
#     return doubles_list
#
# print(dublicates_detector("lucky ids"))
#
#
#
# # This is a list of random, shuffled numbers
# numbers_list = list(range(1, 40))
# random.shuffle(numbers_list)
# print(numbers_list)
#
# # Task 4 - Top three lucky numbers
#
# def top_three(input):
#     start = time.time()
#     top_three = []
#     while len(top_three)<=2:
#         top_number = input[0]
#         for number in input:
#             if number > top_number:
#                 top_number = number
#         top_three.append(top_number)
#         input.remove(top_number)
#     print("Time take is: ", time.time()-start, " seconds")
#     return top_three
#
#
# print(top_three(numbers_list))
#
# # def dubl_num(input):
# #     dubl = input[25] + 1
# #     list_doubl
# #     input.append[dubl]
# #     return input
# #
# # print(dubl_num(numbers_list))
#
# # Task 5 - find the duplucated number
#
# def dublicates_detector(input):
#
#     doubles_list = []
#     while len(input) > 0:
#         check_number = input.pop(0)
#         if check_number in input:
#             doubles_list.append(check_number)
#     return doubles_list
#
# print(dublicates_detector(dubl_num(numbers_list)))
