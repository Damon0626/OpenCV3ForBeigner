# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-18 下午10:02
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import math
'''
画OpenCV的logo，幕布大小是512*512
'''

r1 = 70
r2 = 30

ang = 60
d = 170
h = int(d/2*math.sqrt(3))  # 根据正三角形

dot_red = (256, 128)  # 红色圆圆心
dot_green = (int(dot_red[0] - d/2), dot_red[1] + h)
dot_blue = (int(dot_red[0] + d/2), dot_red[1] + h)

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
black = (0, 0, 0)

full = -1

image = np.zeros((512, 512, 3), np.uint8)

cv2.circle(image, dot_red, r1, red, full)
cv2.circle(image, dot_green, r1, green, full)
cv2.circle(image, dot_blue, r1, blue, full)

cv2.circle(image, dot_red, r2, black, full)
cv2.circle(image, dot_green, r2, black, full)
cv2.circle(image, dot_blue, r2, black, full)

cv2.ellipse(image, dot_red, (r1, r1), ang, 0, ang, black, full)  # 画一个扇形，60度开始画, 0-60度，度数是逆时针的
cv2.ellipse(image, dot_green, (r1, r1), 360-ang, 0, ang, black, full)
cv2.ellipse(image, dot_blue, (r1, r1), 360-2*ang, 0, ang, black, full)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, text="OpenCV", org=(15, 450), fontScale=4, color=(255, 255, 255), thickness=10, fontFace=font)

while True:
	cv2.imshow("image", image)
	if cv2.waitKey(0) == 27:
		break
cv2.destroyAllWindows()