# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-2 上午8:49
# @Email : wwymsn@163.com
# @Software: PyCharm


'''
OpenCV中的傅立叶变换为cv2.dtf和cv2.idft
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../ch10/messi5.jpg', 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)  # 将零频分量移动到频谱的中心
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()