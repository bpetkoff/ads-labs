import time
"""
This is the solution for lab 5 exercise 3:

Given an array arr[] of N non-negative integers, 
the task is to sort these integers according 
to sum of their digits. 
"""

arr = [12, 10, 102, 31, 15]
arr2 = [14, 1101, 10, 35, 0]

def digit_add(digit):
    result = 0
    while digit > 0:
        i = digit % 10
        result += i
        digit = digit // 10
    return result


def bubble_sort(arr):
    t_bubble_sort = time.time()
    n = len(arr)

    for i in range(n):
        swap_flag = False
        for j in range(0, n-i-1):
            # print(i, j)
            if digit_add(arr[j]) > digit_add(arr[j+1]):
                # print(arr[j], arr[j+1], arr)
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = True
        if swap_flag == False:
            break
    # print(arr)
    print(arr)
    print("Time for bubble sort of a", len(arr), "elements is:", time.time()-t_bubble_sort)

bubble_sort(arr)
bubble_sort(arr2)