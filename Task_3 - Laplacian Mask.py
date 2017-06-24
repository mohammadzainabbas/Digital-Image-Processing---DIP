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

img = np.array(cv.imread('Fig03.tif',0),dtype=np.float32)

LaplacianMask = np.array(((-1,-1, -1),
                            (-1, 8, -1),
                            (-1,-1, -1)),dtype=np.float32)

Filtered_img = Convolution(img, LaplacianMask)

Final_img = Filtered_img + img

Final_img = Normalize(Final_img)

cv.imshow('Orginal Image', img)
cv.imshow('Laplacian Filtered Image',Filtered_img)
cv.imshow('Final Image', Final_img)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('Laplacian Filtered Image.png',Filtered_img)
cv.imwrite('Sharpened Image after Laplacian Filter.png', Final_img)