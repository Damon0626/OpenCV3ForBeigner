# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-19 下午9:35
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2

'''
按位运算
'''
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('../ch06/opencv.png')


# 在左上角添加opencv的logo
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)  # 黑底白字0/1
mask_inv = cv2.bitwise_not(mask)  # 白底黑字

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)  # 保留字迹以外的背景
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)  # 保留字迹

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)

cv2.destroyAllWindows()