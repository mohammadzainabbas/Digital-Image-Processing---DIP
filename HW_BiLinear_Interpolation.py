import numpy as np, cv2 as cv

def BiLinearInterpolation(N):
    
    img = np.array(cv.imread('manner.jpg',1))      #reading image and storing in numpy array
    
    #r,c=np.shape(img)
    #new_img = cv.resize(img,(N*r,N*c), interpolation = cv.INTER_LINEAR)
    img = cv.resize(img,(1000,1000), interpolation = cv.INTER_CUBIC)
    #cv.imshow('Cubic Pic',im)
    cv.imshow('Original Pic',img)
    #cv.imshow('BiLinear Interpolated Pic',new_img)
    cv.imwrite('Manner.png',img)
    #cv.imwrite('BiLinear Interpolated Pic.png',new_img)
    cv.waitKey(10000)
    cv.destroyAllWindows()
    return

upscale_value=int(input('Enter upscale value: '))
BiLinearInterpolation(upscale_value)
