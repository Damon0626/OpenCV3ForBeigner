# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-18 下午8:57
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


img = cv2.imread('./home.jpg')
z = img.reshape((-1, 3))
z = np.float32(z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 8

ret, label, center = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# 将分好的每一个类，单独放在一个数组中，其余部分填充0, 每一类都显示出来
for y in range(len(center)):
	a1 = []
	for i, x in enumerate(label.ravel()):
		if x == y:
			a1.append(list(z[i]))
		else:
			a1.append([0, 0, 0])
	a2 = np.array(a1)
	a3 = a2.reshape(img.shape)
	cv2.imshow('res2'+str(y), a3)

cv2.waitKey(0)
cv2.destroyAllWindows()