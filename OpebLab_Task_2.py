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

def Convolution (img,filter):

    return cv.filter2D(img,-1,filter)

def Median_Filter (img,filtersize=3):

    r,c = np.shape(img)

    pad = int(np.floor(filtersize/2))

    median_img = np.zeros((int(r-pad),int(c-pad)),dtype=np.uint8)

    for i in range(pad,r-pad):
        for j in range(pad,c-pad):
            chunk = img[i-pad:i+pad+1,j-pad:j+pad+1]
            chunk_array = np.ravel(chunk)
            np.sort(chunk_array)
            median_img[i,j]=int(np.median(chunk_array))

    return median_img

img1 = np.array(cv.imread('2.tif',0),dtype=np.uint8)

Final_img = cv.medianBlur(img1,9)

##Gaussian = np.array(((1/273, 4/273,7/273, 4/273, 1/273),
##                (4/273,16/273,26/273,16/273,4/273),
##                (7/273,26/273,41/273,26/273,7/273),
##                (4/273,16/273,26/273,16/273,4/273),
##                (1/273, 4/273,7/273, 4/273, 1/273)),dtype=np.float32)
##
####Median1 = Median_Filter(img1,3)
##
##LaplacianMask = np.array(((-1,-1, -1),
##                            (-1, 8, -1),
##                            (-1,-1, -1)),dtype=np.float32)
##
##Filtered_img = Convolution(img1, Gaussian)
##
##Filtered_img1 = Convolution(img1, LaplacianMask)
##
##Final_img = Filtered_img + Filtered_img1
##
##Final_img = Normalize(Final_img)

##AfterLoG = Convolution(img, LoG)

#cv.imshow('Smoothing', Filtered_img)
#cv.imshow('AfterLaplacian', Filtered_img1)
cv.imshow('Final', Final_img)
cv.waitKey(10000)
cv.destroyAllWindows()
#cv.imwrite('AfterAveraging.png', Filtered_img)
#cv.imwrite('AfterLaplacian.png', Filtered_img1)
cv.imwrite('Final.png', Final_img)

