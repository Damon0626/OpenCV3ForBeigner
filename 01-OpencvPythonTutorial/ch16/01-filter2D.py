# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-23 下午9:13
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
和卷积神经网络有点像，5*5的核，求平均数代替原值
'''

img = cv2.imread('../ch06/opencv.png')
kernel = np.ones((5, 5), np.float32)/25

dst = cv2.filter2D(img, -1, kernel)  # 卷积

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')

plt.show()