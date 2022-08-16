#Armando
#contoursCoins.py
#Filter the image in order to get the coins count

from cv2 import Canny, GaussianBlur, cv2
import numpy as np

gaussVlaue= 3
kernelValue= 3

originalImage= cv2.imread("monedas.jpg")
cv2.imshow("Original", originalImage)

grayScaleImage= cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
gaussBlurImage= cv2.GaussianBlur(grayScaleImage, (gaussVlaue, gaussVlaue), 0)
cannyEdgeImage= cv2.Canny(gaussBlurImage, 60, 100)

kernel=np.ones((kernelValue, kernelValue),np.uint8)
closeContours= cv2.morphologyEx(cannyEdgeImage, cv2.MORPH_CLOSE, kernel)

contours, hierarchy= cv2.findContours(closeContours.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(originalImage, contours, -1, (0, 255, 0), 2)

cv2.imshow("Grayscale", grayScaleImage)
cv2.imshow("Gaussian Blur", gaussBlurImage)
cv2.imshow("Canny Contours", closeContours)
cv2.imshow("Result", originalImage)

print("Coins found: {}".format(len(contours)))

cv2.waitKey(0)
