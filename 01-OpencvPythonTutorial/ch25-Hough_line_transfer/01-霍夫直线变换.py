# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-13 下午10:36
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Opencv实现了两种霍夫线变换：

１－标准霍夫线变换
    提供一组参数对（tho, theta)的结合来表示检测到的直线，在OpenCV中通过函数houghlines实现
２－统计概率霍夫线变换
    效率更高的霍夫线性变换，它输出检测到的直线的端点，(x0, y0, x1, y1)，在OpenCV中通过函数houghlinesP来实现
'''

import cv2
import numpy as np


img = cv2.imread('../ch18/sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 10, 50, apertureSize=3)
cv2.imshow('edges', edges)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)  # 极坐标 ro和theta
print('Len of lines:', len(lines))
# print(lines)

for line in lines:
	rho, theta = line[0]
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a * rho
	y0 = b * rho

	x1 = int(x0 + 1000 * (-b))
	y1 = int(y0 + 1000 * (a))
	x2 = int(x0 - 1000 * (-b))
	y2 = int(x0 - 1000 * (a))

	cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
	cv2.imshow('houghlines', img)
	cv2.waitKey(1000)

cv2.waitKey(0)
cv2.destroyAllWindows()