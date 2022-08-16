
from cv2 import cv2
import numpy as np
import os
import imutils


videoCapture=cv2.VideoCapture(0) 

face_cascade= cv2.CascadeClassifier("C:\\Users\\shini\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

noise=cv2.CascadeClassifier("C:\\Users\\shini\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

id=0

while True:
    answer, camera= videoCapture.read()
    if answer==False:break
    camera= imutils.resize(camera, width=640)

    grayScale= cv2.cvtColor(camera, cv2.COLOR_BGR2GRAY)
    idCapture=camera.copy()
    face= noise.detectMultiScale(camera,1.3,5)

    for(x,y,w,h) in face:

        cv2.rectangle(camera, (x,y), (x+w, y+h), (255,0,0), 2)
        faceCaptured= idCapture[y:y+w, x:x+h]
        faceCaptured= cv2.resize(faceCaptured, (160,160), interpolation=cv2.INTER_CUBIC)

    cv2.imshow("Stream", camera)

    if cv2.waitKey(1) == ord("q"):

        break

videoCapture.release()

cv2.destroyAllWindows()
