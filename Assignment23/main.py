
import cv2
from skimage import transform, img_as_float
import numpy as np
import keyboard

def emoji_face(frame,img,face_det):
    frame = img_as_float(frame)
    for x,y,w,h in face_det:
        img_resize = transform.resize(img, (w,h))
        img = img_as_float(img_resize)
        frame[y:y+h,x:x+w, 0] *= 1 - img_resize[:,:,3]
        frame[y:y+h,x:x+w, 1] *= 1 - img_resize[:,:,3]
        frame[y:y+h,x:x+w, 2] *= 1 - img_resize[:,:,3]
        frame[y:y+h,x:x+w, :] += img_resize[:,:,:3]
    return frame

def emoji_eyes_smile(frame,eye_img,smil_img,face_det):


    
    frame = img_as_float(frame)
    for (x,y,w,h) in face_det:
        roi_gray=frame_gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w,:]
        roi_color2=frame[y:y+h,x:x+w,:]

        eyes=eye_detector.detectMultiScale(roi_gray,1.3,minNeighbors=8)
        for (ex,ey,ew,eh) in eyes:
            # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            eye_resize = transform.resize(eye_img, (ew,eh))
            eye_img = img_as_float(eye_resize)
            roi_color[ey:ey+eh,ex:ex+ew, 0] *= 1 - eye_img[:,:,3]
            roi_color[ey:ey+eh,ex:ex+ew, 1] *= 1 - eye_img[:,:,3]
            roi_color[ey:ey+eh,ex:ex+ew, 2] *= 1 - eye_img[:,:,3]
            roi_color[ey:ey+eh,ex:ex+ew, :] += eye_img[:,:,:3]

        smile=smile_detector.detectMultiScale(roi_gray,1.5,minNeighbors=14)
        for (sx,sy,sw,sh) in smile:
            # cv2.rectangle(roi_color2,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
            smail_resize = transform.resize(smil_img, (sh,sw))
            smil_img = img_as_float(smail_resize)

            roi_color2[sy:sy+sh,sx:sx+sw, 0] *= 1 - smil_img[:,:,3]
            roi_color2[sy:sy+sh,sx:sx+sw, 1] *= 1 - smil_img[:,:,3]
            roi_color2[sy:sy+sh,sx:sx+sw, 2] *= 1 - smil_img[:,:,3]
            roi_color2[sy:sy+sh,sx:sx+sw, :] += smil_img[:,:,:3]
    return frame
def rasterize_face(frame,face_det):

    for (x,y,w,h) in face_det:
        # frame[y:y+h,x:x+w]=cv2.GaussianBlur(frame[y:y+h,x:x+w],((w//2)|1,(h//2)|1),cv2.BORDER_DEFAULT)
        for i in range(y, y + h, 10):
            for j in range(x, x + w, 10):
                frame[i:i + 10, j:j + 10] = frame[i, j]
    return frame

def flipVertical_image(frame):
        flipVertical = cv2.flip(frame, 0)
        return flipVertical

def blur_face(frame,face_dect):
    mask=np.ones((21,21))/441
    for x,y,w,h in face_dect:
        img=frame[y:y+h,x:x+w]
        img=cv2.filter2D(img, -1, mask)
        frame[y:y+h,x:x+w]=img[:,:]
    return frame



        

face_detector=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_detector = cv2.CascadeClassifier("haarcascade_smile.xml")


cap= cv2.VideoCapture(0)
fps= int(cap.get(cv2.CAP_PROP_FPS))

print("This is the fps ", fps)
flag = 0
font = cv2.FONT_HERSHEY_COMPLEX
menu_text='1.emoji face\n2.emogi eyes and lip\n3.Rasterize the image\n4.Rotate the image\nESC'
y0, dy = 50, 4
while True:
    ret,frame=cap.read()

    if keyboard.is_pressed('1'):
        flag=1
    elif keyboard.is_pressed('2'):
        flag=2
    elif keyboard.is_pressed('3'):
        flag = 3
    elif keyboard.is_pressed('4'):
        flag=4
    elif keyboard.is_pressed('5'):
        flag=5
    elif keyboard.is_pressed('Esc'):
        flag=-1
    if ret==False:
        break
    for i, line in enumerate(menu_text.split('\n')):
        y = y0 + i * dy*7
        cv2.putText(frame, line, (10, y),font, 0.5, (0,0,0), 1, cv2.LINE_AA)

    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_detection=face_detector.detectMultiScale(frame_gray)
    if flag==1:
        if cap.isOpened() == False:
                print("Error File Not Found")

        img = cv2.imread("starry-eyed-emoji.png", cv2.IMREAD_UNCHANGED)
        if(img.shape[2] <4):
            print('sorry can\'t mask')
        frame=emoji_face(frame,img,face_detection)
    elif flag==2:
        eye_img = cv2.imread('eye.png', cv2.IMREAD_UNCHANGED)
        smil_img = cv2.imread('smil.png', cv2.IMREAD_UNCHANGED)
        if eye_img.shape[2] < 4 and smil_img.shape[2] < 4:
            print('sorry can\'t mask')
        frame=emoji_eyes_smile(frame,eye_img,smil_img,face_detection)
    elif flag==3:
        frame=rasterize_face(frame,face_detection)
    elif flag==4:
        frame=flipVertical_image(frame)
    elif flag==5:
        frame=blur_face(frame,face_detection)
    elif flag==-1:
        exit()




    cv2.imshow('frame',frame)
    cv2.waitKey(10)
