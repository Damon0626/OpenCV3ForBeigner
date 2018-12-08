# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 下午8:23
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2

img = cv2.imread('star.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
_, contours, hierarchy = cv2.findContours(thresh, 2, 1)

img = cv2.drawContours(img, contours, 2, [255, 0, 0], 3)
cnt = contours[2]
hull = cv2.isContourConvex(cnt)
print(hull)
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
print(defects.shape)  # (7,1,4)
for i in range(defects.shape[0]):
	s, e, f, d = defects[i, 0]
	start = tuple(cnt[s][0])
	end = tuple(cnt[e][0])
	far = tuple(cnt[f][0])
	cv2.line(img, start, end, [0, 255, 0], 2)
	cv2.circle(img, far, 5, [0, 0, 255], -1)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()