import numpy as np, cv2 as cv

#To break multiple nested lists/sublists into one list
def Flatten(a, ClassTypes=(list, tuple)):
    ClassType = type(a)
    if ClassType == int:
        return a
    else:
        a = list(a)
        i = 0
        while i < len(a):
            while isinstance(a[i], ClassTypes):
                if not a[i]:
                    a.pop(i)
                    i -= 1
                    break
                else:
                    a[i:i + 1] = a[i]
            i += 1
        a.sort()
        return ClassType(a)

#Connected Component Analysis using 4 connectivity -- To determine how many objects are there in the picture
def ConnectedComponentAnalysis():

    #img = np.array(((1,1,1,1),(1,255,255,255),(1,255,255,255),(1,255,255,1)))       #For testing
    
    img = np.array(cv.imread('cc.png',0))      #reading image and storing in numpy array
##    cv.imshow('Pic',img)
##    cv.waitKey(10000)
##    cv.destroyAllWindows()
    r,c = np.shape(img)         #to get dimensions of my image

##    for i in range(r):
##        for j in range(c):
##            print(img[i,j])
##            print(" ")
##        print("\n")

    labelling_img = np.zeros((int(r),int(c)),dtype=np.uint8)      #creating image of zeros of size 501x501

    label_table = [];           #declaring label table
    label = int(0)              #label counter

    #First Pass
    for i in range(r):
        for j in range(c):

            if (img[i,j] != 1):
                #print(str(i)+','+str(j))

                if(i==0):
                    if(j==0):
                        LeftPixel = 0
                        UpperPixel = 0
                    else:
                        UpperPixel = 0
                        LeftPixel = img [0,j-1]
                elif (j==0):
                    UpperPixel = img [i-1,0]
                    LeftPixel = 0
                else:
                    UpperPixel = img [i-1,j]
                    LeftPixel = img [i,j-1]

                if (UpperPixel == LeftPixel == 1):
                    
                    label=label+1
                    labelling_img [i,j] = label
                    label_table.append(label)
                    
                elif (UpperPixel == 255 and LeftPixel == 255):

                    UpperLabel = labelling_img [i-1,j]
                    LeftLabel = labelling_img [i,j-1]

                    if(UpperLabel == LeftLabel):

                        labelling_img[i,j] = UpperLabel

                    else:
                        #UpperPixel is prefered
                        labelling_img [i,j] = UpperLabel

                        #Index = label_table.index(UpperLabel)       #Check
                        Index = label_table.index(label_table[UpperLabel-1])    #Index = UpperLabel-1

                        temp = []
                        temp.append(label_table[Index])
                        #temp.append(label_table[UpperLabel-1])      #Could work -- don't need index

                        temp.append(LeftLabel)

                        temp = Flatten(temp)
                        #temp.sort()

                        label_table.pop(Index)
                        
##                        for label in range(len(label_table)):
##                            if (label == LeftLabel):
##                                label_table.remove(label)

                        if LeftLabel in label_table:            #Error - If leftlabel exists, remove it from label table
                            label_table.remove(LeftLabel)
                        label_table.insert(Index,temp)

                else:

                    if(UpperPixel == 255):
                        labelling_img [i,j] = labelling_img [i-1,j]
                    else:
                        labelling_img [i,j] = labelling_img [i,j-1]

    #Second Pass
            
    temp=[]
    for k in range(len(label_table)):

        if type(label_table[k])==list:
            temp.append(np.unique(Flatten(label_table[k])).tolist())
        else:
            temp.append(label_table[k])
            label_table.pop(k)
            label_table.insert(k,temp[k])
                

    for k in range(len(label_table)):
        if type(label_table[k]) == list:
            LowestElement = label_table[k][0]
            label_table[k] = LowestElement          #Removing higher entries in that cell
##             for m in range(1,len(label_table[k])):
##            
##                 for
            


                

            

    return label_table

l_table=[];
l_table=ConnectedComponentAnalysis()
print(l_table)
print("\n"*5)
print("Total objects are " + str(len(l_table)))