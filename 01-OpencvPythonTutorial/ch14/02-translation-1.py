# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-21 下午10:25
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
'''
平移
'''
img = cv2.imread('../ch10/messi5.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])  # x移动100, y移动50
dst = cv2.warpAffine(img, M, (rows, cols))  # 原图，移动距离，输出图像大小
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()