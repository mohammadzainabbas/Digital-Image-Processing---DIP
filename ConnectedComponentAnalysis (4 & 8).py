import numpy as np, cv2 as cv

#To assign label to current pixel based upon the label of the neighboring pixel
def AssignLabel(Left,Upper,LeftDiagonal=0,RightDiagonal=0):    #Neighboring pixel labels values
    
    if(Left!=0):                                        #Left pixel --> highest priority
        return Left                                     #Return the label of the left pixel, if not zero

    elif(LeftDiagonal!=0):                              #If left pixel is zero, check left diagonal pixel (in case of 8 connectivity)
        return LeftDiagonal

    elif(Upper!=0):                                     
        return Upper                                    

    elif(RightDiagonal!=0):
        return RightDiagonal

    return 0

#To find the index of a value in a list or sublist
def FindIndex(my_list,value):
    index=-1                                    #Setting index's default value
    for i in range(my_list.__len__()):          #Loop till the length of the list
        if(my_list[i].count(value)>0):          #If that value occurs in list once or multiple times
            index = i                           #Storing index in variable 'index'
            break
    return index                                #Returning index value

def ConnectedComponentAnalysis(img, Connectivity=4):
    
    r,c = np.shape(img)         #to get dimensions of my image
    labelling_img = np.zeros((int(r),int(c)),dtype=int)      #creating image of zeros of size 501x501
    
    label_table=[]
    label=1
    
    for i in range(1,r):
        for j in range(1,c):
            if (img[i,j]==255):
                
                pixelLabel = 0

                if(Connectivity == 8):
                    pixelLabel = AssignLabel(labelling_img[i,j-1],labelling_img[i-1,j],labelling_img[i-1,j-1],labelling_img[i-1,j+1])
                else:
                    pixelLabel = AssignLabel(Left=labelling_img[i,j-1],Upper=labelling_img[i-1,j])

                if(pixelLabel == 0):
                    pixelLabel = label
                    label_table.append([pixelLabel])
                    label = label + 1

                labelling_img[i,j] = pixelLabel

                SecondPass(labelling_img[i-1,j],labelling_img[i,j-1],label_table)

    SortSublists(label_table)
    
    labelling_img = AssignMinimumLabel(labelling_img,label_table)

    return (labelling_img,label_table)

#For second pass - Removing multiple labels of the same object 
def SecondPass(LeftPixelLabel,UpperPixelLabel,label_table):         #Passing left and upper pixel's labels and the labelling table list
    
    if(UpperPixelLabel!=0 and LeftPixelLabel!=0 and UpperPixelLabel!=LeftPixelLabel):       #If upper and left pixel labels aren't same and aren't zero
        
        UpperLabelIndex=FindIndex(label_table,UpperPixelLabel)              #Finding index of upper pixel
        
        LeftLabelIndex=FindIndex(label_table,LeftPixelLabel)                #Finding index of left pixel
        
        if(UpperLabelIndex!=LeftLabelIndex):                        #If both indexes aren't same, update the list
            
            UpdateList(label_table,UpperLabelIndex,LeftLabelIndex)      #Popping left label sublist and appending it to upper label sublist in the labelling table list
            
    return
    
#For seocnd pass - Removing one element (sublist) and copying its contents to another element (sublist)     
def UpdateList(label_table, index1, index2):              #Passing labelling table list and both indexes; We want to append index2-value(s) ---> index1-value(s)
    
    while(label_table[index2].__len__()>0):             #Loop till the length of index2 sublist
        
        label_table[index1].append(label_table[index2].pop())       #Pop the value from index2 sublist and append it in the index1 sublist
        
    label_table.__delitem__(index2)                 #To remove the empty sublist at index2 location - list.__delitem__(index_value) deletes that index element; whether is it an element or a sublist

    return
    

#To sort all the sublists in a list
def SortSublists(my_list):          #Passing my list to be sort
    
    for i in range(1,my_list.__len__()):        #For looping till the length of list
        
        my_list[i].sort()                       #Sorting all sublists

        return

#Last step of 2nd pass - assigning minimum label to every object
def AssignMinimumLabel(labelling_img,label_table):      #Passing labelling image and the labelling table list
    
    r,c = np.shape(labelling_img)               #to know dimensions of labelling image
    newimg = np.zeros((r,c),dtype=np.uint8)          #2D array of dimensions same as labelling image and of datatype np.uint8 

    #Nested looping to acess every pixel location 
    for i in range(r):
        for j in range(c):
            
            if(labelling_img[i,j] != 0):        #if we have some label
                
                newimg[i,j] = (FindIndex(label_table, labelling_img[i,j]) + 1) * 40         #Multiplying labelling table list index values with 40

    return newimg

def LabelDetectSegment(img, Connectivity=8):
    n1,l1=ConnectedComponentAnalysis(img, Connectivity)
    res=AssignMinimumLabel(n1,l1)
    return res,l1
    
img = np.array(cv.imread('wb.png',0))
x,l1=ConnectedComponentAnalysis(img, Connectivity=4)
cv.imshow('Image',x)
cv.waitKey(10000)
cv.destroyAllWindows()
print('Total objects are: ' + str(len(l1)))

