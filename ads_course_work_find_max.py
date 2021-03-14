import time
import timeit
import random


books_tpls = (("Light Fantastic", (25, 108)),
              ("Guards, Guards", (3, 60)),
              ("Witches Abroad", (25, 85)),
              ("Good Omens", (5, 250)),
              ("Small Gods", (15, 150))
              )
books_dict = {"Light Fantastic": 25,
              "Guards, Guards": 3,
              "Witches Abroad": 25,
              "Good Omens": 5,
              "Small Gods": 15
              }

books_lst = [["Light Fantastic", 25],
             ["Guards, Guards", 3],
             ["Witches Abroad", 25],
             ["Good Omens", 5],
             ["Small Gods", 15]
             ]

############################### List ###################################



def random_lst_generator(r):
    """
    This function generates lists with random elements
    """
    arr = []
    for i in range(r):
        arr += [[str(random.randint(1, r)), random.randint(1, r)]]
    return arr

def most_popular_diplicates_lst(lst, input):
    start = time.time()
    temp = 0
    i = 0
    for el in lst:
        # print(el)
        if el[1] > temp:
            book = []
            temp = el[1]
            book += [el]
        else:
            if el[1] == temp:
                temp = el[1]
                book += [el]
    print("Time for", input, "items in a list -", time.time() - start)
    return book

# print(most_popular_diplicates_lst(random_lst_generator(1000), 1000))
# print(most_popular_diplicates_lst(books_lst, 5))
# print(random_lst_generator(5))

############################### Dictionary ###################################


def random_dict_generator(r):
    """
    This function generates dictionaries with random keys and values
    """
    arr = {}
    for i in range(1, r):
        arr[str(i)] = (random.randint(1, r))
    return arr



def most_popular_diplicates_dict(dict, input):
    start = time.time()
    temp_1 = 0
    for k, v in dict.items():
        if v> temp_1:
            book = {}
            temp_1 = v
            book[k] = v
        else:
            if v == temp_1:
                temp_1 = v
                book[k] = v
    print("Time for", input, "in a dictionary -", time.time() - start)
    return book

# input = 320000
# print(most_popular_diplicates_lst(random_lst_generator(input), input))
# print(most_popular_diplicates_dict(random_dict_generator(input), input))



