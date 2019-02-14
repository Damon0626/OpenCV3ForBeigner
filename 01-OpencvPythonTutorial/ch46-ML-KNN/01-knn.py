# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-14 下午8:30
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt


trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
responses = np.random.randint(0, 2, (25, 1)).astype(np.float32)

red = trainData[responses.ravel() == 0]

plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')
# plt.show()
blue = trainData[responses.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')
# plt.show()

# KNN 最好k为奇数
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')  # 测试数据

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)  # 建立模型
ret, results, neighbours, dist = knn.findNearest(newcomer, 3)

print('result:', results, "\n")
print('neighbours:', neighbours, "\n")
print('distance:', dist)
plt.show()
