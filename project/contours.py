import cv2 as cv2
import numpy as np

image = cv2.imread('filtr.jpg')
b,g,r = cv2.split(image.copy())
_, contours, hierarchy = cv2.findContours(b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
img=image.copy()
for c in contours:
	x,y,w,h = cv2.boundingRect(c)
	img+=cv2.rectangle(image,(x,y),(x+w,y+h),(243,20,20),2)
cv2.drawContours(image, contours,-1, (0,255,0), 3)
cv2.imshow(image)
cv2.waitKey(0)