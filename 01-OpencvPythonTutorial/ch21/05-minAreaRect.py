# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-8 下午4:31
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np

img = cv2.imread('lightning.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

image, contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = [cnt for cnt in contours if cv2.contourArea(cnt)>100]

cnt = contours[0]

(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)  # 得到拟合拟合椭圆中心，宽高，旋转角度
print((x, y), (MA, ma), angle)

rect = cv2.minAreaRect(cnt)  # 任意四边形的最小外接矩形
box = cv2.boxPoints(rect)  # 获得四边形的四个点位置坐标
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()