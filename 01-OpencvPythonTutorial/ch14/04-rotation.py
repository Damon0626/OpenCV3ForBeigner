# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-23 下午8:54
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


img = cv2.imread('../ch10/messi5.jpg', 0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)
dst = cv2.warpAffine(img, M, (2*cols, 2*rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()