# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-4 下午10:26
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
OpenCV 提供了三种不同的梯度滤波器 或者说是高通滤波器：Sobel，  Scharr 和 Laplacian。
Sobel Scharr 其实就是求一阶或二阶导数。
Scharr 是对 Sobel (使用小的卷积核求解 梯度角度时 )的优化。
Laplacian 是求二阶导数。
'''
image = cv2.imread("sudoku.jpg", 0)
laplacian = cv2.Laplacian(image, cv2.CV_64F)
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)  # 在x方向求导
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray')
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')

plt.show()
