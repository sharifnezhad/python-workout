import cv2
img=cv2.imread('board-origin.bmp',0)
img2=cv2.imread('board-test.bmp',0)
img2=img2[::,::-1]
result=cv2.absdiff(img2,img)
cv2.imwrite('result2.jpg',result)
cv2.imshow('result2',result)
cv2.waitKey()
