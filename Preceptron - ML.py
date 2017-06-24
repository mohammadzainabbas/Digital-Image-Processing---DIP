import numpy as np, csv, random

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

    random.shuffle(my_list)        
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
    
    Training_list = my_list[0:75]
    Testing_list = my_list[75:150]
    
    Training_list = np.array(Training_list)
    Testing_list = np.array(Testing_list)

    return Training_list, Testing_list

#Returns Accuracy % 
def Calculate_Accuracy(actual, predicted):
    error = 0

    for i in range(len(actual)):
        if (int(actual[i] - predicted[i])!=0):
            error = error + 1

    print("Total predictions are: ", len(predicted))
    print("Total correct predictions are: ", len(predicted) - int(error))
    print("Total false predictions are: ", int(error))

    accuracy = ( (float(len(actual)) - float(error)) / len(actual)) * 100

    return accuracy
            
my_list = String_to_Float(ReadFile())
Training_list, Testing_list = Split_In_Two(my_list)
Features_list = [features[0:4] for features in Training_list]
Labels_list = [element[4] for element in Training_list]

Test_Features_list = [features[0:4] for features in Testing_list]
Actual_Labels = [element[4] for element in Testing_list]

Actual_Labels = np.array(Actual_Labels)

Predicted_Labels = K_Nearest_Neighbors(Features_list, Labels_list, Test_Features_list)

Accuracy = Calculate_Accuracy(Actual_Labels, Predicted_Labels)

print("Accuracy % is: ", Accuracy)
