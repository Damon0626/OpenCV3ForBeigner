# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-15 下午9:11
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2


image = cv2.imread("../../Chapter03/dota.jpg")
temp = image.copy()
gray = False
while True:
	cv2.imshow("ChangeColor", temp)
	k = cv2.waitKey(10)
	if k == 27 or k == ord('q'):
		break
	if k == ord('g'):
		if not gray:
			temp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			gray = True
		else:
			temp = image.copy()
			gray = False
cv2.destroyAllWindows()