import cv2 as cv2
import os
import numpy as np
import time


def obtainModel(method, facesData, ids):
    if method == "EigenFaces": emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
    #if method == "FisherFaces": emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
    #if method == "LBPH": emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

    print("Model training: "+ method +" ..." )
    start = time.time()
    emotion_recognizer.train(facesData, np.array(ids))
    trainingTime= time.time()-start
    print("Method: "+ method+" Training time: ", trainingTime)

    emotion_recognizer.write("model"+method+".xml")


dataPath= "C://Users//shini//Desktop//emotionsRecognition//faceLib"
dataList=os.listdir(dataPath)
#print("data", dataList)

ids=[]
facesData=[]
id=0

for row in dataList:
    fullPath= dataPath+"/"+row
    print("Starting lecture")
    for file in os.listdir(fullPath):

        print("Images: ", row +"/"+ file)
        ids.append(id)
        facesData.append(cv2.imread(fullPath+"/"+file,0))
        images=cv2.imread(fullPath+"/"+file,0)


    id=id+1

obtainModel('EigenFaces',facesData,ids)
#obtainModel('FisherFaces',facesData,ids)
#obtainModel('LBPH',facesData,ids)

print("Finished")