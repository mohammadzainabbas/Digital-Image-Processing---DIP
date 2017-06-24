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

def FourierTransformViaBuiltInFunction(img):
    
    #img = cv.resize(img, (128,128))
    
    img = 20*np.log(np.abs(np.fft.fftshift(np.fft.fft2(img))))

    return img

def FourierTransform(img):
    img = cv.resize(img, (64,64))
         
    r,c = np.shape(img)
    for x in range(r):
        for y in range(c):
            img[x,y] = img[x,y]*pow((-1),(x+y))

    DFT = np.zeros((r,c),dtype=np.double)
    M=int(r)
    N=int(c)

    for u in range(r):
        for v in range(c):
            for x in range(r):
                for y in range(c):
                    DFT[u,v] = DFT[u,v] + np.abs(img[x,y]*np.exp(-1j*2*np.pi*(((u*x)/M) + ((v*y)/N))))

    #DFT = 20*np.log(np.abs(np.fft.fftshift(DFT)))
    
    cv.normalize(DFT,DFT,0, 255, cv.NORM_MINMAX, -1)

    return 20*np.log(np.abs(np.uint8(DFT)))


img = np.array(cv.imread('Fig01.tif',0), dtype = np.double)
DFT = FourierTransform(img)
img_1 = FourierTransformViaBuiltInFunction(img)

cv.imshow('DFT',DFT)
cv.imshow('DFT via built-in Function', img_1)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('DFT by built-in.png',img_1)
cv.imwrite('DFT.png',DFT)
