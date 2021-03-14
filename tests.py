# a = [1, 4, 3, 2]
# b = []
# for i in a:
#     b.append(a.pop())
#
# print(b)


a = [[1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0],
     [0, 0, 2, 4, 4, 0],
     [0, 0, 0, 2, 0, 0],
     [0, 0, 1, 2, 4, 0]]
b = []

for row in a:
    for col in row:
        b.append(col)
print(b)
