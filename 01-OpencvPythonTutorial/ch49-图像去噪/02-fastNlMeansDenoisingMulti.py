# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-19 下午10:05
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture('../ch40-光流/vtest.avi')
img = [cap.read()[1] for i in range(5)]

gray = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in img]

gray = [np.float64(i) for i in gray]

noise = np.random.randn(*gray[1].shape)*10
noisy = [i + noise for i in gray]
noisy = [np.uint8(np.clip(i, 0, 255)) for i in noisy]

dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7, 35)

plt.subplot(131), plt.imshow(gray[2], 'gray')
plt.subplot(132), plt.imshow(noisy[2], 'gray')
plt.subplot(133), plt.imshow(dst, 'gray')

plt.show()
