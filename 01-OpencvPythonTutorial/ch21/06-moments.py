# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 下午4:53
# @Email : wwymsn@163.com
# @Software: PyCharm
"""
计算图像的质心和面积等
"""

import cv2
from pprint import pprint

img = cv2.imread('lightning.png', 0)
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# thresh = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('contours length', len(contours))
cnt = contours[0]
M = cv2.moments(cnt)
# pprint(M)  # 用来计算重心
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print("重心", cx, cy)

area = cv2.contourArea(cnt)
print('面积', area)

perimeter = cv2.arcLength(cnt, True)  # True意味着对象的形状是闭合的，若false，则使一条直线
print('周长', perimeter)

epsilon = 0.1*cv2.arcLength(cnt, True)
print('Epsilon', epsilon)

approx = cv2.approxPolyDP(cnt, epsilon, True)
cv2.drawContours(img, [approx], 0, (255, 0, 0), 1)
cv2.imshow('approxployDP', img)
cv2.waitKey(0)
cv2.destroyAllWindows()