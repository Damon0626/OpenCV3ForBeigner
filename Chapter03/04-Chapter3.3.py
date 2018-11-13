# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-13 下午9:02
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import numpy as np


# 鼠标按下状态反转
drawing = False
ix = -1
iy = -1


def onMouse(event, x, y, flags, param):
	global ix, iy, drawing
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
	elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
		if drawing:
			cv2.rectangle(canvas, (ix, iy), (x, y), (0, 255, 0), -1)
		elif event == cv2.EVENT_LBUTTONUP:
			drawing = False


WINDOW_NAME = "Window"
# 创建一个全黑的画布
canvas = np.zeros((600, 800, 3))
cv2.namedWindow(WINDOW_NAME)
cv2.setMouseCallback(WINDOW_NAME, onMouse)
while True:
	cv2.imshow(WINDOW_NAME, canvas)
	if cv2.waitKey(1) == 27:
		break
cv2.destroyAllWindows()