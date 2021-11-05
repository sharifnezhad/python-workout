import cv2
import numpy as np
images=[[None for i in range(5)] for j in range(4)]

for i in range(4):
    for j in range(5):
        images[i][j]=cv2.imread(str(i+1)+'/'+str(i+1)+'.jpg',0)
image_without_noise=[0 for i in range(4)]
for i in range(4):
    for j in images[i]:
        image_without_noise[i]+=j//5
full_image=np.zeros((2000,2000),dtype=np.uint8)
full_image[0:1000,0:1000]=image_without_noise[0]
full_image[0:1000,1000:2000]=image_without_noise[1]
full_image[1000:2000,0:1000]=image_without_noise[2]
full_image[1000:2000,1000:2000]=image_without_noise[3]
cv2.imwrite('result2.jpg',full_image)
cv2.imshow('amir',full_image)
cv2.waitKey()
