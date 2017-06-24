import numpy as np, cv2 as cv

def Median_Max_Min_Filter (img,filtersize=3):

    r,c = np.shape(img)

    pad = int(np.floor(filtersize/2))

    median_img = np.zeros((int(r-pad),int(c-pad)),dtype=np.uint8)
    min_img = np.zeros((int(r-pad),int(c-pad)),dtype=np.uint8)
    max_img = np.zeros((int(r-pad),int(c-pad)),dtype=np.uint8)

    for i in range(pad,r-pad):
        for j in range(pad,c-pad):
            chunk = img[i-pad:i+pad+1,j-pad:j+pad+1]
            chunk_array = np.ravel(chunk)
            np.sort(chunk_array)
            median_img[i,j]=int(np.median(chunk_array))
            max_img[i,j]=int(np.max(chunk_array))
            min_img[i,j]=int(np.min(chunk_array))

    return [median_img, max_img, min_img]



img1 = np.array(cv.imread('Fig01.tif',0))
img2 = np.array(cv.imread('Fig02.tif',0))

[Median1, Max1, Min1] = Median_Max_Min_Filter(img1,3)

[Median2, Max2, Min2] = Median_Max_Min_Filter(img2,15)

cv.imshow('Median Image 1',Median1)
cv.imshow('Max Image 1', Max1)
cv.imshow('Min Image 1', Min1)

cv.imshow('Median Image 2',Median2)
cv.imshow('Max Image 2', Max2)
cv.imshow('Min Image 2', Min2)

cv.waitKey(10000)
cv.destroyAllWindows()

cv.imwrite('Median Image 1.png',Median1)
cv.imwrite('Max Image 1.png', Max1)
cv.imwrite('Min Image 1.png', Min1)

cv.imwrite('Median Image 2.png',Median2)
cv.imwrite('Max Image 2.png', Max2)
cv.imwrite('Min Image 2.png', Min2)
