# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-16 下午10:28
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('eye-color-blue-z-c-660x440.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(121), plt.imshow(gray, 'gray')
plt.xticks([]), plt.yticks([])

circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=50, minRadius=0, maxRadius=50)
circles1 = np.uint16(np.around(circles1))

for i in circles1[0, :]:
	cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 5)
	cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 10)

plt.subplot(122), plt.imshow(np.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
plt.xticks([]), plt.yticks([])
plt.show()