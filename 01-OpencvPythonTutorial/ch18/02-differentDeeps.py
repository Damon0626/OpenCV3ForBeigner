# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-4 下午10:36
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import matplotlib.pyplot as plt
import numpy as np
'''
设置的深度越高，那么可以检测到想要的边界
'''
image = cv2.imread("sudoku.jpg", 0)

sobelx8u = cv2.Sobel(image, cv2.CV_8U, 1, 0, ksize=5)
sobelx64F = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

abs_sobel64F = np.absolute(sobelx64F)
sobel_8u = np.uint8(abs_sobel64F)

plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray')
plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray')
plt.show()