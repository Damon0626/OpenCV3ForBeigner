# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-23 下午9:23
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import matplotlib.pyplot as plt


img = cv2.imread('../ch06/opencv.png')
blur = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯模糊
median = cv2.medianBlur(blur, 5)  # 中值模糊

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.show()
