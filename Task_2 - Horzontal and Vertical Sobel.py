import numpy as np, cv2 as cv

def Convolution (img,filter):

    return cv.filter2D(img,-1,filter)

img = np.array(cv.imread('Fig03.tif',0))

HorizontalSobel = np.array(((-1,-2,-1),
                            (0, 0, 0),
                            (1, 2, 1)))

VertialSobel = np.array(((-1, 0, 1),
                         (-2, 0, 2),
                         (-1, 0, 1)))

HS_img = Convolution(img, HorizontalSobel)
VS_img = Convolution(img, VertialSobel)

Final_img = HS_img + VS_img

cv.imshow('Horizontal Sobel',HS_img)
cv.imshow('Vertial Sobel', VS_img)
cv.imshow('Final Image', Final_img)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('Horizontal Sobel.png',HS_img)
cv.imwrite('Vertial Sobel.png', VS_img)
cv.imwrite('Sobel Final Image.png', Final_img)