import numpy as np, cv2 as cv

def Normalize(img):
    img_1=np.array(img,dtype=np.uint8)
    r,c = np.shape(img)
    img_min = np.min(img)
    img_max = np.max(img)
    #To normalize image
    for i in range(r):
        for j in range(c):
            img_1[i,j] = 255*((img[i,j] - img_min)/(img_max-img_min))
    return img_1

def Min_Filter (img,filtersize=3):

    r,c = np.shape(img)

    pad = int(np.floor(filtersize/2))

    min_img = np.zeros((int(r-pad),int(c-pad)),dtype=np.uint8)

    for i in range(pad,r-pad):
        for j in range(pad,c-pad):
            chunk = img[i-pad:i+pad+1,j-pad:j+pad+1]
            chunk_array = np.ravel(chunk)
            np.sort(chunk_array)
            min_img[i,j]=int(np.min(chunk_array))

    return min_img

img1 = np.array(cv.imread('1.tif',0))
Min1 = Min_Filter(img1,31)

cv.imshow('Min Image 1', Min1)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('Min Image 1.png', Min1)
