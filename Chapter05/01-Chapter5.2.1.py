# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-16 下午10:02
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2


srcImage = cv2.imread('dota_pa.jpg')
mask = cv2.imread("../Chapter03/dota_logo.jpg")

srcImage[200:200+mask.shape[0], 250:250+mask.shape[1]] = mask

while True:
	cv2.imshow("src", srcImage)
	# cv2.imshow("logo", mask)

	if cv2.waitKey(1) == 27:
		break
cv2.destroyAllWindows()