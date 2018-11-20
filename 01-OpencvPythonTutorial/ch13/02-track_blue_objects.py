# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-20 下午10:23
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


cap = cv2.VideoCapture(0)
ret = cap.set(3, 640)
ret = cap.set(4, 480)

lower = np.array([110, 50, 50])
upper = np.array([130, 255, 255])

while True:
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower, upper)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame', frame)
	cv2.moveWindow('frame', 0, 0)
	cv2.imshow('mask', mask)
	cv2.moveWindow('mask', x=frame.shape[1], y=0)
	cv2.imshow('res', res)
	cv2.moveWindow('res', y=frame.shape[0], x=0)
	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()