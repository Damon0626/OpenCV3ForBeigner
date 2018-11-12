# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-12 下午11:38
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
image = cv2.imread("dota.jpg")
logo = cv2.imread("dota_logo.jpg")
h = image.shape[0]
w = image.shape[1]
rows= logo.shape[0]
cols = logo.shape[1]
roi = image[h-rows-30:h-30, w-cols-30: w-30]
combine = cv2.addWeighted(roi, 0.7, logo, 0.3, 0.0)  # 要求两个尺寸必须一致才可以
image[h-rows-30:h-30, w-cols-30: w-30] = combine  # 替换
while True:
	cv2.imshow("dota", image)
	# cv2.imshow("logo", logo)
	# cv2.imshow("combine", combine)
	if cv2.waitKey(1) == 27:
		break
cv2.destroyAllWindows()