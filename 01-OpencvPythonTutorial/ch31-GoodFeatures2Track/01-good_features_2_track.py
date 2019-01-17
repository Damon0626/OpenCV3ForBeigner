# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-17 下午10:04
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('blox.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
print(corners)

corners = np.int0(corners)

for i in corners:
	x, y = i.ravel()  # 注意和flatten的区别，ravel是视图，改变会改变原来的值
	cv2.circle(img, (x, y), 3, 255, -1)

plt.imshow(img)
plt.show()