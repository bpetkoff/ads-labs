import time

"""
This is the implementation of lab 5 exersice 4:
Given an array arr[] of N elements and an integer K, the task is to make any K elements of the array equal
by performing only increment operations i.e. in one operation, any element can be incremented by 1. Find
the minimum number of operations required to make any K elements equal.

"""

arr = [3, 1, 9, 9, 100, 23]
K = 4


def top_num(arr, K):
    start = time.time()
    while len(arr) > K:
        top_number = arr[0]
        for number in arr:
            if number > top_number:
                top_number = number
        arr.remove(top_number)
    print("Takes:", time.time()-start, " seconds")
    return arr

print(top_num(arr, 4))