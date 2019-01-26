# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-26 下午9:55
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread('box.png', 0)
img2 = cv2.imread('box_in_scene.png', 0)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
	if m.distance < 0.75*n.distance:
		good.append([m])

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
plt.imshow(img3)
plt.show()