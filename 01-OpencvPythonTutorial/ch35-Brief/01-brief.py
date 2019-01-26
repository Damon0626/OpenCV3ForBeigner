# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-26 下午8:39
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2

img = cv2.imread('blox.jpg', 0)
star = cv2.xfeatures2d.StarDetector_create()
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kp = star.detect(img, None)
kp, des = brief.compute(img, kp)

print(brief.descriptorSize())
print(des.shape)