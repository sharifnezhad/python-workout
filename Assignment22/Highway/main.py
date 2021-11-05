import cv2
image=[0 for i in range(15)]
for i in range(15):
    image[i]=cv2.imread(f"h{i}.jpg",0)
result=image[0]//15
for i in range(1,15):
    image[i]=image[i]//15
    result+=image[i]
# result=result//15
# result=result*255
cv2.imwrite('result.jpg',result)
cv2.imshow('mask',result)
cv2.waitKey()