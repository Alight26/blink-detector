import cv2 as cv 
import mediapipe as mp 
import numpy as np 

face_casc = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv.VideoCapture(1)

while True:
    ret, img = cam.read()


    cv.imshow('img', img)

    cv.waitKey(40)