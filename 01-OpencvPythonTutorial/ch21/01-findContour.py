# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 下午12:19
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2


img = cv2.imread('chessboard.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.resize(img_gray, (360, 370))
cv2.imshow('imz_gray', img_gray)

ret, thresh = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh)

image, contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('Contour size:', len(contours))

img = cv2.drawContours(img_gray, contours, -1, (0, 255, 0), 3)
cv2.imshow('contour', img)
while True:
	if cv2.waitKey(1) == ord('q'):
		break

cv2.destroyAllWindows()