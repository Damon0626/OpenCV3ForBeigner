# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-26 下午9:41
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread('box.png', 0)
img2 = cv2.imread('box_in_scene.png', 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
print(img1.shape)
print(des1.shape)  # 关键点和描述
# print(des2.shape)
# print(len(kp1))
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)  # 匹配

matches = sorted(matches, key=lambda x: x.distance)
# print(matches)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)  # 前十个

plt.imshow(img3)
plt.show()