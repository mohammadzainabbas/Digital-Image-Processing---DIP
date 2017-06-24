import numpy as np, cv2 as cv

def IntensityLevelResolution(N,size):
    
    img = np.array(cv.imread('gradient.png',0))      #reading image and storing in numpy array
    
    new_img = cv.resize(img,(size,size))              #Resizing image
    
    r,c = np.shape(new_img)

    div = int(256/N)
    
    for i in range(r):
        for j in range(c):
            
            levels=int((new_img[i,j])/div)
            
            new_img[i,j] = levels*div

    return new_img

size=int(input('Enter image size: '))

new_img_16 = IntensityLevelResolution(16,size)
new_img_4 = IntensityLevelResolution(4,size)
new_img_1 = IntensityLevelResolution(2,size)

cv.imshow('New image 16',new_img_16)
cv.imwrite('Intensity level - 16.png',new_img_16)
cv.imshow('New image 4',new_img_4)
cv.imwrite('Intensity level - 4.png',new_img_4)
cv.imshow('New image 1',new_img_1)
cv.imwrite('Intensity level - 2.png',new_img_1)

cv.waitKey(10000)
cv.destroyAllWindows()
    
