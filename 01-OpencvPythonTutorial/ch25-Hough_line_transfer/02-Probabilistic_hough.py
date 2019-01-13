# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-13 下午10:45
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


img = cv2.imread('../ch18/sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

minLineLength = 100
maxLineGap = 10

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
print("Len fo lines:", len(lines))

for line in lines:
	x1, y1, x2, y2 = line[0]
	cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('houghlines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()