# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-14 下午8:58
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


cap = cv2.VideoCapture(0)

# params = cv2.SimpleBlobDetector_Params()
# params.minThreshold = 10
# params.maxThreshold = 200
#
# params.filterByArea = True  # 像素大小控制
# params.minArea = 1500
#
# params.filterByCircularity = True  # 凹型控制
# params.minCircularity = 0.1
#
# params.filterByConvexity = True  # 凸型控制
# params.minConvexity = 0.87
#
# params.filterByInertia = True  # 圆形控制
# params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create()

while cap.isOpened():
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	keypoints = detector.detect(gray)

	img_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow('keypoints', img_with_keypoints)

	if cv2.waitKey(1) == ord('q'):
		break
cv2.destroyAllWindows()