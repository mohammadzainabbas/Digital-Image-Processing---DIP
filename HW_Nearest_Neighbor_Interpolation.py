import numpy as np, cv2 as cv

def NearestNeighborInterpolation(N):
    
    img = np.array(cv.imread('sad.png',0))      #reading image and storing in numpy array
    
    #L=int(N-1)
    r,c=np.shape(img)
    
    new_img = np.zeros((int(r*N),int(c*N)),dtype=np.uint8)

        #new_img[0:r-1:L,0:c-1:L] = img[:,:]
            
##
##    for i in range(r):
##        
##        for j in range(c):
##            temp = img[i,j]
##            for k in range(L):
##                new_img[i*k,j*k] = temp

    for i in range(1,r):
        for j in range(1,c):
            new_img[((i-1)*N)+1:i*N+1,((j-1)*N)+1:j*N+1] = img [i,j]

    cv.imshow('Original Pic',img)
    cv.imshow('Interpolated Pic',new_img)
    cv.imwrite('Nearest Neighbor Interpolated Pic.png',new_img)
    cv.waitKey(10000)
    cv.destroyAllWindows()
    return

upscale_value=int(input('Enter upscale value: '))
NearestNeighborInterpolation(upscale_value)