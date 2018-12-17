# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-16 下午11:25
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('contrast75.png')
hist, bins = np.histogram(image.flatten(), 256, [0, 256])

cdf = hist.cumsum()  # 累积分布
cdf_mormalized = cdf*hist.max()/cdf.max()

plt.plot(cdf_mormalized, color='b')
plt.hist(image.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(['cdf', 'histogram'], loc='upper left')
plt.show()



