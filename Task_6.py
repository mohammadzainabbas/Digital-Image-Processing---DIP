import numpy, cv2

def ColorCornerBoxGenerator(size=500):
    img = numpy.zeros([size,size,3])                #declaring numpy array of zeros of given size
    box_size=int(size/8)                            #box size is 1/8th of the total size
    w=int(size-box_size);                           #difference of size and box size

    img [0:size,0:size] = 255                       #White box
    img [0:box_size,0:box_size] = (0,0,255)         #Red box at top left corner
    img [0:box_size,w:size] = (0,255,0)             #Green box  at top right corner
    img [w:size,0:box_size] = (255,0,0)             #Blue box   at bottom left corner
    img [w:size,w:size] = (0,0,0)                   #Black box  at bottom right corner

    cv2.imshow("Colored Corner Box", img);          #display the resultant image
    cv2.waitKey(100000)                             
    cv2.destroyAllWindows()
    cv2.imwrite('Color_Corner_Box.png', img)
    return

size=int(input('Enter image size: '))
ColorCornerBoxGenerator(size)