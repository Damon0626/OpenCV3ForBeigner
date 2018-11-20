# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-20 下午10:19
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import numpy as np

green = np.uint8([[[0, 255, 0]]])  # 三层cvArrar, cvMat, IpImage
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)
black = np.uint8([[[0, 0, 0, ]]])
hsv_black = cv2.cvtColor(black, cv2.COLOR_BGR2HSV)
print(hsv_black)