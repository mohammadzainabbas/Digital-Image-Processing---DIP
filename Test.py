import numpy, cv2

img = numpy.zeros([500,500,3])

img[:,:,0] = numpy.ones([500,500])*180/255.0        #Blue
#img[:,:,1] = numpy.ones([500,500])*128/255.0       #Green
#img[:,:,2] = numpy.ones([500,500])*192/255.0       #Red

cv2.imwrite('color_img.jpg', img)
cv2.imshow("image", img);
cv2.waitKey();