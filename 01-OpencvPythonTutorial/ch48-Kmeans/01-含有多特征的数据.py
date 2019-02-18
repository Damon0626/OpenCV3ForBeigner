# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-18 下午7:51
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import numpy as np
import matplotlib.pyplot as plt


X = np.random.randint(25, 50, (25, 2))   # 25*2, 25~50随机整数
Y = np.random.randint(60, 85, (25, 2))
Z = np.vstack((X, Y))

Z = np.float32(Z)

# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
# A = TERM_CRITERIA_EPS 按照精度终止,B = TERM_CRITERIA_MAX_ITER,按照迭代次数终止,A+B 满足任一条件时终止
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(Z, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

A = Z[label.ravel() == 0]
B = Z[label.ravel() == 1]

plt.scatter(A[:, 0], A[:, 1])
plt.scatter(B[:, 0], B[:, 1], c='r')
plt.scatter(center[:, 0], center[:, 1], s=80, c='y', marker='s')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()
