import cv2
img=cv2.imread('board-origin.bmp',0)
img2=cv2.imread('board-test.bmp',0)
result=cv2.subtract(img2,img)
cv2.imwrite('result.jpg',result)
cv2.imshow('result',result)
cv2.waitKey()