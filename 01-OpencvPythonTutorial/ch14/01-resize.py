# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-21 下午10:21
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
'''
扩展2倍
'''
image = cv2.imread('../ch10/messi5.jpg')
res = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
while True:
	cv2.imshow('iamge', image)
	cv2.imshow('resize', res)
	if cv2.waitKey(1) == 27:
		break
cv2.destroyAllWindows()