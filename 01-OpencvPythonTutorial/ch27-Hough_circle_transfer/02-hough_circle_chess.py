# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-16 下午10:03
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
from collections import Counter

def detec_weiqi_color(img):
	txt = 'black'
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # 高于100的都设置为255

	c = Counter(list(threshold.flatten()))  # 对边缘像素数量进行计数
	print(c.most_common())  # 黑色:num, 白色:num

	if c.most_common()[0][0] != 0:  # 不存在0,即不存在黑色
		txt = 'white'
	return txt, threshold


img = cv2.imread('weiqi.png')
img = cv2.medianBlur(img, 5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=10, maxRadius=50)

if circles is None:
	exit(-1)

circles = np.uint16(np.around(circles))

cv2.waitKey(0)
font = cv2.FONT_HERSHEY_SIMPLEX

for i in circles[0, :]:
	cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
	cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

	x, y, r = i
	crop_img = img[y-r:y+r, x-r:x+r]  # 棋子方图

	# 检测颜色
	txt, threshold = detec_weiqi_color(crop_img)
	print("颜色：", '黑色' if txt == 'black' else '白色')

	cv2.putText(threshold, txt, (0, 0), font, 0.5, (0, 255, 0), 2)
	cv2.imshow('threshold', threshold)

	cv2.imshow('crop_img', crop_img)
	cv2.moveWindow('crop_img', x=0, y=img.shape[0])

	cv2.imshow('detectd chess', img)
	cv2.moveWindow('detected chess', y=0, x=img.shape[1])

	cv2.waitKey(1500)

cv2.waitKey(0)
cv2.destroyAllWindows()
