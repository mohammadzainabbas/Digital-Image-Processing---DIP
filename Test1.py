import numpy as np, scipy, sklearn, csv, random
from sklearn import neighbors

#To display a list
def disp(my_list):
    for i in my_list:
        print(i)
        
#Reads the file and returns it after appending in a list
def ReadFile():
    my_list = []

    with open('dataset.csv',newline='') as f:
        reader = csv.reader(f)

        for row in reader:
            my_list.append(row)
            
    return my_list

#To convert elements from string to float
def String_to_Float(my_list):
    for i in range(len(my_list)):
        if my_list[i][4] == 'Iris-virginica':
            my_list[i][4] = 2
        elif my_list[i][4] == 'Iris-versicolor':
            my_list[i][4] = 1
        elif my_list[i][4] == 'Iris-setosa':
            my_list[i][4] = 0
    l = [[float(string) for string in inner] for inner in my_list]
    return l

#Splitting list into -> Training list and Testing list
def Split_In_Two(my_list):
    Training_list = []
    Testing_list = []
    
    Training_list = my_list[0:25]
    Training_list.extend(my_list[50:75])
    Training_list.extend(my_list[100:125])
    Testing_list = my_list[25:50]
    Testing_list.extend(my_list[75:100])
    Testing_list.extend(my_list[125:150])
    
    Training_list = np.array(Training_list)
    Testing_list = np.array(Testing_list)

    return Training_list, Testing_list

my_list = String_to_Float(ReadFile())
Training_list, Testing_list = Split_In_Two(my_list)
disp(my_list)
