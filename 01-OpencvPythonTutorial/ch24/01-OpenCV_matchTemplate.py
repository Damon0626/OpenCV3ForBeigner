# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-3 下午9:23
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
CV_TM_SQDIFF 平方差匹配法：该方法采用平方差来进行匹配；最好的匹配值为0；匹配越差，匹配值越大。

CV_TM_CCORR 相关匹配法：该方法采用乘法操作；数值越大表明匹配程度越好。

CV_TM_CCOEFF 相关系数匹配法：1表示完美的匹配；-1表示最差的匹配。

CV_TM_SQDIFF_NORMED 归一化平方差匹配法

CV_TM_CCORR_NORMED 归一化相关匹配法

CV_TM_CCOEFF_NORMED 归一化相关系数匹配法

'''

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./messi5.jpg', 0)
img2 = img.copy()

template = cv2.imread('./messi_face.jpg', 0)

# print(template.shape[::-1])  # (52, 40)

w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
	img = img2.copy()

	method = eval(meth)

	res = cv2.matchTemplate(img, template, method)

	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 在res中找到最小值和最大值，并返回其坐标

	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc

	bottom_right = (top_left[0] + w, top_left[1] + h)

	cv2.rectangle(img, top_left, bottom_right, 255, 2)

	plt.subplot(121), plt.imshow(res, cmap='gray')
	plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

	plt.subplot(122), plt.imshow(img, cmap='gray')
	plt.title('Detected Point'), plt.xticks([]), plt.yticks([])

	plt.suptitle('method:' + meth)

	plt.show()