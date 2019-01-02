# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-2 下午9:25
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
构造了一个低通滤波器，可以预想下结果，低通图像模糊

通过观察结果，我们可以看到，在经历过矩形低通滤波器后，图像产生了震荡，就像敲击后产生的空气震荡，我们称之为＂振铃现象＂
这种现场通常是由矩形低通滤波器造成，我们一般不用矩形低通滤波器，最好用高斯滤波.
'''

import matplotlib.pyplot as plt
import cv2
import numpy as np


img = cv2.imread('../ch10/messi5.jpg', 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)

# 创建一个掩膜，中心30*30是1，其余为0  模拟矩形低通滤波器
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow - 30: crow + 30, ccol - 30: ccol + 30] = 1

fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)

# 计算x, y两数组形成的向量的大小，如[1,2,3]和[4,5,6]，结果[4.123, 5.385, 6.708]
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])


plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()