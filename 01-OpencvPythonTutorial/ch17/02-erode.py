# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-23 下午9:34
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import numpy as np


img = cv2.imread('j.png', 0)
cv2.imshow('j.png', img)
print(img.shape)


kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow('erode', erosion)
cv2.moveWindow('erode', x=img.shape[1], y=0)
cv2.waitKey(0)
cv2.destroyAllWindows()