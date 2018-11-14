# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-14 下午9:00
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np

WINDOW_NAME = "Drawing"
backgroud = np.zeros((600, 600, 3))  # 黑色背景
cv2.namedWindow(WINDOW_NAME)
cv2.ellipse(backgroud, (300, 300), (150, 37), 0, 0, 360, 255, 2)  # 不接受浮点型
cv2.ellipse(backgroud, (300, 300), (150, 37), 45, 0, 360, 255, 2)
cv2.ellipse(backgroud, (300, 300), (150, 37), 90, 0, 360, 255, 2)
cv2.ellipse(backgroud, (300, 300), (150, 37), -45, 0, 360, 255, 2)
cv2.circle(backgroud, (300, 300), 18, 255, -1)

while True:
	cv2.imshow(WINDOW_NAME, backgroud)
	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()