# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 下午7:55
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


img = cv2.imread('lightning.png', 0)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
'''
凸包：数学中，在实向量空间V中的一组点x的凸包或凸包络使包含x的最小凸集，通俗的来说就是，包围一组散点的最小凸边形．
cv2.convexHull(),计算凸包．
'''
hull = cv2.convexHull(cnt)

# 凸边检测
k = cv2.isContourConvex(hull)  # 返回是＼否
# print(k)

# 边界矩形
x, y, w, h = cv2.boundingRect(cnt)
# print(x, y, w, h)
# img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# cv2.imshow('img', img)

# 旋转矩形
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
# cv2.drawContours(img, [box], 0, (255, 0, 0), 2)
# cv2.imshow('min', img)

# 最小外接圆
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
# cv2.circle(img, center, radius, (255, 0, 0), 2)
# cv2.imshow('circle', img)

# 椭圆拟合
ellipsis = cv2.fitEllipse(cnt)
angel = ellipsis[2]
# cv2.ellipse(img, ellipsis, (255, 0, 0), 2)
# cv2.imshow('Ellipse', img)

# 拟合直线
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx)+y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img, (cols-1, righty), (0, lefty), (255, 0, 0), 2)
cv2.imshow('Line', img)
cv2.waitKey(0)