# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-12 下午9:26
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


cap = cv2.VideoCapture('vtest.avi')
ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255

while True:
	ret, frame2 = cap.read()
	next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

	# Computes a dense optical flow using the Gunnar Farneback's algorithm.
	flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
	mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
	hsv[..., 0] = ang * 180/np.pi/2
	hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
	bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

	cv2.imshow('frame2', frame2)
	cv2.imshow('flow', bgr)

	if cv2.waitKey(1) == ord('q'):
		break
	prvs = next
cv2.destroyAllWindows()
cap.release()
