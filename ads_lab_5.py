import time
import random

custom_numbers = input("Please enter a number: ")
def random_numbers(custom_numbers):
    # This is a list of random, shuffled numbers
    numbers_list = list(range(1, int(custom_numbers)+1))
    random.shuffle(numbers_list)
    return numbers_list

# print(random_numbers())


random_arr = random_numbers(custom_numbers)
ascending_arr = list(range(1, int(custom_numbers)+1))
descending_arr = list(reversed(range(1, int(custom_numbers)+1)))
# print(arr)

def bubble_sort(arr):
    t_bubble_sort = time.time()
    n = len(arr)

    for i in range(n):
        swap_flag = False
        for j in range(0, n-i-1):
            # print(i, j)
            if arr[j] > arr[j+1]:
                # print(arr[j], arr[j+1], arr)
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = True
        if swap_flag == False:
            break
    # print(arr)
    print("Time for bubble sort of a", len(arr), "elements is:", time.time()-t_bubble_sort)


def selection_sort(arr):
    t_select_sort = time.time()
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # print(arr[i], arr[min_idx], arr)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # print(arr)
    print("Time for selection sort of a", len(arr), "elements is:", time.time()-t_select_sort)


def insersion_sort(arr):
    t_insertion_sort = time.time()
    n = len(arr)




print("Shuffeled numbers")
bubble_sort(random_arr)
selection_sort(random_arr)
print()
print("Ascending ordered numbers")
bubble_sort(ascending_arr)
selection_sort(ascending_arr)
print()
print("Descending ordered numbers")
bubble_sort(descending_arr)
selection_sort(descending_arr)

