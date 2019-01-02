# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-2 下午9:54
# @Email : wwymsn@163.com
# @Software: PyCharm


import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('../ch10/messi5.jpg', 0)
f = np.fft.fft2(img)

fshift = np.fft.fftshift(f)  # move the zeros to the center of spectrum

magnitude_spectrum = 20 * np.log(np.abs(fshift))  # need to find the 'signal analyze' book

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()

