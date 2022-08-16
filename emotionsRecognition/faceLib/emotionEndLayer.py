import cv2
import os
import numpy as np
import imutils
import matplotlib.pyplot as plt

def emotionImage(emotion):
    if emotion == "Neutral":
        
        image = cv2.hconcat([frame,np.zeros((480,300,3),dtype=np.uint8)])
    if emotion == "Angry": 
        image = cv2.hconcat([frame,np.zeros((480,300,3),dtype=np.uint8)])
    if emotion == "Happy": 
        image = cv2.hconcat([frame,np.zeros((480,300,3),dtype=np.uint8)])
    #if emotion == "Fear": image = cv2.imread('Captura.png')
    #if emotion == "Surprise": image = cv2.imread('Captura.png')
    #if emotion == "Disgust": image = cv2.imread('Captura.png')
    print(emotion)
    return image

method = 'EigenFaces'
#method = 'FisherFaces'
#method = 'LBPH'

if method == 'EigenFaces': emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
emotion_recognizer.read("model"+method+".xml")

dataPath = "C://Users//shini//Desktop//emotionsRecognition//faceLib" 
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
faceClassif = cv2.CascadeClassifier("C:\\Users\\shini\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    nFrame = cv2.hconcat([frame, np.zeros((480,300,3),dtype=np.uint8)])
    faces = faceClassif.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(160,160),interpolation= cv2.INTER_CUBIC)
        result = emotion_recognizer.predict(rostro)
        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        # EigenFaces
        if method == 'EigenFaces':
            if result[1] < 5700:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                image = emotionImage(imagePaths[result[0]])
                nFrame = image
            else:
                cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                nFrame = cv2.hconcat([frame,np.zeros((480,300,3),dtype=np.uint8)])
    cv2.imshow('nFrame',nFrame)
    if(cv2.waitKey(1)==ord("q")):
        break
cap.release()
cv2.destroyAllWindows()
print("End")
