# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:59:31 2017

@author: Umer Mushtaq
"""

import numpy
import cv2
import csv

    
Umer_List=[]
with open('dataset.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        Umer_List.append(row)
        
#print(Umer_List[1][4])        

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

Umer_List2=Umer_List[0:25]
Umer_List2[25:50]=Umer_List[50:75]
Umer_List2[50:175]=Umer_List[100:125]

Umer_List3 = [item[0:4] for item in Umer_List2]



Feature1 = [item[0] for item in Umer_List3]
Feature2 = [item[1] for item in Umer_List3]
Feature3 = [item[2] for item in Umer_List3]
Feature4 = [item[3] for item in Umer_List3]

Class1_Mean_Value=[]
Class1_Mean_Value.append(numpy.mean(Feature1[0:25]))
Class1_Mean_Value.append(numpy.mean(Feature2[0:25]))
Class1_Mean_Value.append(numpy.mean(Feature3[0:25]))
Class1_Mean_Value.append(numpy.mean(Feature4[0:25]))
print(Class1_Mean_Value)
Class2_Mean_Value=[]
Class2_Mean_Value.append(numpy.mean(Feature1[25:50]))
Class2_Mean_Value.append(numpy.mean(Feature2[25:50]))
Class2_Mean_Value.append(numpy.mean(Feature3[25:50]))
Class2_Mean_Value.append(numpy.mean(Feature4[25:50]))
print(Class2_Mean_Value)
Class3_Mean_Value=[]
Class3_Mean_Value.append(numpy.mean(Feature1[50:75]))
Class3_Mean_Value.append(numpy.mean(Feature2[50:75]))
Class3_Mean_Value.append(numpy.mean(Feature3[50:75]))
Class3_Mean_Value.append(numpy.mean(Feature4[50:75]))
print(Class3_Mean_Value)


Test_List = Umer_List[25:50]
Test_List[25:50] = Umer_List[75:100]
Test_List[50:75] = Umer_List[125:150]

temp = [item[4] for item in Test_List]
Actual_Results = numpy.asarray(temp)

my_result_list=[]
Comparison_Array=[]

for items in Test_List:
    my_result_list=[]
    my_result_list.append(numpy.sqrt( (items[0] - Class1_Mean_Value[0])**2 
                                    + (items[1] - Class1_Mean_Value[1])**2 
                                    + (items[2] - Class1_Mean_Value[2])**2 
                                    + (items[3] - Class1_Mean_Value[3])**2))
    
    my_result_list.append(numpy.sqrt((items[0] - Class2_Mean_Value[0]) ** 2
                                     + (items[1] - Class2_Mean_Value[1]) ** 2
                                     + (items[2] - Class2_Mean_Value[2]) ** 2
                                     + (items[3] - Class2_Mean_Value[3]) ** 2))

    my_result_list.append(numpy.sqrt((items[0] - Class3_Mean_Value[0]) ** 2
                                     + (items[1] - Class3_Mean_Value[1]) ** 2
                                     + (items[2] - Class3_Mean_Value[2]) ** 2
                                     + (items[3] - Class3_Mean_Value[3]) ** 2))
    
    
    Comparison_Array.append(numpy.argmin(my_result_list))
 
Comparison_Array=numpy.array(Comparison_Array)   

count=0
for i in range(len(Comparison_Array)):
    if(int(Actual_Results[i]-Comparison_Array[i])!=0):
        count=count+1

print(len(Test_List))
print(count)
Accuracy=((float(len(Test_List))-float(count))/len(Test_List))*100
print("Accuracy=",Accuracy)
