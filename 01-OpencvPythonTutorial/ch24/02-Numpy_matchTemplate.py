# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-3 下午10:01
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


img_rgb = cv2.imread('./mario.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('./mario_coin.png', 0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.8
loc = np.where(res >= threshold)

print(loc)  # loc为两个数组，第一个表示所在行，第二个表示所在列，行和列结合就能确定坐标

for pt in zip(*loc[::-1]):  # 解压
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
	print('rectangle 1')

cv2.imshow('result', img_rgb)
cv2.waitKey(0)