import cv2 as cv
import numpy as np

image = cv2.imread("imagem_test.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow(‘Original image’,image)
cv2.imshow(‘Gray image’, gray)
cv2.waitKey(0)
cv2.destroyAllWindows()