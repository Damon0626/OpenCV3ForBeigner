# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-19 下午10:23
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
'''
图像相减
'''
img1 = cv2.imread('subtract1.jpg')
img2 = cv2.imread('subtract2.jpg')

cv2.imshow('subtract1', img1)
cv2.imshow('subtract2', img2)

st = img2 - img1
cv2.imshow('after subtract', st)

ret, threshold = cv2.threshold(st, 50, 255, cv2.THRESH_BINARY)
cv2.imshow('after threshold', threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()