# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-16 下午11:04
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import matplotlib.pyplot as plt


image = cv2.imread('home.jpg')
color = ('b', 'g', 'r')

for i, col in enumerate(color):
	histr = cv2.calcHist([image], [i], None, [256], [0, 256])
	plt.plot(histr, color=col)
	plt.xlim([0, 256])
plt.show()