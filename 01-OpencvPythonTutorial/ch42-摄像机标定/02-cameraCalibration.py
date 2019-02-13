# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-13 下午9:06
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


criteria = (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001)
cap = cv2.VideoCapture(0)

frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = int(480/frame_width*frame_height)

ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)  # 270
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

while cap.isOpened():
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	ret, corners = cv2.findChessboardCorners(gray, (6, 4), None)
	print(corners)
	print('------')
	if ret:
		corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
		cv2.drawChessboardCorners(img, (6, 4), corners2, ret)

	cv2.imshow('img', img)

	if cv2.waitKey(10) == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()