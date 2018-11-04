# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-1 下午11:13
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2


pic = cv2.imread("4.jpg")
while True:
	cv2.imshow("pic", pic)
	if cv2.waitKey(1) == 27:  # Ese按键
		break

cv2.destroyAllWindows()