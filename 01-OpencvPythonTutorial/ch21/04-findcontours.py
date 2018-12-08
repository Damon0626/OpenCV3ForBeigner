# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 下午4:23
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2

img = cv2.imread('contour.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('thresh', binary)

image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('Contour size:', len(contours))

cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow('img', img)

cv2.waitKey(0)
