# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-2 下午9:59
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
高滤波器的作用：获得图像的边缘和纹理
'''


import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('../ch10/messi5.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)

fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0  # 高通滤波器

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)

img_back = np.abs(img_back)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(img_back, cmap='gray')
plt.title('Image After HLP'), plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

plt.show()