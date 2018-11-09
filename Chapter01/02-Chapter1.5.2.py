# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-4 下午11:04
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
'''
图像腐蚀：
即用图中暗色部分＂腐蚀＂掉图中的高亮部分．
'''
srcImage = cv2.imread("test.jpg")
while True:
	kernel = np.ones((15, 15))
	eroding = cv2.erode(srcImage, kernel=kernel)
	cv2.imshow("show", eroding)

	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()

