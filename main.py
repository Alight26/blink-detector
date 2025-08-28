import cv2 as cv 
import mediapipe as mp 
import numpy as np 

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv.VideoCapture(1)

while True:
    ret, img = cam.read()
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = img_gray[x:x+w, y:y+h]
        roi_color = img[x:x+w, y:y+h]

    



    cv.imshow('img', img)

    cv.waitKey(40)