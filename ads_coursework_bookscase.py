import time
import timeit
import random

"""
Sort a given dictionary by one of the values in a tuple
"""

def random_numbers():
    """
    This function generates a random number
    """
    val = random.randint(1, 5)
    return val

def random_dict_generator(r):
    """
    This function generates dictionaries with random keys and values
    """
    arr = {}
    for i in range(r):
        arr[str(random.randint(1, r))] = (random.randint(1, r), random.randint(1, r))
    return arr

books_lst = [["Light Fantastic", 25, 108],
             ["Guards, Guards", 3, 60],
             ["Witches Abroad", 25, 85],
             ["Good Omens", 5, 250],
             ["Small Gods", 15, 150]
             ]

books = {"Light Fantastic": (25, 108),
         "Guards, Guards": (3, 60),
         "Witches Abroad": (25, 85),
         "Good Omens": (5, 250),
         "Small Gods": (15, 150)
         }
# print(books.key(0))

def most_popular(dict, crit):
    start = time.time()
    temp = 0
    print(dict)
    for k, v in dict.items():
        print(v[crit])
        if v[crit] > temp:
            temp = v[crit]
            book = (k, v)
    print("The most popular book is", book[0], "with", temp, "sold copies")
    print("Time:", time.time() - start)
        # temp = dict.item[key]
        # print(temp)

def most_popular_diplicates(dict, input):
    start = time.time()
    temp_1 = 0
    # book = {}
    # print(dict)
    for k, v in dict.items():
        if v[0] > temp_1:
            book = {}
            temp_1 = v[0]
            book[k] = v
        else:
            if v[0] == temp_1:
                temp_1 = v[0]
                book[k] = v

    return book, "Time for", input, time.time() - start



def sort_dict(dict, crit):
    temp = 0
    while len(dict):
        for k, v in dict.items():  # iteration through the dictionary elements
            if v[crit] > temp:
                temp = v[crit]
                book = (k, v)
        del dict[book[0]]

        return book, sort_dict(dict, 0)  # sorting the dictionary recursively and returning a tuple


def top_three(arr):
    a, b = arr
    c, d = b
    e, f = d
    return a, c, e


# a, b = sort_dict(books, 0)
# c, d = b
# e, f = d
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# print(sort_dict(random_dict_generator(1000), 0))
# print(top_three(sort_dict(books, 0)))
print(random_dict_generator(10))
# print(most_popular(random_dict_generator(1000), 0))
# print(most_popular_diplicates(random_dict_generator(10000), 10000))
# print(most_popular_diplicates(books))
# print(random_dict_generator(100))


# print(timeit.timeit('''
#
# books = {"Light Fantastic": (25, 108),
#          "Guards, Guards": (3, 60),
#          "Witches Abroad": (13, 85),
#          "Good Omens": (5, 250),
#          "Small Gods": (15, 150)
#          }
# # print(books.key(0))
#
# def sort_dict(dict, crit):
#     temp = 0
#     while len(dict):
#         for k, v in dict.items():  # iteration through the dictionary elements
#             if v[crit] > temp:     #
#                 temp = v[crit]
#                 book = (k, v)
#         del dict[book[0]]
#
#         return book, sort_dict(dict, 0)
#
# def top_three(arr):
#     a, b = arr
#     c, d = b
#     e, f = d
#     return a, c, e
# # print(top_three(sort_dict(books, 0)))
#
# ''', number=1000))
#
#

#
# print(timeit.timeit('''
#
# books = {"Light Fantastic": (25, 108),
#          "Guards, Guards": (3, 60),
#          "Witches Abroad": (13, 85),
#          "Good Omens": (5, 250),
#          "Small Gods": (15, 150)
#          }
#
# def most_popular(dict, crit):
#     temp = 0
#     for k, v in dict.items():
#         if v[crit] > temp:
#             temp = v[crit]
#             book = (k, v)
#     print("The most popular book is", book[0], "with", temp, "sold copies")
#
# print(most_popular(books, 0))
#
#
# ''', number=1000))


