# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 下午5:21
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np

org_img = cv2.imread('cards.png')
imgray = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imgray', imgray)

# 大于244的值全部设置为255, 白色背景
ret, thresh = cv2.threshold(imgray, 244, 255, cv2.THRESH_BINARY)
cv2.imshow('after threshold', thresh)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

areas = list()
for i, cnt in enumerate(contours):
	areas.append((i, cv2.contourArea(cnt)))

a2 = sorted(areas, key=lambda d: d[1], reverse=True)
print(a2)
cv2.waitKey(0)

for i, area in a2:
	if area < 150:
		continue
	img22 = org_img.copy()
	cv2.drawContours(img22, contours, i, (0, 0, 255), 3)
	print(i, area)

	cv2.imshow('drawcontours', img22)
	cv2.moveWindow('drawcontours', x=img22.shape[1], y=0)
	if cv2.waitKey(500) == ord('q'):
		break

# 获取最大的contour
idx = a2[3][0]
mask = np.zeros_like(org_img)
cv2.drawContours(mask, contours, idx, (0, 255, 0), -1)
out = np.zeros_like(org_img)
out[mask == 255] = org_img[mask == 255]
cv2.imshow('out_contour', out)
cv2.waitKey(0)
