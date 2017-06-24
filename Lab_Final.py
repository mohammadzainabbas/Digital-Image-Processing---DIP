from os import listdir
from os.path import isfile, join
import numpy as np, cv2 as cv, matplotlib.pyplot as plt, math
import scipy, sklearn, csv, random
from sklearn import neighbors

#For training model and predicting using K-Nearest-Neighbor (KNN) algorithm
def K_Nearest_Neighbors(training_features, training_labels, testing_features):
    K = int(input("Enter the numbers of neighbors 'K': "))
    
    model = neighbors.KNeighborsClassifier(n_neighbors=K)
    model.fit(training_features, training_labels)
    
    predicted_labels = model.predict(testing_features)

    return predicted_labels

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

def Histogram(img):

    hist = np.zeros((1,256),dtype = np.int)

    r,c = np.shape(img)

    for i in range(r):
        for j in range(c):
            hist[0,img[i,j]] = hist[0,img[i,j]] + 1

    return hist

def Binary_List_To_Decimal(my_list):
    return int(str(''.join(str(e) for e in my_list)), 2)

def Clockwise__Chunk_To_List(input_list, output_list=[]):
    list_size = len(input_list[0])
    if list_size == 1:
        return output_list
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

        return Clockwise__Chunk_To_List(new_list, output_list)

def Threshold_Chunk_To_Binary_List(list_1, t):
    #print(list_1)
    my_list = Clockwise__Chunk_To_List(list_1,[])
    #print(my_list)
    my_list = list(reversed(my_list))
    #print(my_list)
    return [(0,1)[i > t] for i in my_list]

def Local_Binary_Pattern(img):
    boxsize=3
    r,c = np.shape(img)
    pad = int(np.floor(boxsize/2))
    new_img = np.zeros((r,c),dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            if(i>0 and i<r-1 and j>0 and j<c-1):
                threshold = img[i,j]
                my_list = Threshold_Chunk_To_Binary_List((img[i-pad:i+pad+1,j-pad:j+pad+1]).tolist(), threshold)
                new_img[i,j] = Binary_List_To_Decimal(my_list)
            else:
                new_img[i,j] = 0
    return new_img
        


mypath=r'E:\CEME\6th Semester\Digital Image Processing\Lab Final Syndicate A\PH2 Dataset\Training'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv.imread( join(mypath,onlyfiles[n]), 0 )

binary_images = np.empty(int(len(onlyfiles)/2), dtype=object)
gray_images = np.empty(int(len(onlyfiles)/2), dtype=object)
for n in range(0, int(len(onlyfiles)/2)):
  binary_images [n] = images[2*n + 1]
  gray_images [n] = images[2*n]

bins=8
features = []
for n in range(0, 2):
    hist = Histogram(Local_Binary_Pattern(gray_images[n]))
    new_hist = np.array(np.array_split(hist.flatten(), bins))
    new_hist = [np.sum(i) for i in new_hist]
    features.append(new_hist)


Predicted_Labels = K_Nearest_Neighbors(Features_list, Labels_list, Test_Features_list)

Accuracy = Calculate_Accuracy(Actual_Labels, Predicted_Labels)

print(features)
print(np.shape(images))
print(np.shape(binary_images))
cv.imshow('1', images[0])

cv.imshow('1', binary_images[0])
cv.waitKey()
cv.destroyAllWindows()