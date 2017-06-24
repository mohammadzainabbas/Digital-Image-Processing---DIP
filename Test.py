import csv, random, scipy, sklearn, numpy as np

def Minimum_Distance(mean_list, unknown):
    return


def disp(my_list):
    for i in my_list:
        print(i)


def Display(my_list):
    for i in range(len(my_list)):
        print(my_list)

my_list = []

with open('dataset.csv',newline='') as f:
    reader = csv.reader(f)

    for row in reader:
        my_list.append(row)

#print(my_list)

for i in range(len(my_list)):

    my_list[i][0] = float(my_list[i][0])
    my_list[i][1] = float(my_list[i][1])
    my_list[i][2] = float(my_list[i][2])
    my_list[i][3] = float(my_list[i][3])
    
    if my_list[i][4] == 'Iris-virginica':
        my_list[i][4] = 2
    elif my_list[i][4] == 'Iris-versicolor':
        my_list[i][4] = 1
    elif my_list[i][4] == 'Iris-setosa':
        my_list[i][4] = 0

Training_list = []

print(len(my_list))

Training_list = my_list[0:25]
Training_list.extend(my_list[50:75])
Training_list.extend(my_list[100:125])


Training_list = np.array(Training_list)
disp(Training_list)

##Training_list.append(my_list[0:25], axis=0) 
##Training_list.append(my_list[50:75], axis=0)
##Training_list.append(my_list[100:125], axis=0)


###Display(Training_list)
print(len(Training_list))

#Mean = np.array(np.zeros((3,5)),dtype=np.float)
#Mean=[]
##for i in range(3):
##    for j in range(5):
##        if i == 0:
##            Mean[i][j] = (np.mean(Training_list[0:25], axis=0))
##        elif i==1:
##            Mean[i][j] = (np.mean(Training_list[25:50], axis=0))
##        elif i==2:
##            Mean[i][j] = (np.mean(Training_list[50:75], axis=0))
Mean = (np.mean(Training_list[0:25], axis=0))
Mean = np.concatenate((Mean, (np.mean(Training_list[25:50], axis=0))))
Mean = np.concatenate((Mean, (np.mean(Training_list[50:75], axis=0))))



Mean_list = []

Mean_list.append(Mean[0:5])
Mean_list.append(Mean[5:10])
Mean_list.append(Mean[10:15])
disp(Mean_list)