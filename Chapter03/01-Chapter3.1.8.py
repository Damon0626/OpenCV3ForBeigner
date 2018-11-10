# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-9 下午4:59
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


# 对四个通道分别进行参数设置
def createAlphamat(img_rgba):
	width = img_rgba.shape[0]
	hight = img_rgba.shape[1]
	for i in range(width):
		for j in range(hight):
			b1 = (width-j)/width * 255  # 类似正则化
			g1 = (hight-i)/hight * 255
			img_rgba[i, j, 0] = b1  # 蓝通道
			img_rgba[i, j, 1] = g1  # 绿通道
			img_rgba[i, j, 2] = (b1+g1)/2  # 红通道
			img_rgba[i, j, 3] = 0.5*(b1+g1)  # Alpha通道
	return img_rgba


if __name__ == "__main__":
	originImage = np.ones((480, 640, 3))
	Alpha = np.ones((480, 640))  # 创建透明通道
	imgRGBA = cv2.merge((originImage, Alpha))  # 合并通道
	imgRGBA = createAlphamat(imgRGBA)
	cv2.imwrite('3.1.8.png', imgRGBA)

	# 图像显示,如果直接显示imgRGBA图像不对
	img = cv2.imread('3.1.8.png')
	while True:
		cv2.imshow('show', img)
		if cv2.waitKey(1) == 27:
			break
	cv2.destroyAllWindows()

