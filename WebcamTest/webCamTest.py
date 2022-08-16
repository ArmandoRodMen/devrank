
import cv2 as cv2

videoCapture=cv2.VideoCapture(0)

if not videoCapture.isOpened():
    print("No video camera found")
    exit()

while True:
    cameraType, camera= videoCapture.read()
    grayScale= cv2.cvtColor(camera, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Stream", grayScale)

    if cv2.waitKey(1) == ord("q"):

        break

videoCapture.release()

cv2.destroyAllWindows()