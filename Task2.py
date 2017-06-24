# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:55:43 2017

@author: Umer Mushtaq
"""

import random
import numpy
import scipy
import csv
from sklearn import neighbors 


Umer_List=[]
with open('dataset.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        Umer_List.append(row)
random.shuffle (Umer_List)

for i in range(len(Umer_List)):
    if(Umer_List[i][4]=='Iris-setosa'):
        Umer_List[i][4]=0
    elif(Umer_List[i][4]=='Iris-versicolor'):
        Umer_List[i][4]=1
    else:
        Umer_List[i][4]=2

Umer_List4=[]
for N in Umer_List:
    Umer_List4.append([float(i) for i in N])
  
Umer_List=Umer_List4    
    
Umer_List_Training=[]
training=[]
training=Umer_List[0:75]
testing=Umer_List[75:150]

Umer_List_Training=[item[0:4] for item in training]
labels_Training=[item[4] for item in training]

k=int(input("Enter no of Neighbours="))
my_classifier = neighbors.KNeighborsClassifier(n_neighbors=k)
my_classifier.fit(Umer_List_Training, labels_Training)


Umer_List_Testing=[item[0:4] for item in testing]
labels_Testing=[item[4] for item in testing]
labels_Testing=numpy.array(labels_Testing)

print(labels_Testing)
Test_Results = my_classifier.predict(Umer_List_Testing)
print(Test_Results)
count=0;
for i in range(len(Test_Results)):
    if(int(Test_Results[i]-labels_Testing[i])!=0):
        count=count+1

print(float(count))
Accuracy=((float(len(labels_Testing))-float(count))/len(labels_Testing))*100
print("Accuracy=",Accuracy)






