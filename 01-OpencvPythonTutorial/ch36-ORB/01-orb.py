# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-26 下午9:34
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
ORB是FAST关键点检测和BRIEF关键点描述器的结合体，并做了很多修改增强了性能。
首先他使用FAST找到关键点，然后在使用Harris关键点检测对这些关键点做排序找到前N个点，
他也是用金字塔从而产生尺度不变性特征。

'''

import cv2
import matplotlib.pyplot as plt


img = cv2.imread('../ch35-Brief/blox.jpg', 0)

orb = cv2.ORB_create()
kp = orb.detect(img, None)

kp, des = orb.compute(img, kp)

img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
plt.imshow(img2)
plt.show()