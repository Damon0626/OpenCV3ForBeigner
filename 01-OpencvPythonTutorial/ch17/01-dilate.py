# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-23 下午9:27
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
'''
膨胀
'''
img = cv2.imread('j.png', 0)
cv2.imshow('j.png', img)
print(img.shape)

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)  # iteration是膨胀的重复次数

cv2.imshow('dilation', dilation)
cv2.moveWindow('dilation', x=img.shape[1], y=0)
cv2.waitKey(0)
cv2.destroyAllWindows()