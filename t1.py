import numpy as np, cv2 as cv

def region(img, seed, e):

    row,column=np.shape(img)

    while(1):
        img1 = np.copy(img)

        for i in range(row):
            for j in range(column):
                if(img[i,j] == seed):
                    if(i>0 and i<row-1 and j>0 and j<column-1):
                        if(np.abs(img[i-1,j-1] - seed) <= e):
                            img[i-1,j-1] = seed
                        elif(np.abs(img[i-1,j] - seed) <= e):
                            img[i-1,j] = seed
                        elif(np.abs(img[i-1,j+1] - seed) <= e):
                            img[i-1,j+1] = seed
                        elif(np.abs(img[i,j-1] - seed) <= e):
                            img[i,j-1] = seed
                        elif(np.abs(img[i,j+1] - seed) <= e):
                            img[i,j+1] = seed
                        elif(np.abs(img[i+1,j-1] - seed) <= e):
                            img[i+1,j-1] = seed
                        elif(np.abs(img[i+1,j] - seed) <= e):
                            img[i+1,j] = seed
                        elif(np.abs(img[i+1,j+1] - seed) <= e):
                            img[i+1,j+1] = seed
        if(np.max(img1 - img) == 0):
            break;

    img[img != seed] = 0
    img[img == seed] = 255
    return img
    

img = np.array(cv.imread('Fig01.tif',0),dtype=np.uint8)

final = region(img, seed = 249, e = 5)

cv.imshow('result', final)
cv.waitKey(10000)
cv.destroyAllWindows()