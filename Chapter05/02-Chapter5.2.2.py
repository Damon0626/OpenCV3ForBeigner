# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-16 下午10:14
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
'''
简单的线性叠加
'''
# 定义一些局部变量
alpha = 0.5
beta = 1 - alpha
srcImage1 = cv2.imread('mogu.jpg')
srcImage2 = cv2.imread('rain.jpg')

res = cv2.addWeighted(srcImage1, alpha, srcImage2, beta, 0.0)

while True:
	cv2.imshow("src", srcImage1)
	cv2.imshow("dst", res)
	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()