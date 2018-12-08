# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 下午4:11
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2

img1 = cv2.imread('star.jpg', 0)
img2 = cv2.imread('star2.jpg', 0)

ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)

image, contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]

image, contours, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)  # 3.22返回值越小，说明匹配越好
