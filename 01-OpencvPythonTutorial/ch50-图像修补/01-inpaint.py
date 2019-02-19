# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-19 下午10:24
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2


img = cv2.imread('./messi_2.jpg')
mask = cv2.imread('mask2.png', 0)
cv2.imshow('img', img)
cv2.imshow('mask', mask)

dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)  # 快速行进算法
cv2.imshow('INPAINT_TELEA', dst)

dst2 = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
cv2.imshow('INPAINT_NS', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()