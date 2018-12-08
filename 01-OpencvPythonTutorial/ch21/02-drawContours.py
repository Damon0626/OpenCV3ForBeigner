# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 下午4:01
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2

img = cv2.imread('cards.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 244, 255, 0)

img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Contours length:", len(contours))

contours2 = [cnt for cnt in contours if cv2.contourArea(cnt)>200]
print("With Filter the length of contours", len(contours2))

result = cv2.drawContours(img_gray, contours[4], -1, (255, 0, 0), 3)
cv2.imshow('result', result)

cv2.waitKey(0)

