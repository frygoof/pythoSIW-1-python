# matrix = [[0, 0, 0, 1],
#           [0, 0, 1, 0],
#           [0, 1, 0, 0],
#           [1, 0, 0, 0]]
# for row in matrix:
#     print(' '.join(map(str, row)))

# matrix = [
#     [1, 2, 3, 4],
#     [8, 7, 6, 5],
#     [9, 10, 11, 12],
#     [16, 15, 14, 13]
# ]
# for row in matrix:
#     print(row)


# import numpy as np
# matrix = np.array([
#     [1, 2, 3, 4],
#     [2, 3, 4, 5],
#     [3, 4, 5, 6],
#     [4, 5, 6, 7]
# ])
#
# print(matrix)


# start_value = 1
# matrix = []
# for i in range(4):
#     row = []
#     for j in range(4):
#         row.append(start_value)
#         start_value += 1
#     matrix.append(row)
# for row in matrix:
#     print(row)


# matrix = [[0] * 4 for _ in range(4)]
# value = 16
# for i in range(4):
#     for j in range(4):
#         matrix[i][j] = value
#         value -= 1
# for row in matrix:
#     print(row)


# import numpy as np
# values = np.array([1, 2, 3, 4, 12, 13, 14, 15, 11, 16, 15, 6, 10, 9, 8, 7])
# matrix = values.reshape((4, 4))
# print(matrix)