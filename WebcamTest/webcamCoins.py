"""""

Armando Rodriguez
09/15/2021
webcamCoin.py

Records camera and gets the coins number

"""""

import cv2 as cv2
import numpy as np
import math as math

width_px= 720
height_px= 540

baro_1_Diameter= 21
baro_5_Diameter= 25
baro_10_Diameter= 28

width_cm= width_px*2.54/96
height_cm= height_px*2.54/96

aspectRatio= width_cm/height_cm
aspectRatio_px= width_px/height_px

workSpace_Width_px= width_px
workSpace_Height_px= workSpace_Width_px/aspectRatio_px

baro_1_Radius= baro_1_Diameter/2
baro_5_Radius= baro_5_Diameter/2
baro_10_Radius= baro_10_Diameter/2

baro_1_Area= (math.pi)*((baro_1_Radius**2))
baro_5_Area= (math.pi)*((baro_5_Radius**2))
baro_10_Area= (math.pi)*((baro_10_Radius**2))

baro_1_Area_px= ((baro_1_Area*width_cm)/workSpace_Width_px)*1000
baro_5_Area_px= ((baro_5_Area*width_cm)/workSpace_Width_px)*1000
baro_10_Area_px= ((baro_10_Area*width_cm)/workSpace_Width_px)*1000

print("1 baro Area px= ", baro_1_Area_px)
print("5 baro Area px= ", baro_5_Area_px)
print("10 baro Area px= ", baro_10_Area_px)

def organicePoints(points):
    nPoints= np.concatenate([points[0], points[1], points[2], points[3]]).tolist()
    y_Order= sorted(nPoints, key=lambda nPoints:nPoints[1])
    x1_Order= y_Order[0:2]
    x1_Order= sorted(x1_Order, key=lambda x1_Order:x1_Order[0])
    x2_Order= y_Order[2:4]
    x2_Order= sorted(x2_Order, key=lambda x2_Order:x2_Order[0])

    return [x1_Order[0], x1_Order[1], x2_Order[0], x2_Order[1]]

def align(image, width, height):
    alignedImage= None
    grayScale= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold= cv2.threshold(grayScale, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("Threshold", threshold)
    contour= cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contour= sorted(contour, key= cv2.contourArea, reverse=True)[0:1]

    for i in contour:
        epsilon= 0.01*cv2.arcLength(i, True)
        approach= cv2.approxPolyDP(i, epsilon, True)
        if len(approach)==4:
            points= organicePoints(approach)
            poinst1= np.float32(points)
            points2= np.float32([[0,0], [width,0], [0, height], [width, height]])
            M= cv2.getPerspectiveTransform(poinst1, points2)
            alignedImage= cv2.warpPerspective(image, M, (width, height))

    return alignedImage

captureVideo= cv2.VideoCapture(0)

while True:
    cameraType, camera= captureVideo.read() 
    if cameraType==False:
        print("CAMERA ERROR")
        break
    image_WEBCAM= align(camera, width=1280, height=720)
    if image_WEBCAM is not None:
        points=[]
        imageGreyScale= cv2.cvtColor(image_WEBCAM, cv2.COLOR_BGR2GRAY)
        imageBlur= cv2.GaussianBlur(imageGreyScale, (5,5), 1)
        _, threshold_2= cv2.threshold(imageBlur, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
        cv2.imshow("Threshold", threshold_2)
        contour_2 = cv2.findContours(threshold_2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(image_WEBCAM, contour_2, -1, (0, 255, 0), 2)

        sum_1= 0.0
        sum_2= 0.0
        sum_3= 0.0 

        for a in contour_2:
            area= cv2.contourArea(a)
            moment= cv2.moments(a)
            if(moment["m00"]==0):
                moment["m00"]=1.0
            x= int(moment["m10"]/moment["m00"])
            y= int(moment["m01"]/moment["m00"])

            if area<baro_10_Area_px+500 and area>baro_10_Area_px-500:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image_WEBCAM, "10 baros", (x,y), font, 0.75, (0, 255, 0), 2)
                sum_1+= + 10.0

            if area<baro_5_Area_px+200 and area>baro_5_Area_px-200:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image_WEBCAM, "5 baros", (x,y), font, 0.75, (0, 255, 0), 2)
                sum_2+= 5.0
                
            if area<baro_1_Area_px+1000 and area>baro_1_Area_px-1000:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image_WEBCAM, "1 baro", (x,y), font, 0.75, (0, 255, 0), 2)
                sum_3+= 1.0

        total= sum_1 + sum_2 + sum_3
        print("Total: ", round(total,2))
        cv2.imshow("Webcam Coin", image_WEBCAM)
        cv2.imshow("Camera", camera)

    if cv2.waitKey(1) == ord("q"):
        break

captureVideo.release()
cv2.destroyAllWindows()

"""""

End Script

"""""