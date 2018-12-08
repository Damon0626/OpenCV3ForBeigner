# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 上午10:37
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../ch10/messi5.jpg', 0)
edge = cv2.Canny(img, 150, 200)
# cv2.imshow('edges', edge)
# cv2.waitKey(0)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(edge, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()