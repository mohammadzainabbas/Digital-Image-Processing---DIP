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
li = list(l[0:2,0:2])
print(li)
output_list = []
clockwise(l, output_list)

print (output_list)