import cv2
image=cv2.imread('2.jpg',0)
image2=cv2.imread('22.jpg',0)
result=image//2+image2//2
cv2.imwrite('result.jpg',result)
cv2.imshow('amir',result)
result=image//4+image2//2
cv2.imwrite('result2.jpg',result)
cv2.imshow('amir2',result)
cv2.waitKey()