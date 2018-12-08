# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 上午10:45
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import matplotlib.pyplot as plt
'''
图像金字塔，几乎可以无缝衔接两幅图片，苹果和橘子．内容报错：尺寸有点问题，30像素在down的时候使16而不是15...
显示6层图，向下像素丢失，图像模糊，向上只能扩充尺寸，清晰度不会改变．
'''
apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

orange_copy = orange.copy()
gp_oranage = [orange_copy]  # generate Gaussian pyramid
for i in range(6):  # 6层
	orange_copy = cv2.pyrDown(orange_copy)
	gp_oranage.append(orange_copy)
	plt.subplot(231+i), plt.imshow(orange_copy)
	plt.xticks([]), plt.yticks([])
plt.show()

apple_copy = apple.copy()
gp_apple = [apple_copy]  # generate Gaussian pyramid
for i in range(6):
	apple_copy = cv2.pyrDown(apple_copy)
	gp_apple.append(apple_copy)
	plt.subplot(231+i), plt.imshow(apple_copy)
	plt.xticks([]), plt.yticks([])
plt.show()
