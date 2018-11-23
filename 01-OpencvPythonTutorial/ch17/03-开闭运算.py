# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-23 下午9:41
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


img = cv2.imread('j.png', 0)
cv2.imshow('j.png', img)

kernel = np.ones((5, 5), np.uint8)

# 开运算，就是先腐蚀再膨胀，目的是消除噪声
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)
cv2.moveWindow('opening', x=img.shape[1], y=0)

# 闭运算，先膨胀再腐蚀，目的是填充前景物体中的小洞
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', closing)
cv2.moveWindow('closing', x=img.shape[1]*2, y=0)

# 形态学梯度，就是一幅图像膨胀与腐蚀的差别
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient', gradient)
cv2.moveWindow('gradient', x=img.shape[1]*3, y=0)

# 礼帽
# 原始图像与  开运算之后得到的图像的差。
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('tophat', tophat)
cv2.moveWindow('tophat', x=img.shape[1] * 4, y=0)

# 黑帽  进行闭运算之后得到的图像与原始图像的差
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('blackhat', blackhat)
cv2.moveWindow('blackhat', x=img.shape[1] * 5, y=0)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()