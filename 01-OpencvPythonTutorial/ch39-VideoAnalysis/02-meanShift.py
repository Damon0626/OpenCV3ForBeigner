# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-29 下午10:07
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


cap = cv2.VideoCapture('slow.flv')
ret, frame = cap.read()

r, h, c, w = 250, 90, 400, 125
track_window = (c, r, w, h)

roi = frame[r:r+h, c: c+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])

cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

term_crit = (cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
	ret, frame = cap.read()
	if ret is True:
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

		ret, track_window = cv2.meanShift(dst, track_window, term_crit)

		x, y, w, h = track_window
		print(track_window)

		img2 = cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
		cv2.imshow('img2', img2)

		k = cv2.waitKey(60)
		if k == 27:
			break
	else:
		break
cv2.destroyAllWindows()
cap.release()

# cv2.imshow('roi', roi)
# print(frame.shape)
# cv2.waitKey(0)
# cv2.destroyAllWindows()