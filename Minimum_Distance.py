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

Mean = (np.mean(Features_list[0:25], axis=0))
Mean = np.concatenate((Mean, (np.mean(Features_list[25:50], axis=0))))
Mean = np.concatenate((Mean, (np.mean(Features_list[50:75], axis=0))))

Mean_list = []

Mean_list.append(Mean[0:4])
Mean_list.append(Mean[4:8])
Mean_list.append(Mean[8:12])

Test_Features_list = [features[0:4] for features in Testing_list]
Actual_Labels = [element[4] for element in Testing_list]

Actual_Labels = np.array(Actual_Labels)

Predicted_Labels = []

for element in Testing_list:
    temp = []
    temp.append(np.sqrt( np.square(element[0] - Mean_list[0][0]) + np.square(element[1] - Mean_list[0][1]) + np.square(element[2] - Mean_list[0][2]) + np.square(element[3] - Mean_list[0][3])))
    
    temp.append(np.sqrt( np.square(element[0] - Mean_list[1][0]) + np.square(element[1] - Mean_list[1][1]) + np.square(element[2] - Mean_list[1][2]) + np.square(element[3] - Mean_list[1][3])))
    
    temp.append(np.sqrt( np.square(element[0] - Mean_list[2][0]) + np.square(element[1] - Mean_list[2][1]) + np.square(element[2] - Mean_list[2][2]) + np.square(element[3] - Mean_list[2][3])))
 
    Predicted_Labels.append(np.argmin(temp))
 
Predicted_Labels = np.array(Predicted_Labels)

Accuracy = Calculate_Accuracy(Actual_Labels, Predicted_Labels)

print("Accuracy % is: ", Accuracy)

