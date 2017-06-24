import numpy as np, cv2 as cv, matplotlib.pyplot as plt, math

def Histogram(img):

    hist = np.zeros((1,256),dtype = np.int)

    r,c = np.shape(img)

    for i in range(r):
        for j in range(c):
            hist[0,img[i,j]] = hist[0,img[i,j]] + 1

    return hist

def Binary_List_To_Decimal(my_list):
    return int(str(''.join(str(e) for e in my_list)), 2)

def Clockwise__Chunk_To_List(input_list, output_list=[]):
    list_size = len(input_list[0])
    if list_size == 1:
        return output_list
    else:
        for i in range(list_size):
            output_list.append(input_list[0][i])

        for i in range(list_size)[1:]:
            output_list.append(input_list[i][list_size - 1])

        for i in reversed(range(list_size)[:-1]):    
            output_list.append(input_list[list_size - 1][i])

        for i in reversed(range(list_size)[1:-1]):    
            output_list.append(input_list[i][0])

        new_list = list()
        for i in range(list_size - 2):
            new_list.append(input_list[i + 1][1:-1])

        return Clockwise__Chunk_To_List(new_list, output_list)
##
##l = [[2, 3, 5, 9, 10],[ 8, 7, 1, 11, 13],[ 0, 4, 6, 21, 22], [12, 19, 17, 18, 25], [14, 15, 16, 23, 24]]
##output = Clockwise__Chunk_To_List(l)
##
##print ('\nMethod 3:\n',output)

def Threshold_Chunk_To_Binary_List(list_1, t):
    #print(list_1)
    my_list = Clockwise__Chunk_To_List(list_1,[])
    #print(my_list)
    my_list = list(reversed(my_list))
    #print(my_list)
    return [(0,1)[i > t] for i in my_list]

def Local_Binary_Pattern(img):
    boxsize=3
    r,c = np.shape(img)
    pad = int(np.floor(boxsize/2))
    new_img = np.zeros((r,c),dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            if(i>0 and i<r-1 and j>0 and j<c-1):
##                print(i)
##                print(j)
##                if i==1 and j==1:
##                    print((img[0:3,0:3]).tolist())
##                    print(img[1,1])
                threshold = img[i,j]
                my_list = Threshold_Chunk_To_Binary_List((img[i-pad:i+pad+1,j-pad:j+pad+1]).tolist(), threshold)
##                print(my_list)
                new_img[i,j] = Binary_List_To_Decimal(my_list)
            else:
                new_img[i,j] = 0
    return new_img
        
##l = [[2, 3, 5 ],[ 8, 7, 1],[ 0, 4, 6]]
###l=np.array(l)
##print(l)
##print(np.mean(l))
##t = int(math.ceil(np.mean(l)))
##print(t)
##l1=Threshold_Chunk_To_Binary_List(l,t)
##print(l1)
##a = Binary_List_To_Decimal(l1)
##print(a)

img = np.array(cv.imread('image3.png',0))
LBP_img = Local_Binary_Pattern(img)

histogram = Histogram(LBP_img)
bins=8

new_histogram = np.array(np.array_split(histogram.flatten(), bins))
new_histogram = [np.sum(i) for i in new_histogram]
#print(np.array(new_histogram))
#print(histogram)
plt.title('Histogram')
plt.stem(histogram[0])
plt.xlabel('Graylevels 0-255')
plt.ylabel('Frequency')
plt.show()

plt.title('Histogram after Local Binary Pattern')
plt.stem(new_histogram)
plt.xlabel('Graylevels 0-255')
plt.ylabel('Frequency')
plt.show()

cv.imshow('Original Image', img)
cv.imshow('Local Binary Pattern Image', LBP_img)
cv.imwrite('Local Binary Pattern Image1.png', LBP_img)
cv.waitKey()
cv.destroyAllWindows()