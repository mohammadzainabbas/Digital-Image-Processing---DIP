import numpy as np, cv2 as cv

def K_Mean_Clustering(img, epsilon=1, k=3):

    r,c=np.shape(img)

    Centeroid_1 = 52;
    Centeroid_2 = 155;
    Centeroid_3 = 240;
    
    New_Centeroid_1 = New_Centeroid_2 = New_Centeroid_3 = 0;

    while(1):
        
        list_1 = [];
        list_2 = [];
        list_3 = [];

        for i in range(r):
            for j in range(c):
                
                dist = [abs(Centeroid_1 - img[i,j]),abs(Centeroid_2 - img[i,j]),abs(Centeroid_3 - img[i,j])]
                dist_index = dist.index(min(dist))

                if(dist_index == 0):
                    list_1.append(img[i,j])
                elif(dist_index == 1):
                    list_2.append(img[i,j])
                else:
                    list_3.append(img[i,j])

        New_Centeroid_1 = int(np.mean(list_1))
        New_Centeroid_2 = int(np.mean(list_2))
        New_Centeroid_3 = int(np.mean(list_3))

        if (abs(New_Centeroid_1 - Centeroid_1)<epsilon and abs(New_Centeroid_2 - Centeroid_2)<epsilon and abs(New_Centeroid_3 - Centeroid_3)<epsilon):
            break;
        else:
            Centeroid_1 = New_Centeroid_1
            Centeroid_2 = New_Centeroid_2
            Centeroid_3 = New_Centeroid_3

    img1 = np.copy(img)

    list_1 = np.unique(list_1)
    list_2 = np.unique(list_2)
    list_3 = np.unique(list_3)

    for i in range(len(list_1)):
        img1[img1 == list_1[i]] = 0

    for i in range(len(list_2)):
        img1[img1 == list_2[i]] = 128

    for i in range(len(list_3)):
        img1[img1 == list_3[i]] = 255

    
    return img1
    

img = np.array(cv.imread('Fig01.tif',0),dtype=np.uint8)

Segmentated_img = K_Mean_Clustering(img, epsilon=1, k=3)

cv.imshow('Segmentated Image via K mean clustering', Segmentated_img)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('Segmentated Image via K mean clustering.png', Segmentated_img)