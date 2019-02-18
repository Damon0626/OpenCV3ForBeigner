# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-18 下午8:17
# @Email : wwymsn@163.com
# @Software: PyCharm


import numpy as np
import cv2


image = cv2.imread('./home.jpg')
z = image.reshape((-1, 3))
z = np.float32(z)

creteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 2
ret, label, center = cv2.kmeans(z, k, None, creteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((image.shape))

cv2.imshow('res2', res2)

cv2.waitKey(0)
cv2.destroyAllWindows()