# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-20 下午10:40
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


lower = np.array([20, 100, 100])
upper = np.array([30, 255, 255])

image = cv2.imread('pingpang.JPG')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)

res = cv2.bitwise_and(image, image, mask=mask)

while True:
	cv2.imshow('iamge', image)
	cv2.imshow('res', res)
	if cv2.waitKey(1) == 27:
		break
cv2.destroyAllWindows()