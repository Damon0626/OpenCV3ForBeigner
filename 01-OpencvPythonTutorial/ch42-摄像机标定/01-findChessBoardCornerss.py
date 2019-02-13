# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-13 下午8:33
# @Email : wwymsn@163.com
# @Software: PyCharm


import glob
import cv2
import numpy as np


criteria = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6*7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

objpoints = []
imgpoints = []

images = glob.glob('./left*.jpg')
images += glob.glob('./right*.jpg')

for fname in images:
	# print(fname)
	img = cv2.imread(fname)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)  # 寻找棋盘内角点
	if ret:
		objpoints.append(objp)
		corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
		imgpoints.append(corners)

		cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
		cv2.imshow('img', img)
		cv2.waitKey(500)
cv2.destroyAllWindows()