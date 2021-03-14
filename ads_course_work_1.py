"""
In a collection of positive numbers find
the min and max dividers to a number D.
Return -1 if there are no such numbers
"""


arr = [20, 5, 6, 18, 25, 3]

D = 2

def find_dividers(arr, D):
    new_arr = []
    for num in arr:
        if num % D == 0:
            new_arr.append(num)
    return new_arr


def find_div_rec(arr, D):
    if len(arr) == 0:
        pass
    else:
        print(arr)
        print(arr.pop(D))
        find_div_rec(arr, D)
    return arr

# print(find_dividers(arr, 2))
print(find_div_rec(arr, 0))

