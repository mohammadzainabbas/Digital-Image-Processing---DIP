import matplotlib.pyplot as plt, cv2 as cv, numpy as np

def Histogram(img):

    hist = np.zeros((1,256),dtype = np.int)

    r,c = np.shape(img)

    for i in range(r):
        for j in range(c):
            hist[0,img[i,j]] = hist[0,img[i,j]] + 1

    return hist

def PDF(img,hist):

    pdf = np.zeros((1,256),dtype=np.float)
    r, c = np.shape(img)
    
    for j in range(256):
            pdf[0,j]=hist[0,j]/(r*c)
            
    return pdf

def CDF(pdf):

    cdf = np.zeros((1,256),dtype=np.float)
    r, c = np.shape(pdf)
    
    for i in range(256):
        cdf[0,i]=cdf[0,i-1]+pdf[0,i]

    return cdf

def TransferFunction(cdf,img):

    r,c = np.shape(img)

    e_img = np.zeros((r,c),dtype=np.uint8)
    transfer = 255*cdf

    for i in range(r):
        for j in range(c):
            e_img[i,j] = transfer[0,img[i,j]]

    return e_img
    
def Normalize(img):
    r,c = np.shape(img)

    img_min = np.min(img)

    #To normalize image
    for i in range(r):
        for j in range(c):
            img[i,j] = img[i,j] - img_min
            
    img_max = np.max(img)
    for i in range(r):
        for j in range(c):
            img[i,j] = 255*(img[i,j]/img_max)
    return img

def Display():

    img = np.array(cv.imread('fig01.tif',0))

    r,c = np.shape(img)
 
    histogram = Histogram(img)

    plt.title('Histogram')
    plt.stem(histogram[0])
    plt.xlabel('Graylevels 0-255')
    plt.ylabel('Frequency')
    plt.show()
    
    pdf = PDF(img,histogram)

    plt.title('PDF')
    plt.stem(pdf[0])
    plt.xlabel('Graylevels 0-255')
    plt.ylabel('Relative Frequency')
    plt.show()

    cdf = CDF(pdf)

    plt.title('CDF')
    plt.stem(cdf[0])
    plt.xlabel('Graylevels 0-255')
    plt.ylabel('Cumulative Frequency')
    plt.show()

    transfer = 255*cdf
    plt.title('Transfer Function')
    plt.stem(transfer[0])
    plt.xlabel('Graylevels 0-255')
    plt.ylabel('Intensities Values')
    plt.show()
    
    enhanced = TransferFunction(cdf,img)
    cv.imshow('Enhanced Image',enhanced)
    cv.imwrite('Enhanced Image.png',enhanced)
    cv.waitKey()
    cv.destroyAllWindows()

    return

Display()
