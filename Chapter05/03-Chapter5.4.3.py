# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-16 下午10:36
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
'''
简单地对图像的亮度和对比度进行调整
'''


def contratAndBright(*args):
	contrastValue = cv2.getTrackbarPos("ContrastValue", "Result")
	brightValue = cv2.getTrackbarPos("BrightValue", "Result")
	res = np.uint8(np.clip((contrastValue*image*0.01+brightValue), 0, 255))  # 可以将值限制在0-255之间
	# image[i][j][np.where(image[i][j][:] > 255)] = 255
	# image[i][j][np.where(image[i][j][:] < 0)] = 0
	# res[np.where(res > 255)] = 255
	cv2.imshow("Result", res)


image = cv2.imread('1.jpg')
contrastValue = 80  # 对比度
brightValue = 80  # 亮度

cv2.namedWindow("Result")
cv2.createTrackbar("ContrastValue", "Result", contrastValue, 300, contratAndBright)
cv2.createTrackbar("BrightValue", "Result", contrastValue, 100, contratAndBright)

cv2.waitKey(0)
cv2.destroyAllWindows()