# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-12 下午9:57
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np

cap = cv2.VideoCapture('../ch40-光流/vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)
	cv2.imshow('frame', fgmask)
	if cv2.waitKey(1) == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()