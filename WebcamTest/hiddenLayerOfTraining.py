import cv2 as cv2
import os
import numpy as np
from time import time 

dataPath= "C:/Users/shini/Desktop/PythonFaceRec/WebcamTest/faceLibrary"
dataList=os.listdir(dataPath)
#print("data", dataList)

ids=[]
facesData=[]
id=0
startTime= time()


for row in dataList:
    fullPath= dataPath+"/"+row
    print("Starting lecture")
    for file in os.listdir(fullPath):

        totalLectureTime= time()
        lectureTime= totalLectureTime - startTime
        print("Images: ", row +"/"+ file)
        ids.append(id)
        facesData.append(cv2.imread(fullPath+"/"+file,0))
        images=cv2.imread(fullPath+"/"+file,0)


    id=id+1
    totalLectureTime= time()
    lectureTime= totalLectureTime - startTime
    print("Total time= ", lectureTime)

EigenFaceRecognizer=cv2.face.EigenFaceRecognizer_create()

print("Starting training")

EigenFaceRecognizer.train(facesData, np.array(ids))

endTrainingTime= time()
totalTrainingTime= endTrainingTime-totalLectureTime

print("Total lecture time= ", totalTrainingTime)

EigenFaceRecognizer.write("Training_EigenRecognizer.xml")

print("Finished")