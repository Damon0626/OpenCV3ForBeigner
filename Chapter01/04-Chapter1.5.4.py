# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-5 下午11:45
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
'''
canny边缘检测,先用RGB2GRAY转换为灰度图片，然后Blur进行降噪，最后用Canny进行边缘检测
'''
srcImage = cv2.imread('test.jpg')

while True:
	cv2.imshow('srcImage', srcImage)
	grayImage = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
	blurGrayImage = cv2.blur(grayImage, (5, 5))  # 默认5*5滤波

	# maxVal和minVal,灰度高于maxVal的认为是真正的边界，低于minVal的舍弃
	# 两者之间的值要判断是否与真正的边界相连，相连舅保留，否则丢弃
	edge = cv2.Canny(blurGrayImage, 10, 30)
	cv2.imshow('Canny', edge)

	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()