
from cv2 import FONT_HERSHEY_PLAIN, FONT_HERSHEY_SIMPLEX, cv2
import numpy as np
import os
import imutils
import time
import mediapipe as mp


videoCapture=cv2.VideoCapture(0) 

face_cascade= cv2.CascadeClassifier("C:\\Users\\shini\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
noise=cv2.CascadeClassifier("C:\\Users\\shini\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

mpDraw= mp.solutions.drawing_utils
mpFaceMesh= mp.solutions.face_mesh
faceMesh= mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec= mpDraw.DrawingSpec(thickness=1, circle_radius=1)


while True:

    answer, camera= videoCapture.read()

    """"
    previousTime=0
    currentTime= time.time()

    fps= 1/(currentTime-previousTime)
    previousTime= currentTime

    cv2.putText(camera, f"FPS: {int(fps)}", (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
    """

    if answer==False:
        break
    
    camera= imutils.resize(camera, width=640)

    cameraRGB= cv2.cvtColor(camera, cv2.COLOR_BGR2RGB)
    result= faceMesh.process(cameraRGB)
    grayScale= cv2.cvtColor(camera, cv2.COLOR_BGR2GRAY)
    idCapture=grayScale.copy()
    face= noise.detectMultiScale(grayScale,1.3,5)

    for(x,y,w,h) in face:

        cv2.rectangle(camera, (x,y), (x+w, y+h), (255,0,0), 2)
        faceCaptured= idCapture[y:y+w, x:x+h]
        faceCaptured= cv2.resize(faceCaptured, (160,160), interpolation=cv2.INTER_CUBIC)

        if result.multi_face_landmarks:
            for faceLandmarks in result.multi_face_landmarks:
                mpDraw.draw_landmarks(camera, faceLandmarks, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)

                for landmark in faceLandmarks.landmark:
                    
                    ih, iw, ic = camera.shape
                    x,y = int(landmark.x*iw), int(landmark.y*ih)
                    print("x=",x, " y=", y)

    cv2.imshow("Stream", camera)

    if cv2.waitKey(1) == ord("q"):

        break

videoCapture.release()

cv2.destroyAllWindows()


