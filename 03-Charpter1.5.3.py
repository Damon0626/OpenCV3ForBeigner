# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-5 下午11:12
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
'''
对图像进行均值滤波操作，模糊一张图片
'''
srcImage = cv2.imread('4.jpg')

while True:
	blurImage = cv2.blur(srcImage, (27, 27))  # size越大，越模糊
	cv2.imshow('blurImage', blurImage)
	cv2.imshow('srcImage', srcImage)

	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()