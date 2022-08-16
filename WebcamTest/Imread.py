from skimage import feature
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('effyup.jpg')
(hog, hog_image) = feature.hog(image, orientations=9, 
                    pixels_per_cell=(8, 8), cells_per_block=(2, 2), 
                    block_norm='L2-Hys', visualize=True, transform_sqrt=True)

cv2.imshow("Original", image)
cv2.imshow('HOG Image', hog_image)
cv2.imwrite('hog_face.jpg', hog_image*255.)
cv2.waitKey(0)