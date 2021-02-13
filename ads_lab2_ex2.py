import time
import random

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

staircase(2)
