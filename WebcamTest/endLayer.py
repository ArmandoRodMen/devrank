import cv2 as cv2
import numpy as np
import os
import imutils
import mediapipe as mp

id=0

dataPath= "C:/Users/shini/Desktop/PythonFaceRec/WebcamTest/faceLibrary"
dataList= os.listdir(dataPath)

EigenFaceRecognizer=cv2.face.EigenFaceRecognizer_create()
EigenFaceRecognizer.read("C:\\Users\\shini\\Desktop\\PythonFaceRec\\Training_EigenRecognizer.xml")

noise= cv2.CascadeClassifier("C:\\Users\\shini\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
camera= cv2.VideoCapture(0)

mpDraw= mp.solutions.drawing_utils
mpFaceMesh= mp.solutions.face_mesh
faceMesh= mpFaceMesh.FaceMesh(max_num_faces=1)
drawSpec= mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True:
    answer, capture= camera.read()
    if answer == False:
        break
    capture=imutils.resize(capture, width= 640)
    cameraRGB= cv2.cvtColor(capture, cv2.COLOR_BGR2RGB)
    resultRGB= faceMesh.process(cameraRGB)
    grayScale= cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)
    idCapture= grayScale.copy()
    face= noise.detectMultiScale(grayScale,1.3,5)
    faceArray = []

    xpixel = []
    ypixel = []
    list = []


    for(x,y,w,h) in face:

        faceCaptured= idCapture[y:y+w, x:x+h]
        faceCaptured= cv2.resize(faceCaptured, (160,160), interpolation=cv2.INTER_CUBIC)
        result= EigenFaceRecognizer.predict(faceCaptured)
        cv2.putText(capture, '{}'.format(result), (x,y-5), 1, 1.3, (0,255,0), 1, cv2.LINE_AA)

        if result[1]<9000:
            cv2.putText(capture, '{}'.format(dataList[result[0]]), (x,y-25), 1, 1.3, (0,255,0), 1, cv2.LINE_AA)
            cv2.rectangle(capture, (x,y), (x+h, y+w), (0,255,0), 2)

            if resultRGB.multi_face_landmarks:
                for faceLandmarks in resultRGB.multi_face_landmarks:
                    mpDraw.draw_landmarks(capture, faceLandmarks, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)

                for id, landmark in enumerate(faceLandmarks.landmark):
                    
                    ih, iw, ic = capture.shape
                    x,y = int(landmark.x*iw), int(landmark.y*ih)

                    xpixel.append(x)
                    ypixel.append(y)
                    list.append([id, x, y])

                    if len(list) == 468:

                        #Right Eyebrow
                        x1, y1 = list[65][1:]
                        x2, y2 = list[158][1:]
                        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                        cv2.line(capture, (x1, y1), (x2, y2), (0,255,0), 2)
                        cv2.circle(capture, (x1, y1), 2, (0,255,0), cv2.FILLED)
                        cv2.circle(capture, (x2, y2), 2, (0,255,0), cv2.FILLED)
                        cv2.circle(capture, (cx, cy), 2, (0,255,0), cv2.FILLED)

                        #Test
                        x1, y1 = list[10][1:]
                        x2, y2 = list[152][1:]
                        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                        cv2.line(capture, (x1, y1), (x2, y2), (0,255,0), 2)
                        cv2.circle(capture, (x1, y1), 2, (0,255,0), cv2.FILLED)
                        cv2.circle(capture, (x2, y2), 2, (0,255,0), cv2.FILLED)
                        cv2.circle(capture, (cx, cy), 2, (0,255,0), cv2.FILLED)
                        #//////////////////////////////////////////////////////
                        x1, y1 = list[234][1:]
                        x2, y2 = list[454][1:]
                        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                        cv2.line(capture, (x1, y1), (x2, y2), (0,255,0), 2)
                        cv2.circle(capture, (x1, y1), 2, (0,255,0), cv2.FILLED)
                        cv2.circle(capture, (x2, y2), 2, (0,255,0), cv2.FILLED)
                        cv2.circle(capture, (cx, cy), 2, (0,255,0), cv2.FILLED)
                        #//////////////////////////////////////////////////////
                        x1, y1 = list[400][1:]
                        x2, y2 = list[450][1:]
                        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                        cv2.line(capture, (x1, y1), (x2, y2), (0,255,0), 2)
                        cv2.circle(capture, (x1, y1), 2, (0,255,0), cv2.FILLED)
                        cv2.circle(capture, (x2, y2), 2, (0,255,0), cv2.FILLED)
                        cv2.circle(capture, (cx, cy), 2, (0,255,0), cv2.FILLED)


                    #print("id=", id, ", x=", x, ", y=", y)
                    faceArray.append([x,y])
                    #print("Array=", id, " ", faceArray[0])
                    
                    
                    
        else:
            cv2.putText(capture, "No Match found!", (x,y-25), 1, 1.3, (0,0,255), 1, cv2.LINE_AA)
            cv2.rectangle(capture, (x,y), (x+h, y+w), (0,0,255), 2)

        
    

    cv2.imshow("Result", capture)
    if(cv2.waitKey(1)==ord("q")):
        break

camera.release()
cv2.destroyAllWindows()

print("End")
