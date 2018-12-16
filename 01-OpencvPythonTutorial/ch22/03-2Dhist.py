# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-16 下午3:20
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import matplotlib.pyplot as plt

image = cv2.imread('home.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

h, s, v = cv2.split(hsv)
plt.imshow(hist, interpolation='nearest')
plt.show()