import numpy as np, cv2 as cv

##def Check_Value(value, epsilon, seed):
##    return 1 if (abs(value - seed) <= epsilon) else 0

def Region_Growing(img, seed = 249, epsilon = 5):

    r,c=np.shape(img)

    while(1):
        new_img = np.copy(img)

        for i in range(r):
            for j in range(c):
                if(img[i,j] == seed):
                    if(i>0 and i<r-1 and j>0 and j<c-1):
                        if(np.abs(img[i-1,j-1] - seed) <= epsilon):
                            img[i-1,j-1] = seed
                        elif(np.abs(img[i-1,j] - seed) <= epsilon):
                            img[i-1,j] = seed
                        elif(np.abs(img[i-1,j+1] - seed) <= epsilon):
                            img[i-1,j+1] = seed
                        elif(np.abs(img[i,j-1] - seed) <= epsilon):
                            img[i,j-1] = seed
                        elif(np.abs(img[i,j+1] - seed) <= epsilon):
                            img[i,j+1] = seed
                        elif(np.abs(img[i+1,j-1] - seed) <= epsilon):
                            img[i+1,j-1] = seed
                        elif(np.abs(img[i+1,j] - seed) <= epsilon):
                            img[i+1,j] = seed
                        elif(np.abs(img[i+1,j+1] - seed) <= epsilon):
                            img[i+1,j+1] = seed
        if(np.max(new_img - img) == 0):
            break;

    img[img != seed] = 0
    img[img == seed] = 255
    return img
    

img = np.array(cv.imread('Fig01.tif',0),dtype=np.uint8)

seed = int(input('Enter seed value: '))

Segmentated_img = Region_Growing(img, seed = 249, epsilon = 5)

cv.imshow('Segmentated Image via Region Growing', Segmentated_img)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('Segmentated Image via Region Growing.png', Segmentated_img)
