# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-9 下午3:48
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import time


cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	if not ret:
		break
	grayVideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	blurGrayVideo = cv2.blur(grayVideo, (5, 5))  # 5*5的内核来降噪

	edge = cv2.Canny(grayVideo, 150, 180)  # 边缘检测
	cv2.imshow('show', edge)
	time.sleep(0.04)

	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()

