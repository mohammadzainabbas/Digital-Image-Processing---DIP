import numpy as np, cv2 as cv

def EuclidianDistanceMap(img):

    r,c = np.shape(img)

    half_r = int(r/2)
    half_c = int(c/2)
    
    for i in range(r):
        for j in range(c):

            distance = int((int((half_r - i)**2)+int((half_c - j)**2))**(1/2))
            if distance > 255:
                img[i,j] = 255
            else:
                img[i,j] = distance

    return img

img = np.zeros((int(501),int(501)),dtype=np.uint8)      #creating image of zeros of size 501x501

img = EuclidianDistanceMap(img)

cv.imshow('Distance Map',img)
cv.imwrite('Euclidian Distance Map.png',img)
cv.waitKey(10000)
cv.destroyAllWindows()
