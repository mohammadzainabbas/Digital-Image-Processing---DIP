import numpy as np, cv2 as cv

def Check_Value(value, epsilon, seed):
    return seed if (abs(value - seed) <= epsilon) else 0

def Region_Growing(img, seed = 249, epsilon = 5):

    r,c=np.shape(img)

    new_img = np.copy(img)

    while(1):
        for i in range(r):
            for j in range(c):
                img[img == Check_Value(img, epsilon = 5, seed = 249)] = 249

        if (abs(new_img - img) == 0):
            break;
        else:
            new_img = img  
        
    return img
    

img = np.array(cv.imread('Fig01.tif',0),dtype=np.uint8)

Segmentated_img = Region_Growing(img, seed = 249, epsilon = 5)

cv.imshow('Segmentated Image via Region Growing', Segmentated_img)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('Segmentated Image via Region Growing.png', Segmentated_img)

