import numpy as np
#Method 1

from math import floor
lists = [[  2,  3,  5,  9, 10]
       ,[  8,  7,  1, 11, 13]
       ,[  0,  4,  6, 21, 22]
       ,[ 12, 19, 17, 18, 25]
      , [ 14, 15, 16, 23, 24]]

n = len(lists) # assume each list also has n-length
arr = np.array(lists)
print('Input: \n', arr)
output_list = []

idx = 0
while idx <= floor(n/2):

    if len(output_list) == n*n:
        break

    # across ->
    #print("Across ->")
    for item in lists[idx][idx:n-idx]:
        output_list.append(item)
    #print(output_list)

    if len(output_list) == n*n:
        break

    # down
    #print("Down")
    for _idx in range(idx+1, n-idx-1):
        output_list.append(lists[_idx][n-idx-1])
    #print(output_list)

    if len(output_list) == n*n:
        break

    # across <-
    #print("Across <-")
    for _idx in range(n-idx-1, idx-1, -1):
        output_list.append(lists[n-idx-1][_idx])
    #print(output_list)

    if len(output_list) == n*n:
        break

    # up
    #print("Up")
    for _idx in range(n-idx-2, idx, -1):
        output_list.append(lists[_idx][idx])
    #print(output_list)

    idx += 1


print("Output:")
print('\nMethod 1:\n',output_list)


#Method 2
import itertools
def transpose_and_yield_top(arr):
    while arr:
        yield arr[0]
        arr = list(zip(*arr[1:]))[::-1]
    return arr
arr = [[2,  3,  5,  9, 10],
       [8,  7,  1, 11, 13],
       [0,  4,  6, 21, 22],
       [12, 19, 17, 18, 25],
       [14, 15, 16, 23, 24]]
rotated = list(itertools.chain(*transpose_and_yield_top(arr)))
print('\nMethod 2:\n',rotated)


#Method 3

def clockwise(input_list, output_list):
    list_size = len(input_list[0])
    if list_size == 1:
        output_list.append(input_list[0][0])
    else:
        for i in range(list_size):
            output_list.append(input_list[0][i])

        for i in range(list_size)[1:]:
            output_list.append(input_list[i][list_size - 1])

        for i in reversed(range(list_size)[:-1]):    
            output_list.append(input_list[list_size - 1][i])

        for i in reversed(range(list_size)[1:-1]):    
            output_list.append(input_list[i][0])

        new_list = list()
        for i in range(list_size - 2):
            new_list.append(input_list[i + 1][1:-1])

        return clockwise(new_list, output_list)

l = [[2, 3, 5, 9, 10],[ 8, 7, 1, 11, 13],[ 0, 4, 6, 21, 22], [12, 19, 17, 18, 25], [14, 15, 16, 23, 24]]
output_list = []
clockwise(l, output_list)

print ('\nMethod 3:\n',output_list)
