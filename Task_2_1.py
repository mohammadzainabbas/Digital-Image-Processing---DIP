import numpy as np
import cv2 as cv

img = np.array(cv.imread('sad.png',0))  #reading image in numpy array

dim=np.shape(img)
print(dim)

newimg1 = np.zeros((int(dim[0]/2),int(dim[1])),dtype=np.uint8)
newimg2 = np.zeros((int(dim[0]/2),int(dim[1])),dtype=np.uint8)
final = np.zeros((int(dim[0]),int(dim[1])),dtype=np.uint8)

for i in range(int(dim[0]/2)):
    for j in range(int(dim[1])):
        newimg1[i,j] = img[i,j]
        
for i in range(int(dim[0]/2)):
    for j in range(int(dim[1])):
        newimg2[i,j] = img[int(dim[0]/2)-i,j]

##for i in range(int(dim[0])):
##    for j in range(int(dim[1])):
##        final[i,j] = newimg1[i,j]
##        else:
##            final[i,j] = newimg2[i,j]

final=np.concatenate((newimg1,newimg2),axis=0)

cv.imshow('New image1',newimg1)
cv.imshow('New image2',newimg2)
cv.imshow('Final',final)
cv.waitKey(10000)
cv.destroyAllWindows()
#cv.imwrite('Flipped from center.png',final)

        
        
