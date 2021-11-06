import cv2
img=cv2.imread('a.tif',0)
img2=cv2.imread('b.tif',0)
result=img2-img
cv2.imwrite('result2.jpg',result)
cv2.imshow('result2',result)
cv2.waitKey()