# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-18 下午10:28
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2


img = cv2.imread('home.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)
print(kp)
img = cv2.drawKeypoints(gray, kp, img)

kp, des = sift.detectAndCompute(gray, None)
# cv2.imwrite('sift-keypoints.jpg', img)
cv2.imshow('sift_keypoints', img)

cv2.waitKey(0)