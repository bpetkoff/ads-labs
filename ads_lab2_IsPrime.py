import time

# This function returnes True if the input number is a prime number and False if not
# First algorithm
def is_prime_first(input):
    start = time.time()
    j = 0
    if input > 1:
        for n in range(2, input):
            if input % n == 0:
                j += 1
        if j == 0:
            print("The number is a prime")
            print("Time take is: ", time.time() - start, " seconds")
        else:
            print("The number is not a prime")
            print("Time take is: ", time.time() - start, " seconds")
    else:
        print("The number is not a prime")
is_prime_first(14742)
is_prime_first(331778)
is_prime_first(7772778)
is_prime_first(111181112)




# This function returnes True if the input number is a prime number and False if not
# Second algorithm
def is_prime_second(input):
    start = time.time()
    j = 0
    if input > 1:
        for n in range(2, input):
            if input % n == 0:
                j += 1
                if j > 0:
                    print("The number is not a prime")
                    print("Time take is: ", time.time() - start, " seconds")
                    return
        if j == 0:
            print("The number is a prime")
            print("Time take is: ", time.time() - start, " seconds")
        # else:
        #     print("The number is not a prime")
        #     print("Time take is: ", time.time() - start, " seconds")
    else:
        print("The number is not a prime")
is_prime_second(14742)
is_prime_second(331778)
is_prime_second(7772778)
is_prime_second(111181112)


"""The fuction is linear - O(n)"""
