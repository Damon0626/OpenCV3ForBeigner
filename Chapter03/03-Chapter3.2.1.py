# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-13 下午8:04
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2


g_nMaxAlphaValue = 100
WINDOW_NAME = "LineMixDisplay"
g_nAlphaValueSlider = 70


def on_Tracker(*args):
	g_nAlphaValueSlider = cv2.getTrackbarPos("Alpha", WINDOW_NAME)
	print(g_nAlphaValueSlider)
	res = cv2.addWeighted(srcImage1, g_nAlphaValueSlider/100, srcImage2, 1-g_nAlphaValueSlider/100, 0.0)
	cv2.imshow(WINDOW_NAME, res)


srcImage1 = cv2.imread('1.jpg')
srcImage2 = cv2.imread('2.jpg')
cv2.namedWindow(WINDOW_NAME)
cv2.createTrackbar("Alpha", WINDOW_NAME, g_nAlphaValueSlider, 100, on_Tracker)


cv2.waitKey()
cv2.destroyAllWindows()
