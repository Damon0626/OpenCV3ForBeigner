# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-18 下午8:05
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt


x = np.random.randint(25, 100, 25)
y = np.random.randint(175, 255, 25)
z = np.vstack((x, y))
z = z.reshape((50, 1))
z = np.float32(z)
plt.hist(z, 256, [0, 256])
plt.show()

creteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS

compactness, labels, centers = cv2.kmeans(z, 2, None, creteria, 10, flags)

A = z[labels == 0]
B = z[labels == 1]

plt.hist(A, 256, [0, 256], color='r')
plt.hist(B, 256, [0, 256], color='b')
plt.hist(centers, 32, [0, 256], color='y')
plt.show()