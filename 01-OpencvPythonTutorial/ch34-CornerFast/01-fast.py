# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-22 下午4:41
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2

img = cv2.imread('blox.jpg', 0)

fast = cv2.FastFeatureDetector_create()

kp = fast.detect(img, None)

# img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
img2 = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0))
print("Threshhold", fast.getThreshold())
print("nonmaxSuppression:", fast.getNonmaxSuppression())
print("neighborhodd:", fast.getType())
print("Total keypoints with nonmaxSuppression:", len(kp))
cv2.imshow('fast_true', img2)
cv2.waitKey(0)
