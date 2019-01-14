# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-14 下午8:43
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


img = cv2.imread('blob.jpg', cv2.IMREAD_GRAYSCALE)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 10
params.maxThreshold = 200

params.filterByArea = True  # 像素大小控制
params.minArea = 1500

params.filterByCircularity = True  # 凹型控制
params.minCircularity = 0.1

params.filterByConvexity = True  # 凸型控制
params.minConvexity = 0.87

params.filterByInertia = True  # 圆形控制
params.minInertiaRatio = 0.01


detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(img)
# print(len(keypoints))  # 16

img_with_keypoints  = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('keypoints', img_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()